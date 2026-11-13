# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-item-resource-properties/property-switch-missing/property-switch-missing.epub: An epub:switch without the switch property.

The EPUB 3 template's files, changed by scripts/lib/xhtmlextvariants.py `switch_property_missing()`.

Run: python3 scripts/epub-3.3/package/sec-item-resource-properties/property-switch-missing/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import xhtmlextvariants as xv  # noqa: E402

SET = "epub-3.3/package/sec-item-resource-properties/property-switch-missing"


def main() -> None:
    info = eb.load_set(
        SET, title='An epub:switch without the switch property',
        description='content.xhtml has an epub:switch, and its manifest item has no switch property. Does a validator reject it?',
        subject="EPUB 3.3 content documents")
    out = eb.write_epub(info.book_dir / "property-switch-missing.epub", xv.switch_property_missing(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
