# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""A small ZIP writer that controls every header field.

epubbook.write_epub() writes correct containers with Python's zipfile. Some
sets need a container zipfile will not write: a compressed or misplaced
mimetype, an extra field, a non-UTF-8 name, another compression method,
traditional ZIP encryption, ZIP64 fields on an entry that does not need them.
This writer builds those directly, and is reproducible in the same way
(fixed 1980-01-01 times, fixed attributes, entries in the order given).
"""
import struct, zlib, bz2
from dataclasses import dataclass, field

DOS_TIME, DOS_DATE = 0, (0 << 9) | (1 << 5) | 1   # 1980-01-01 00:00


@dataclass
class E:
    name: str | bytes
    data: bytes
    method: int = 8            # 0 stored, 8 deflate, 12 bzip2
    flags: int = 0x0800        # bit 11: UTF-8 names
    version: int | None = None # version needed; default 10 or 20
    extra: bytes = b""
    raw_name: bool = False     # name already bytes, no encoding
    password: bytes | None = None  # traditional PKWARE encryption (APPNOTE 6.1)
    zip64: bool = False        # sizes as 0xFFFFFFFF, real ones in a ZIP64 extra field (APPNOTE 4.5.3), both headers


def _compress(data, method):
    if method == 0:
        return data
    if method == 8:
        c = zlib.compressobj(9, zlib.DEFLATED, -15)
        return c.compress(data) + c.flush()
    if method == 12:
        return bz2.compress(data, 9)
    raise ValueError(method)


_CRC_TABLE = []
for _n in range(256):
    _c = _n
    for _ in range(8):
        _c = (_c >> 1) ^ 0xEDB88320 if _c & 1 else _c >> 1
    _CRC_TABLE.append(_c)


def _zipcrypto(data, password, crc):
    """Traditional PKWARE encryption (APPNOTE 6.1). The 12-byte encryption
    header is fixed rather than random, so the build stays reproducible: 11
    zero bytes, then the high byte of the CRC-32 as the check byte."""
    keys = [0x12345678, 0x23456789, 0x34567890]

    def update(b):
        keys[0] = (keys[0] >> 8) ^ _CRC_TABLE[(keys[0] ^ b) & 0xFF]
        keys[1] = ((keys[1] + (keys[0] & 0xFF)) * 134775813 + 1) & 0xFFFFFFFF
        keys[2] = (keys[2] >> 8) ^ _CRC_TABLE[(keys[2] ^ (keys[1] >> 24)) & 0xFF]

    for b in password:
        update(b)
    out = bytearray()
    for b in bytes(11) + bytes([crc >> 24]) + data:
        t = (keys[2] | 2) & 0xFFFF
        out.append(b ^ (((t * (t ^ 1)) >> 8) & 0xFF))
        update(b)
    return bytes(out)


def build(entries, comment=b""):
    out, central = bytearray(), bytearray()
    for e in entries:
        name = e.name if isinstance(e.name, bytes) else e.name.encode("utf-8")
        comp = _compress(e.data, e.method)
        crc = zlib.crc32(e.data) & 0xFFFFFFFF
        flags = e.flags
        if e.password is not None:
            comp, flags = _zipcrypto(comp, e.password, crc), flags | 1
        ver = e.version if e.version is not None else (45 if e.zip64 else 10 if e.method == 0 else 20)
        off = len(out)
        csize, usize, extra, cextra, made = len(comp), len(e.data), e.extra, b"", 20
        if e.zip64:
            z64 = struct.pack("<HHQQ", 0x0001, 16, usize, csize)
            csize = usize = 0xFFFFFFFF
            extra, cextra, made = extra + z64, z64, 45
        out += struct.pack("<IHHHHHIIIHH", 0x04034B50, ver, flags, e.method,
                           DOS_TIME, DOS_DATE, crc, csize, usize,
                           len(name), len(extra)) + name + extra + comp
        central += struct.pack("<IHHHHHHIIIHHHHHII", 0x02014B50, (3 << 8) | made, ver,
                               flags, e.method, DOS_TIME, DOS_DATE, crc, csize,
                               usize, len(name), len(cextra), 0, 0, 0,
                               0o100644 << 16, off) + name + cextra
    cd_off = len(out)
    out += central
    out += struct.pack("<IHHHHIIH", 0x06054B50, 0, 0, len(entries), len(entries),
                       len(central), cd_off, len(comment)) + comment
    return bytes(out)


def entries_from(files):
    """Template file list (after mimetype) -> E list with mimetype first, stored."""
    return [E("mimetype", b"application/epub+zip", method=0)] + [
        E(n, d.encode() if isinstance(d, str) else d) for n, d in files]
