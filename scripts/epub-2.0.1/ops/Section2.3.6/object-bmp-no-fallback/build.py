# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ops/Section2.3.6/object-bmp-no-fallback/object-bmp-no-fallback.epub: An object of a BMP with no fallback.

The EPUB 2 template's files with the change for this set, made with
scripts/lib/opsvariants.py.

Run: python3 scripts/epub-2.0.1/ops/Section2.3.6/object-bmp-no-fallback/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402,F401
import epubbook as eb  # noqa: E402
import opsvariants as ov  # noqa: E402

SET = "epub-2.0.1/ops/Section2.3.6/object-bmp-no-fallback"


def main() -> None:
    info = eb.load_set(
        SET, title='An object of a BMP with no fallback',
        description='content.xhtml has an empty object whose data is a BMP image, with no nested fallback and no text. Does a validator reject it?',
        subject="EPUB 2.0.1 content documents")
    files = epub2.package(info, content=ov.doc(epub2, '    <div><object data="image.bmp" type="image/bmp"></object></div>'), extra=[ov.BMP])
    out = eb.write_epub(info.book_dir / "object-bmp-no-fallback.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
