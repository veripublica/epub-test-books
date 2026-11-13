# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-reserved-prefixes/reserved-prefix-msv/reserved-prefix-msv.epub: The reserved prefix msv used without a declaration (valid).

The EPUB 3 template's files, changed by scripts/lib/xhtmlextvariants.py `reserved_prefix_msv()`.

Run: python3 scripts/epub-3.3/content/sec-reserved-prefixes/reserved-prefix-msv/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import xhtmlextvariants as xv  # noqa: E402

SET = "epub-3.3/content/sec-reserved-prefixes/reserved-prefix-msv"


def main() -> None:
    info = eb.load_set(
        SET, title='The reserved prefix msv used without a declaration (valid)',
        description='content.xhtml uses epub:type="msv:article" without declaring msv. Does a validator accept the book?',
        subject="EPUB 3.3 content documents")
    out = eb.write_epub(info.book_dir / "reserved-prefix-msv.epub", xv.reserved_prefix_msv(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
