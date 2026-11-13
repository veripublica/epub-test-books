# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-reserved-prefixes/z3998-undeclared/z3998-undeclared.epub: The prefix z3998 used without a declaration.

The EPUB 3 template's files, changed by scripts/lib/xhtmlextvariants.py `z3998_undeclared()`.

Run: python3 scripts/epub-3.3/content/sec-reserved-prefixes/z3998-undeclared/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import xhtmlextvariants as xv  # noqa: E402

SET = "epub-3.3/content/sec-reserved-prefixes/z3998-undeclared"


def main() -> None:
    info = eb.load_set(
        SET, title='The prefix z3998 used without a declaration',
        description='content.xhtml uses epub:type="z3998:fiction" without declaring z3998. Does a validator reject it?',
        subject="EPUB 3.3 content documents")
    out = eb.write_epub(info.book_dir / "z3998-undeclared.epub", xv.z3998_undeclared(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
