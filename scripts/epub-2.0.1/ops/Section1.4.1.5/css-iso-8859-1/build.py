# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ops/Section1.4.1.5/css-iso-8859-1/css-iso-8859-1.epub: A stylesheet in ISO-8859-1.

The EPUB 2 template's files with the change for this set, made with
scripts/lib/opsvariants.py.

Run: python3 scripts/epub-2.0.1/ops/Section1.4.1.5/css-iso-8859-1/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402,F401
import epubbook as eb  # noqa: E402
import opsvariants as ov  # noqa: E402

SET = "epub-2.0.1/ops/Section1.4.1.5/css-iso-8859-1"


def main() -> None:
    info = eb.load_set(
        SET, title='A stylesheet in ISO-8859-1',
        description='A linked stylesheet is encoded in ISO-8859-1 and says so with @charset. Does a validator reject it?',
        subject="EPUB 2.0.1 content documents")
    files = epub2.package(info, content=ov.doc(epub2, '    <p>x</p>', head=[ov.LINK]), extra=[ov.css('@charset "ISO-8859-1";\np::before { content: "\u00e9"; }\n'.encode('iso-8859-1'))])
    out = eb.write_epub(info.book_dir / "css-iso-8859-1.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
