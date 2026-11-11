# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/layout/spread-overrides/spread-override-portrait/spread-override-portrait.epub: The deprecated rendition:spread-portrait override.

The EPUB 3 template's files with the change for this set, made with
scripts/lib/layoutvariants.py.

Run: python3 scripts/epub-3.3/layout/spread-overrides/spread-override-portrait/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import layoutvariants as lv  # noqa: E402

SET = "epub-3.3/layout/spread-overrides/spread-override-portrait"


def main() -> None:
    info = eb.load_set(
        SET, title='The deprecated rendition:spread-portrait override',
        description="The content document's itemref has rendition:spread-portrait, a deprecated override. What does a validator report?",
        subject="EPUB 3.3 fixed layouts")
    files = lv.itemref_properties(lv.fixed(epub3, info), 'content', 'rendition:spread-portrait')
    out = eb.write_epub(info.book_dir / "spread-override-portrait.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
