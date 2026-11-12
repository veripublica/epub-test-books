# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Small generated media files: formats that are not EPUB core media types, and silent MP3.

No outside files: every byte comes from these functions, so the sets that
need a foreign resource stay reproducible and carry nothing copied.
"""

from __future__ import annotations

import io
import struct
import wave


def gray_bmp() -> bytes:
    """A 1x1 24-bit BMP, mid gray."""
    pixels = b"\x80\x80\x80\x00"
    header = struct.pack("<2sIHHI", b"BM", 54 + len(pixels), 0, 0, 54)
    info = struct.pack("<IiiHHIIiiII", 40, 1, 1, 1, 24, 0, len(pixels), 2835, 2835, 0, 0)
    return header + info + pixels


def gray_xbm() -> bytes:
    """A 1x1 X BitMap, which is plain text."""
    return (b"#define x_width 1\n#define x_height 1\n"
            b"static unsigned char x_bits[] = { 0x01 };\n")


def silent_wav() -> bytes:
    """A tenth of a second of silence."""
    out = io.BytesIO()
    with wave.open(out, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(1)
        w.setframerate(8000)
        w.writeframes(b"\x80" * 800)
    return out.getvalue()


def silent_mp3(frames: int = 125) -> bytes:
    """Silent MPEG-1 Layer III audio, 24 ms per frame (125 frames = 3 s).

    Each frame is a 4-byte header (64 kbit/s, 48 kHz, mono, no CRC) and
    188 zero bytes: all-zero side information codes no samples, which
    decoders play as silence.
    """
    return (b"\xff\xfb\x54\xc0" + b"\x00" * 188) * frames
