# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ops/Section2.6.3.1.1/switch-in-paragraph/switch-in-paragraph.epub: An ops:switch inside a p.

The EPUB 2 template's files with the change for this set, made with
scripts/lib/opsvariants.py.

Run: python3 scripts/epub-2.0.1/ops/Section2.6.3.1.1/switch-in-paragraph/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402,F401
import epubbook as eb  # noqa: E402
import opsvariants as ov  # noqa: E402

SET = "epub-2.0.1/ops/Section2.6.3.1.1/switch-in-paragraph"


def main() -> None:
    info = eb.load_set(
        SET, title='An ops:switch inside a p',
        description='In content.xhtml, an ops:switch stands inside a p, between two runs of text. Its ops:default holds an em. Does a validator accept it?',
        subject="EPUB 2.0.1 content documents")
    files = epub2.package(info, content=ov.doc(epub2, '    <p>The value is <ops:switch xmlns:ops="http://www.idpf.org/2007/ops"><ops:case required-namespace="http://www.w3.org/1998/Math/MathML"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></ops:case><ops:default><em>x</em></ops:default></ops:switch>.</p>'))
    out = eb.write_epub(info.book_dir / "switch-in-paragraph.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
