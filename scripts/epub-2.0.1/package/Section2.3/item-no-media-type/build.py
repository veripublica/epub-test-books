# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/package/Section2.3/item-no-media-type/item-no-media-type.epub: A manifest item without media-type.

The EPUB 2 template's files with one change for this set, made with
scripts/lib/epub2variants.py.

Run: python3 scripts/epub-2.0.1/package/Section2.3/item-no-media-type/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402
import epubbook as eb  # noqa: E402

SET = "epub-2.0.1/package/Section2.3/item-no-media-type"


def main() -> None:
    info = eb.load_set(
        SET, title='A manifest item without media-type',
        description='One extra manifest item has no media-type. Does a validator reject it?',
        subject="EPUB 2.0.1 package")
    files = epub2.package(info); files = e2.add_item(files + [("OEBPS/extra.xhtml", e2.extra_page(epub2))], '<item id="extra" href="extra.xhtml"/>')
    out = eb.write_epub(info.book_dir / "item-no-media-type.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
