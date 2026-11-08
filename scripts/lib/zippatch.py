# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Byte changes made to a finished, reproducible ZIP.

A damaged container cannot come out of a correct ZIP writer, so the books
that show ZIP defects are built in two steps: epubbook.write_epub() makes a
valid book, then one function here changes its bytes. Each function checks
the bytes it is about to change first, and stops if they are not what it
expects, so a change in the template cannot silently move a patch to the
wrong place.

All offsets follow the ZIP application note (APPNOTE.TXT 6.3.10): local file
header 4.3.7, central directory header 4.3.12, end of central directory
record 4.3.16.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

LOCAL_SIG = b"PK\x03\x04"
CENTRAL_SIG = b"PK\x01\x02"
EOCD_SIG = b"PK\x05\x06"


@dataclass
class Entry:
    name: str
    central: int   # offset of its central directory header
    local: int     # offset of its local header, as the central header says


@dataclass
class Layout:
    eocd: int
    cd_offset: int
    cd_size: int
    entries: list[Entry]

    def entry(self, name: str) -> Entry:
        for e in self.entries:
            if e.name == name:
                return e
        raise SystemExit(f"no entry {name!r} in the archive")


def layout(data: bytes) -> Layout:
    """Read a well-formed ZIP (the template's own output)."""
    eocd = data.rfind(EOCD_SIG)
    if eocd < 0 or len(data) - eocd != 22:
        raise SystemExit("expected one EOCD with no comment at the end")
    _, _, _, count, cd_size, cd_offset, _ = struct.unpack_from(
        "<HHHHIIH", data, eocd + 4)
    entries, p = [], cd_offset
    for _ in range(count):
        if data[p:p + 4] != CENTRAL_SIG:
            raise SystemExit(f"no central header at {p}")
        n, m, k = struct.unpack_from("<HHH", data, p + 28)
        local = struct.unpack_from("<I", data, p + 42)[0]
        entries.append(Entry(data[p + 46:p + 46 + n].decode(), p, local))
        p += 46 + n + m + k
    return Layout(eocd, cd_offset, cd_size, entries)


def _u16(data: bytearray, at: int) -> int:
    return struct.unpack_from("<H", data, at)[0]


def _u32(data: bytearray, at: int) -> int:
    return struct.unpack_from("<I", data, at)[0]


def _expect(cond: bool, what: str) -> None:
    if not cond:
        raise SystemExit(f"check before patching failed: {what}")


# --- the patches -----------------------------------------------------------

def insert_in_mimetype_data(data: bytes) -> bytes:
    """insert 22 bytes (an EOCD signature and 18 zero bytes) at file
    offset 40, inside the stored mimetype data. Nothing else changes."""
    _expect(data[30:38] == b"mimetype", "bytes 30-37 are 'mimetype'")
    return data[:40] + EOCD_SIG + bytes(18) + data[40:]


def rename_local(data: bytes, name: str, new: str) -> bytes:
    """write a different name of the same length into the local
    header only."""
    lay, buf = layout(data), bytearray(data)
    e = lay.entry(name)
    n = _u16(buf, e.local + 26)
    _expect(buf[e.local + 30:e.local + 30 + n] == name.encode(),
            f"local header at {e.local} names {name}")
    _expect(len(new.encode()) == n, "the new name has the same length")
    buf[e.local + 30:e.local + 30 + n] = new.encode()
    return bytes(buf)


def local_method_stored(data: bytes, name: str) -> bytes:
    """the local header says stored (0); the central header keeps
    deflated (8)."""
    lay, buf = layout(data), bytearray(data)
    e = lay.entry(name)
    _expect(_u16(buf, e.local + 8) == 8, "local method is 8 (deflated)")
    _expect(_u16(buf, e.central + 10) == 8, "central method is 8")
    struct.pack_into("<H", buf, e.local + 8, 0)
    return bytes(buf)


def local_csize_plus(data: bytes, name: str, delta: int) -> bytes:
    """add `delta` to the compressed size in the local header only."""
    lay, buf = layout(data), bytearray(data)
    e = lay.entry(name)
    local, central = _u32(buf, e.local + 18), _u32(buf, e.central + 20)
    _expect(local == central, "local and central compressed sizes are equal")
    struct.pack_into("<I", buf, e.local + 18, local + delta)
    return bytes(buf)


def local_crc(data: bytes, name: str, value: int) -> bytes:
    """overwrite the CRC-32 in the local header only."""
    lay, buf = layout(data), bytearray(data)
    e = lay.entry(name)
    _expect(_u32(buf, e.local + 14) == _u32(buf, e.central + 16),
            "local and central CRCs are equal")
    struct.pack_into("<I", buf, e.local + 14, value)
    return bytes(buf)


def append_bogus_eocd(data: bytes) -> bytes:
    """append a second EOCD whose central directory (999 bytes at
    offset 99999) cannot fit before it."""
    _expect(data[-22:-18] == EOCD_SIG and data[-2:] == b"\x00\x00",
            "the file ends with an EOCD with no comment")
    return data + EOCD_SIG + struct.pack("<HHHHIIH", 0, 0, 9, 9, 999, 99999, 0)


def join_archives(first: bytes, second: bytes) -> bytes:
    """two complete archives, one after the other."""
    layout(first), layout(second)
    return first + second


def eocd_in_comment(data: bytes) -> bytes:
    """a 24-byte archive comment, 'xx' then an EOCD signature and 18
    zero bytes, so a backward search meets a fake record first."""
    lay, buf = layout(data), bytearray(data)
    _expect(_u16(buf, lay.eocd + 20) == 0, "the comment length is 0")
    comment = b"xx" + EOCD_SIG + bytes(18)
    struct.pack_into("<H", buf, lay.eocd + 20, len(comment))
    return bytes(buf) + comment


def prepend(data: bytes, junk: bytes) -> bytes:
    """bytes before the first local header; no offset adjusted."""
    _expect(data[:4] == LOCAL_SIG, "the file starts with a local header")
    return junk + data


def descriptor_flag(data: bytes, name: str) -> bytes:
    """set bit 3 of the general purpose flag in the local and the
    central header; write no data descriptor."""
    lay, buf = layout(data), bytearray(data)
    e = lay.entry(name)
    lf, cf = _u16(buf, e.local + 6), _u16(buf, e.central + 8)
    _expect(not lf & 8 and not cf & 8, "bit 3 is clear in both headers")
    struct.pack_into("<H", buf, e.local + 6, lf | 8)
    struct.pack_into("<H", buf, e.central + 8, cf | 8)
    return bytes(buf)


def cd_offset_minus(data: bytes, delta: int) -> bytes:
    """subtract `delta` from the central directory offset in the
    EOCD."""
    lay, buf = layout(data), bytearray(data)
    _expect(buf[lay.cd_offset:lay.cd_offset + 4] == CENTRAL_SIG,
            "the EOCD offset points at the central directory")
    struct.pack_into("<I", buf, lay.eocd + 16, lay.cd_offset - delta)
    return bytes(buf)
