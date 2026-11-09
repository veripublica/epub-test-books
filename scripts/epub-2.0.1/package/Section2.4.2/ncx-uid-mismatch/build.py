# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/package/Section2.4.2/ncx-uid-mismatch/ncx-uid-mismatch.epub: An NCX dtb:uid that differs from the package.

The EPUB 2 template's files with one change for this set, made with
scripts/lib/epub2variants.py.

Run: python3 scripts/epub-2.0.1/package/Section2.4.2/ncx-uid-mismatch/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402
import epubbook as eb  # noqa: E402

SET = "epub-2.0.1/package/Section2.4.2/ncx-uid-mismatch"


def main() -> None:
    info = eb.load_set(
        SET, title='An NCX dtb:uid that differs from the package',
        description="The NCX dtb:uid differs from the package's unique identifier. Does a validator reject it?",
        subject="EPUB 2.0.1 package")
    files = epub2.package(info); files = e2.ncx_re(files, r'name="dtb:uid" content="[^"]*"', 'name="dtb:uid" content="urn:uuid:00000000-0000-5000-8000-000000000000"')
    out = eb.write_epub(info.book_dir / "ncx-uid-mismatch.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
