# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/resources/sec-resource-locations/remote-audio/remote-audio.epub: Audio outside the container (valid).

The EPUB 3 template's files with one change for this set, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/resources/sec-resource-locations/remote-audio/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/resources/sec-resource-locations/remote-audio"


def doc(inner: str) -> str:
    return epub3.xhtml("Content", pv.section(inner))


def main() -> None:
    info = eb.load_set(
        SET, title='Audio outside the container (valid)',
        description='An audio element plays an MP3 at an https URL, listed in the manifest, and the content item has remote-resources. Does a validator accept it?',
        subject="EPUB 3.3 publication resources")
    files = rv.content_properties(rv.add_item(rv.book_has_audio(epub3.package(info, content=doc(f'    <audio src="{rv.REMOTE}sound.mp3" controls="controls"></audio>'))), f'<item id="remote" href="{rv.REMOTE}sound.mp3" media-type="audio/mpeg"/>'), "remote-resources")
    out = eb.write_epub(info.book_dir / "remote-audio.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
