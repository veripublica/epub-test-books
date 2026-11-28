# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.4/resources/sec-core-media-types/core-audio-mp4-aac-codecs/core-audio-mp4-aac-codecs.epub: AAC audio in MP4, audio/mp4; codecs=aac (valid).

The EPUB 3 template, with the change for this set, following EPUB 3.4.

Run: python3 scripts/epub-3.4/resources/sec-core-media-types/core-audio-mp4-aac-codecs/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import encodedmedia as em  # noqa: E402,F401
import epubbook as eb  # noqa: E402
import layoutvariants as lv  # noqa: E402,F401
import minifont as mf  # noqa: E402,F401
import navvariants as nv  # noqa: E402,F401
import packagevariants as pv  # noqa: E402,F401
import resourcevariants as rv  # noqa: E402,F401

SET = "epub-3.4/resources/sec-core-media-types/core-audio-mp4-aac-codecs"


def main() -> None:
    info = eb.load_set(
        SET, title='AAC audio in MP4, audio/mp4; codecs=aac (valid)',
        description='content.xhtml plays AAC LC audio in an MP4 container, declared as audio/mp4; codecs=aac, with no fallback. Does a validator accept the book?',
        subject="EPUB 3.4 publication resources")
    content = epub3.xhtml("Content", pv.section('    <p><audio src="sound.mp4" controls="controls">No audio.</audio></p>'))
    files = rv.book_has_audio(epub3.package(info, content=content, extra=[("sound", "sound.mp4", "audio/mp4; codecs=aac", "", em.silent_aac_mp4())]))
    out = eb.write_epub(info.book_dir / "core-audio-mp4-aac-codecs.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
