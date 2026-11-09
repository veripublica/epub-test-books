# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""A generated baseline JPEG: an 8x8 square of mid gray.

No image library and no outside image. With every quantisation value at 1
and a sample value of 128, the single block's DC coefficient is 0 and it has
no AC coefficients, so the scan is one Huffman code for "DC category 0", one
for "end of block", and padding.
"""

from __future__ import annotations

import struct


def _segment(marker: int, body: bytes) -> bytes:
    return struct.pack(">BBH", 0xFF, marker, len(body) + 2) + body


def _huffman(table: int) -> bytes:
    """A table with one symbol, 0, whose code is the single bit 0."""
    return _segment(0xC4, bytes([table]) + bytes([1] + [0] * 15) + b"\x00")


def gray_jpeg() -> bytes:
    return b"".join([
        b"\xff\xd8",
        _segment(0xE0, b"JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00"),
        _segment(0xDB, b"\x00" + b"\x01" * 64),
        _segment(0xC0, b"\x08\x00\x08\x00\x08\x01\x01\x11\x00"),
        _huffman(0x00),
        _huffman(0x10),
        _segment(0xDA, b"\x01\x01\x00\x00\x3f\x00"),
        b"\x3f",  # DC code 0, end-of-block code 0, then six padding 1s
        b"\xff\xd9",
    ])
