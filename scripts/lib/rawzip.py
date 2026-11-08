# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""A small ZIP writer that controls every header field.

epubbook.write_epub() writes correct containers with Python's zipfile. Some
sets need a container zipfile will not write: a compressed or misplaced
mimetype, an extra field, a non-UTF-8 name, another compression method.
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


def _compress(data, method):
    if method == 0:
        return data
    if method == 8:
        c = zlib.compressobj(9, zlib.DEFLATED, -15)
        return c.compress(data) + c.flush()
    if method == 12:
        return bz2.compress(data, 9)
    raise ValueError(method)


def build(entries, comment=b""):
    out, central = bytearray(), bytearray()
    for e in entries:
        name = e.name if isinstance(e.name, bytes) else e.name.encode("utf-8")
        comp = _compress(e.data, e.method)
        crc = zlib.crc32(e.data) & 0xFFFFFFFF
        ver = e.version if e.version is not None else (10 if e.method == 0 else 20)
        off = len(out)
        out += struct.pack("<IHHHHHIIIHH", 0x04034B50, ver, e.flags, e.method,
                           DOS_TIME, DOS_DATE, crc, len(comp), len(e.data),
                           len(name), len(e.extra)) + name + e.extra + comp
        central += struct.pack("<IHHHHHHIIIHHHHHII", 0x02014B50, (3 << 8) | 20, ver,
                               e.flags, e.method, DOS_TIME, DOS_DATE, crc, len(comp),
                               len(e.data), len(name), 0, 0, 0, 0,
                               0o100644 << 16, off) + name
    cd_off = len(out)
    out += central
    out += struct.pack("<IHHHHIIH", 0x06054B50, 0, 0, len(entries), len(entries),
                       len(central), cd_off, len(comment)) + comment
    return bytes(out)


def entries_from(files):
    """Template file list (after mimetype) -> E list with mimetype first, stored."""
    return [E("mimetype", b"application/epub+zip", method=0)] + [
        E(n, d.encode() if isinstance(d, str) else d) for n, d in files]
