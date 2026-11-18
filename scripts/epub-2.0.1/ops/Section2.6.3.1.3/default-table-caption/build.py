# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ops/Section2.6.3.1.3/default-table-caption/default-table-caption.epub: An ops:switch standing for a table's caption.

The EPUB 2 template's files with the change for this set, made with
scripts/lib/opsvariants.py.

Run: python3 scripts/epub-2.0.1/ops/Section2.6.3.1.3/default-table-caption/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402,F401
import epubbook as eb  # noqa: E402
import opsvariants as ov  # noqa: E402

SET = "epub-2.0.1/ops/Section2.6.3.1.3/default-table-caption"


def main() -> None:
    info = eb.load_set(
        SET, title="An ops:switch standing for a table's caption",
        description='In content.xhtml, a table starts with an ops:switch whose ops:default holds a caption, and then has a row. Does a validator accept it?',
        subject="EPUB 2.0.1 content documents")
    files = epub2.package(info, content=ov.doc(epub2, '    <table><ops:switch xmlns:ops="http://www.idpf.org/2007/ops"><ops:case required-namespace="http://www.w3.org/1998/Math/MathML"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></ops:case><ops:default><caption>c</caption></ops:default></ops:switch><tr><td>a</td></tr></table>'))
    out = eb.write_epub(info.book_dir / "default-table-caption.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
