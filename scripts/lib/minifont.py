# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""A minimal TrueType font, written byte by byte, and the EPUB font
obfuscation algorithm.

The font has two glyphs: .notdef, a box, and the space (U+0020). It is made
here so the books that need a font carry one with no licence question and no
dependency. Every field is fixed, the dates included, so the bytes are the
same on every build.

`obfuscate(font, identifier)` follows EPUB 3.3 §4.4 (sec-font-obfuscation):
the key is the SHA-1 of the unique identifier with all white space removed,
and the first 1040 bytes of the font are XORed with it.
"""

from __future__ import annotations

import hashlib
import re
import struct

FAMILY = "epub-test-books Box"
COPYRIGHT = "Copyright (c) 2026 Baris Kayadelen (veripublica). CC BY 4.0."
# head.created and head.modified: 2026-11-08 00:00 UTC, in seconds since 1904-01-01
DATE = 3876940800


def _checksum(data: bytes) -> int:
    data += b"\0" * (-len(data) % 4)
    return sum(struct.unpack(f">{len(data) // 4}I", data)) & 0xFFFFFFFF


def _name_table() -> bytes:
    names = {0: COPYRIGHT, 1: FAMILY, 2: "Regular", 3: FAMILY + " 1.0",
             4: FAMILY, 5: "Version 1.0", 6: "epub-test-books-Box"}
    records, strings = b"", b""
    for nid, text in names.items():
        s = text.encode("utf-16-be")
        records += struct.pack(">HHHHHH", 3, 1, 0x409, nid, len(s), len(strings))
        strings += s
    return struct.pack(">HHH", 0, len(names), 6 + len(records)) + records + strings


def font() -> bytes:
    # .notdef: one clockwise rectangle (50,0)-(450,700); space: no outline
    notdef = (struct.pack(">hhhhh", 1, 50, 0, 450, 700) + struct.pack(">HH", 3, 0)
              + bytes([1, 1, 1, 1]) + struct.pack(">hhhh", 50, 0, 400, 0)
              + struct.pack(">hhhh", 0, 700, 0, -700))
    assert len(notdef) == 34
    tables = {
        b"OS/2": struct.pack(
            ">HhHHH10hh10s4I4sHHHhhhHH2IhhHHH",
            4, 375, 400, 5, 0,
            650, 700, 0, 140, 650, 700, 0, 480, 50, 250,
            0, bytes(10), 1, 0, 0, 0, b"VPUB", 0x40, 0x20, 0x20,
            800, -200, 0, 800, 200, 1, 0, 500, 700, 0, 0x20, 1),
        b"cmap": struct.pack(">HHHHI", 0, 1, 3, 1, 12) + struct.pack(
            ">HHHHHHH2HH2H2h2H", 4, 32, 0, 4, 4, 1, 0,
            0x20, 0xFFFF, 0, 0x20, 0xFFFF, 1 - 0x20, 1, 0, 0),
        b"glyf": notdef,
        b"head": struct.pack(">IIIIHHqqhhhhHHhhh", 0x00010000, 0x00010000, 0,
                             0x5F0F3CF5, 0x000B, 1000, DATE, DATE, 50, 0, 450, 700,
                             0, 8, 2, 0, 0),
        b"hhea": struct.pack(">I15hH", 0x00010000, 800, -200, 0, 500, 50, 50,
                             450, 1, 0, 0, 0, 0, 0, 0, 0, 2),
        b"hmtx": struct.pack(">HhHh", 500, 50, 250, 0),
        b"loca": struct.pack(">HHH", 0, 17, 17),
        b"maxp": struct.pack(">I14H", 0x00010000, 2, 4, 1, 0, 0, 2, 0, 0, 0, 0,
                             0, 0, 0, 0),
        b"name": _name_table(),
        b"post": struct.pack(">IIhhIIIII", 0x00030000, 0, -100, 50, 0, 0, 0, 0, 0),
    }
    assert len(tables[b"OS/2"]) == 96 and len(tables[b"head"]) == 54
    assert len(tables[b"hhea"]) == 36 and len(tables[b"maxp"]) == 32
    tags = sorted(tables)
    n = len(tags)
    es = n.bit_length() - 1
    header = struct.pack(">IHHHH", 0x00010000, n, 16 << es, es, n * 16 - (16 << es))
    offset = 12 + 16 * n
    directory, body, head_at = b"", b"", 0
    for tag in tags:
        data = tables[tag]
        if tag == b"head":
            head_at = offset + len(body)
        directory += struct.pack(">4sIII", tag, _checksum(data), offset + len(body), len(data))
        body += data + b"\0" * (-len(data) % 4)
    out = bytearray(header + directory + body)
    adjust = (0xB1B0AFBA - _checksum(bytes(out))) & 0xFFFFFFFF
    out[head_at + 8:head_at + 12] = struct.pack(">I", adjust)
    return bytes(out)


def obfuscation_key(identifier: str) -> bytes:
    return hashlib.sha1(re.sub("[\x20\x09\x0d\x0a]", "", identifier).encode("utf-8")).digest()


def obfuscate(data: bytes, identifier: str) -> bytes:
    key = obfuscation_key(identifier)
    head = bytes(b ^ key[i % 20] for i, b in enumerate(data[:1040]))
    return head + data[1040:]
