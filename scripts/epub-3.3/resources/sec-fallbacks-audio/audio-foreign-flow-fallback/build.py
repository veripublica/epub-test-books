# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/resources/sec-fallbacks-audio/audio-foreign-flow-fallback/audio-foreign-flow-fallback.epub: Foreign audio with only flow content as a fallback.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/resources/sec-fallbacks-audio/audio-foreign-flow-fallback/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/resources/sec-fallbacks-audio/audio-foreign-flow-fallback"


def doc(inner: str) -> str:
    return epub3.xhtml("Content", pv.section(inner))


def main() -> None:
    info = eb.load_set(
        SET, title='Foreign audio with only flow content as a fallback',
        description='An audio element plays a WAV file, which is a foreign resource, and its only fallback is a paragraph inside it. Does a validator reject it?',
        subject="EPUB 3.3 publication resources")
    files = rv.book_has_audio(epub3.package(info, content=doc('    <audio src="sound.wav" controls="controls"><p>No audio.</p></audio>'), extra=[rv.WAV]))
    out = eb.write_epub(info.book_dir / "audio-foreign-flow-fallback.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
