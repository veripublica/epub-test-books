# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/package/Section2.2/language-missing/language-missing.epub: No dc:language.

The EPUB 2 template's files with one change for this set, made with
scripts/lib/epub2variants.py.

Run: python3 scripts/epub-2.0.1/package/Section2.2/language-missing/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402
import epubbook as eb  # noqa: E402

SET = "epub-2.0.1/package/Section2.2/language-missing"


def main() -> None:
    info = eb.load_set(
        SET, title='No dc:language',
        description='The metadata has no dc:language. Does a validator reject it?',
        subject="EPUB 2.0.1 package")
    files = epub2.package(info); files = e2.opf(files, "    <dc:language>en</dc:language>\n", "")
    out = eb.write_epub(info.book_dir / "language-missing.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
