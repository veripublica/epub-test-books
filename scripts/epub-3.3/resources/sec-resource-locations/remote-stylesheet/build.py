# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/resources/sec-resource-locations/remote-stylesheet/remote-stylesheet.epub: A stylesheet outside the container.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/resources/sec-resource-locations/remote-stylesheet/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/resources/sec-resource-locations/remote-stylesheet"


def doc(inner: str) -> str:
    return epub3.xhtml("Content", pv.section(inner))


def main() -> None:
    info = eb.load_set(
        SET, title='A stylesheet outside the container',
        description='The content document links to a stylesheet at an https URL, listed in the manifest. Does a validator reject it?',
        subject="EPUB 3.3 publication resources")
    files = rv.add_item(epub3.package(info, content=rv.head_link(doc("    <p>Content.</p>"), rv.REMOTE + "style.css")), f'<item id="remote" href="{rv.REMOTE}style.css" media-type="text/css"/>')
    out = eb.write_epub(info.book_dir / "remote-stylesheet.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
