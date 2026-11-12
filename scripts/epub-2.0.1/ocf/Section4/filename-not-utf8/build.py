# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ocf/Section4/filename-not-utf8/filename-not-utf8.epub: A file name that is not UTF-8.

The EPUB 2 template's files are built for this set, then written as a
container by scripts/lib/ocf2variants.py.

Run: python3 scripts/epub-2.0.1/ocf/Section4/filename-not-utf8/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epubbook as eb  # noqa: E402
import ocf2variants as ov2  # noqa: E402

SET = "epub-2.0.1/ocf/Section4/filename-not-utf8"


def main() -> None:
    info = eb.load_set(
        SET, title='A file name that is not UTF-8',
        description="The content document's name in the ZIP is OEBPS/c\\x81ntent.xhtml, with the UTF-8 flag clear. Does a validator reject the book?",
        subject="EPUB 2.0.1 OCF")
    files = epub2.package(info)
    out = info.book_dir / "filename-not-utf8.epub"
    out.write_bytes(ov2.filename_not_utf8(files))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
