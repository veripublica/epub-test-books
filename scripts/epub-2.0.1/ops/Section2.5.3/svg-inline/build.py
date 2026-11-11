# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ops/Section2.5.3/svg-inline/svg-inline.epub: SVG inside a content document (valid).

The EPUB 2 template's files with the change for this set, made with
scripts/lib/opsvariants.py.

Run: python3 scripts/epub-2.0.1/ops/Section2.5.3/svg-inline/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402,F401
import epubbook as eb  # noqa: E402
import opsvariants as ov  # noqa: E402

SET = "epub-2.0.1/ops/Section2.5.3/svg-inline"


def main() -> None:
    info = eb.load_set(
        SET, title='SVG inside a content document (valid)',
        description='content.xhtml has an svg element, in the SVG namespace, inside a div. Does a validator accept it?',
        subject="EPUB 2.0.1 content documents")
    files = epub2.package(info, content=ov.doc(epub2, '    <div><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 40 40"><rect width="40" height="40" fill="gray"/></svg></div>'))
    out = eb.write_epub(info.book_dir / "svg-inline.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
