# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/css-cascade-5/at-import/import-layer/import-layer.epub: A stylesheet imported into a layer, @import url("b.css") layer(base) (valid).

The EPUB 3 template with one linked stylesheet (and b.css, which it imports), made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/css-cascade-5/at-import/import-layer/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "css-cascade-5/at-import/import-layer"
CSS = '@import url("b.css") layer(base);\np { margin: 0; }\n'
B_CSS = 'p { margin: 0; }\n'


def main() -> None:
    info = eb.load_set(
        SET, title='A stylesheet imported into a layer, @import url("b.css") layer(base) (valid)',
        description='style.css holds @import url("b.css") layer(base);, then p { margin: 0; }; b.css, also in the manifest, holds p { margin: 0; }. Does a validator accept the book?',
        subject='CSS Cascading and Inheritance Level 5')
    content = rv.head_link(epub3.xhtml("Content", pv.section('    <p class="x">Content.</p>')), "style.css")
    extra = [("style", "style.css", "text/css", "", CSS.encode("utf-8"))]
    extra.append(("b", "b.css", "text/css", "", B_CSS.encode("utf-8")))
    files = epub3.package(info, content=content, extra=extra)
    out = eb.write_epub(info.book_dir / "import-layer.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
