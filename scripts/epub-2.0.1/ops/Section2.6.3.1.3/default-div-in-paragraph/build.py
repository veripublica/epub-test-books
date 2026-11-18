# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ops/Section2.6.3.1.3/default-div-in-paragraph/default-div-in-paragraph.epub: An ops:switch in a p, with a div in its default.

The EPUB 2 template's files with the change for this set, made with
scripts/lib/opsvariants.py.

Run: python3 scripts/epub-2.0.1/ops/Section2.6.3.1.3/default-div-in-paragraph/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402,F401
import epubbook as eb  # noqa: E402
import opsvariants as ov  # noqa: E402

SET = "epub-2.0.1/ops/Section2.6.3.1.3/default-div-in-paragraph"


def main() -> None:
    info = eb.load_set(
        SET, title='An ops:switch in a p, with a div in its default',
        description='In content.xhtml, a p holds an ops:switch whose ops:default holds a div. Does a validator reject it?',
        subject="EPUB 2.0.1 content documents")
    files = epub2.package(info, content=ov.doc(epub2, '    <p>a <ops:switch xmlns:ops="http://www.idpf.org/2007/ops"><ops:case required-namespace="http://www.w3.org/1998/Math/MathML"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></ops:case><ops:default><div>b</div></ops:default></ops:switch></p>'))
    out = eb.write_epub(info.book_dir / "default-div-in-paragraph.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
