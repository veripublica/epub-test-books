# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ops/Section1.3.5/css-position-absolute/css-position-absolute.epub: position: absolute in a stylesheet (valid).

The EPUB 2 template's files with the change for this set, made with
scripts/lib/opsvariants.py.

Run: python3 scripts/epub-2.0.1/ops/Section1.3.5/css-position-absolute/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402,F401
import epubbook as eb  # noqa: E402
import opsvariants as ov  # noqa: E402

SET = "epub-2.0.1/ops/Section1.3.5/css-position-absolute"


def main() -> None:
    info = eb.load_set(
        SET, title='position: absolute in a stylesheet (valid)',
        description='A linked stylesheet sets position: absolute on p. OPS 2.0.1 strongly discourages it. Does a validator accept it?',
        subject="EPUB 2.0.1 content documents")
    files = epub2.package(info, content=ov.doc(epub2, '    <p>x</p>', head=[ov.LINK]), extra=[ov.css('p { position: absolute; top: 0; }\n')])
    out = eb.write_epub(info.book_dir / "css-position-absolute.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
