# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/package/Section1.4.1.1/package-iso-8859-1/package-iso-8859-1.epub: A package document in ISO-8859-1.

The EPUB 2 template's files with one change for this set, made with
scripts/lib/epub2variants.py.

Run: python3 scripts/epub-2.0.1/package/Section1.4.1.1/package-iso-8859-1/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402
import epubbook as eb  # noqa: E402

SET = "epub-2.0.1/package/Section1.4.1.1/package-iso-8859-1"


def main() -> None:
    info = eb.load_set(
        SET, title='A package document in ISO-8859-1',
        description='The package document is encoded in ISO-8859-1 and says so. Does a validator reject it?',
        subject="EPUB 2.0.1 package")
    files = epub2.package(info); files = [(n, d.replace('encoding="UTF-8"', 'encoding="ISO-8859-1"', 1).encode("latin-1") if n == e2.OPF else d) for n, d in files]
    out = eb.write_epub(info.book_dir / "package-iso-8859-1.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
