# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-item-resource-properties/property-scripted-no-script/property-scripted-no-script.epub: The scripted property on a document with no scripting.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/package/sec-item-resource-properties/property-scripted-no-script/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/package/sec-item-resource-properties/property-scripted-no-script"


def main() -> None:
    info = eb.load_set(
        SET, title='The scripted property on a document with no scripting',
        description='The manifest item of content.xhtml has properties="scripted", but the document has no scripting and no form. Does a validator reject it?',
        subject="EPUB 3.3 package document")
    files = rv.content_properties(epub3.package(info), "scripted")
    out = eb.write_epub(info.book_dir / "property-scripted-no-script.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
