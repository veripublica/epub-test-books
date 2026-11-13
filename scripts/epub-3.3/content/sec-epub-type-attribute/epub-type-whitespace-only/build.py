# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-epub-type-attribute/epub-type-whitespace-only/epub-type-whitespace-only.epub: An epub:type of spaces only.

The EPUB 3 template's files, changed by scripts/lib/xhtmlextvariants.py `type_whitespace_only()`.

Run: python3 scripts/epub-3.3/content/sec-epub-type-attribute/epub-type-whitespace-only/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import xhtmlextvariants as xv  # noqa: E402

SET = "epub-3.3/content/sec-epub-type-attribute/epub-type-whitespace-only"


def main() -> None:
    info = eb.load_set(
        SET, title='An epub:type of spaces only',
        description='content.xhtml has epub:type="  " (two spaces). Does a validator reject it?',
        subject="EPUB 3.3 content documents")
    out = eb.write_epub(info.book_dir / "epub-type-whitespace-only.epub", xv.type_whitespace_only(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
