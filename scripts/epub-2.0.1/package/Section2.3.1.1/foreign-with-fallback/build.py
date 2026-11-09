# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/package/Section2.3.1.1/foreign-with-fallback/foreign-with-fallback.epub: A foreign item with a fallback (valid).

The EPUB 2 template's files with one change for this set, made with
scripts/lib/epub2variants.py.

Run: python3 scripts/epub-2.0.1/package/Section2.3.1.1/foreign-with-fallback/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402
import epubbook as eb  # noqa: E402

SET = "epub-2.0.1/package/Section2.3.1.1/foreign-with-fallback"


def main() -> None:
    info = eb.load_set(
        SET, title='A foreign item with a fallback (valid)',
        description='A plain text file in the manifest has a fallback to an XHTML document. Does a validator accept it?',
        subject="EPUB 2.0.1 package")
    files = e2.fallback(epub2.package(info, extra=[("extra", "extra.txt", "text/plain", "A plain text file.\n")]), "extra", "content")
    out = eb.write_epub(info.book_dir / "foreign-with-fallback.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
