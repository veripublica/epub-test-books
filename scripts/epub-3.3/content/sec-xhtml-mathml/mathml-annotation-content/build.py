# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-xhtml-mathml/mathml-annotation-content/mathml-annotation-content.epub: Content MathML in an annotation (valid).

The EPUB 3 template's files with one change for this set, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/content/sec-xhtml-mathml/mathml-annotation-content/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/content/sec-xhtml-mathml/mathml-annotation-content"


def doc(inner: str) -> str:
    return epub3.xhtml("Content", pv.section(inner))


def main() -> None:
    info = eb.load_set(
        SET, title='Content MathML in an annotation (valid)',
        description='A math element holds Content MathML in an annotation-xml with the required encoding and name. Does a validator accept it?',
        subject="EPUB 3.3 content documents")
    files = rv.content_properties(epub3.package(info, content=doc('    <p><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="x"><semantics><mi>x</mi><annotation-xml encoding="MathML-Content" name="contentequiv"><ci>x</ci></annotation-xml></semantics></math></p>')), "mathml")
    out = eb.write_epub(info.book_dir / "mathml-annotation-content.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
