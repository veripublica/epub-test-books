# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/css-cascade-5/at-import/import-missing/import-missing.epub: An @import of a file that is not in the container.

The EPUB 3 template with one linked stylesheet, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/css-cascade-5/at-import/import-missing/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "css-cascade-5/at-import/import-missing"
CSS = '@import "missing.css";\np { margin: 0; }\n'


def main() -> None:
    info = eb.load_set(
        SET, title='An @import of a file that is not in the container',
        description='style.css holds @import "missing.css";, then p { margin: 0; }, and there is no missing.css. Does a validator reject the book?',
        subject='CSS Cascading and Inheritance Level 5')
    content = rv.head_link(epub3.xhtml("Content", pv.section('    <p class="x">Content.</p>')), "style.css")
    extra = [("style", "style.css", "text/css", "", CSS.encode("utf-8"))]
    files = epub3.package(info, content=content, extra=extra)
    out = eb.write_epub(info.book_dir / "import-missing.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
