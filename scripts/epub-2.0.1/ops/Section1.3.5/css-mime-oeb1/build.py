# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ops/Section1.3.5/css-mime-oeb1/css-mime-oeb1.epub: A stylesheet with the deprecated text/x-oeb1-css type (valid).

The EPUB 2 template's files with the change for this set, made with
scripts/lib/opsvariants.py.

Run: python3 scripts/epub-2.0.1/ops/Section1.3.5/css-mime-oeb1/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402,F401
import epubbook as eb  # noqa: E402
import opsvariants as ov  # noqa: E402

SET = "epub-2.0.1/ops/Section1.3.5/css-mime-oeb1"


def main() -> None:
    info = eb.load_set(
        SET, title='A stylesheet with the deprecated text/x-oeb1-css type (valid)',
        description='A linked stylesheet has the media type text/x-oeb1-css in the manifest and on the link. The type is deprecated. Does a validator accept it?',
        subject="EPUB 2.0.1 content documents")
    files = epub2.package(info, content=ov.doc(epub2, '    <p>x</p>', head=[ov.LINK.replace('text/css', 'text/x-oeb1-css')]), extra=[ov.css('p { margin: 0; }\n', 'text/x-oeb1-css')])
    out = eb.write_epub(info.book_dir / "css-mime-oeb1.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
