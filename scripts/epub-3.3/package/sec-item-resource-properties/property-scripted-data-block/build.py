# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-item-resource-properties/property-scripted-data-block/property-scripted-data-block.epub: The scripted property on a document whose only script is a data block.

The EPUB 3 template's files with the changes for this set, made with
scripts/lib/packagevariants.py and scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/package/sec-item-resource-properties/property-scripted-data-block/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/package/sec-item-resource-properties/property-scripted-data-block"


def main() -> None:
    info = eb.load_set(
        SET, title='The scripted property on a document whose only script is a data block',
        description='content.xhtml'"'"'s only script is <script type="application/json">{"a": 1}</script>, and its manifest item has properties="scripted". Does a validator reject it?',
        subject="EPUB 3.3 package document")
    content = epub3.xhtml("Content", pv.section('    <script type="application/json">{"a": 1}</script>'))
    files = rv.content_properties(epub3.package(info, content=content), "scripted")
    out = eb.write_epub(info.book_dir / "property-scripted-data-block.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
