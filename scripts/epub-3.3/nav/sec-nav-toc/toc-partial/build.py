# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/nav/sec-nav-toc/toc-partial/toc-partial.epub: A toc that omits a spine item (valid).

The EPUB 3 template's files with one change to the navigation document, made
with scripts/lib/navvariants.py.

Run: python3 scripts/epub-3.3/nav/sec-nav-toc/toc-partial/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import navvariants as nv  # noqa: E402

SET = "epub-3.3/nav/sec-nav-toc/toc-partial"


def main() -> None:
    info = eb.load_set(
        SET, title='A toc that omits a spine item (valid)',
        description='The toc nav links to only one of the two spine documents. Does a validator accept it?',
        subject="EPUB 3.3 navigation document")
    files = nv.toc_partial(epub3.package(info))
    out = eb.write_epub(info.book_dir / "toc-partial.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
