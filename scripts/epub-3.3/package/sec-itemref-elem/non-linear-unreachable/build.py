# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-itemref-elem/non-linear-unreachable/non-linear-unreachable.epub: Non-linear content nothing links to.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/packagevariants.py.

Run: python3 scripts/epub-3.3/package/sec-itemref-elem/non-linear-unreachable/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402

SET = "epub-3.3/package/sec-itemref-elem/non-linear-unreachable"


def main() -> None:
    info = eb.load_set(
        SET, title='Non-linear content nothing links to',
        description='A non-linear document is in the spine, and no link leads to it. Does a validator reject it?',
        subject="EPUB 3.3 package document")
    files = pv.non_linear_unreachable(epub3.package(info, extra=[("extra", "extra.xhtml", "application/xhtml+xml", "", epub3.xhtml("Extra", pv.section("    <p>An extra document.</p>", "Extra", "extra")))]))
    out = eb.write_epub(info.book_dir / "non-linear-unreachable.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
