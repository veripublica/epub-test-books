# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ocf/Section4/mimetype-wrong-value/mimetype-wrong-value.epub: A mimetype file that holds application/epub.

The EPUB 2 template's files are built for this set, then written as a
container by scripts/lib/ocf2variants.py.

Run: python3 scripts/epub-2.0.1/ocf/Section4/mimetype-wrong-value/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epubbook as eb  # noqa: E402
import ocf2variants as ov2  # noqa: E402

SET = "epub-2.0.1/ocf/Section4/mimetype-wrong-value"


def main() -> None:
    info = eb.load_set(
        SET, title='A mimetype file that holds application/epub',
        description='The mimetype file holds application/epub. Does a validator reject the book?',
        subject="EPUB 2.0.1 OCF")
    files = epub2.package(info)
    out = info.book_dir / "mimetype-wrong-value.epub"
    out.write_bytes(ov2.mimetype_wrong_value(files))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
