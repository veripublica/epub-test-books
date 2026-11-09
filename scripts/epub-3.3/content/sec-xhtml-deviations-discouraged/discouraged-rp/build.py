# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-xhtml-deviations-discouraged/discouraged-rp/discouraged-rp.epub: The rp element (valid).

The EPUB 3 template's files with one change for this set, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/content/sec-xhtml-deviations-discouraged/discouraged-rp/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/content/sec-xhtml-deviations-discouraged/discouraged-rp"


def doc(inner: str) -> str:
    return epub3.xhtml("Content", pv.section(inner))


def main() -> None:
    info = eb.load_set(
        SET, title='The rp element (valid)',
        description='The content document uses rp in ruby markup. Does a validator accept it?',
        subject="EPUB 3.3 content documents")
    files = epub3.package(info, content=doc('    <p><ruby>x<rp>(</rp><rt>y</rt><rp>)</rp></ruby></p>'))
    out = eb.write_epub(info.book_dir / "discouraged-rp.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
