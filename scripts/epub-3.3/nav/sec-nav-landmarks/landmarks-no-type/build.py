# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/nav/sec-nav-landmarks/landmarks-no-type/landmarks-no-type.epub: A landmarks link without epub:type.

The EPUB 3 template's files with one change to the navigation document, made
with scripts/lib/navvariants.py.

Run: python3 scripts/epub-3.3/nav/sec-nav-landmarks/landmarks-no-type/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import navvariants as nv  # noqa: E402

SET = "epub-3.3/nav/sec-nav-landmarks/landmarks-no-type"


def main() -> None:
    info = eb.load_set(
        SET, title='A landmarks link without epub:type',
        description='An a element in the landmarks nav has no epub:type. Does a validator reject it?',
        subject="EPUB 3.3 navigation document")
    files = nv.landmarks_no_type(epub3.package(info))
    out = eb.write_epub(info.book_dir / "landmarks-no-type.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
