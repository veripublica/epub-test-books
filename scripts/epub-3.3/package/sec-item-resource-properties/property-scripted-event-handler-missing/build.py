# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-item-resource-properties/property-scripted-event-handler-missing/property-scripted-event-handler-missing.epub: An event handler attribute without the scripted property.

The EPUB 3 template's files, changed by scripts/lib/scriptvariants.py `scripted_event_handler_missing()`.

Run: python3 scripts/epub-3.3/package/sec-item-resource-properties/property-scripted-event-handler-missing/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import scriptvariants as sv  # noqa: E402

SET = "epub-3.3/package/sec-item-resource-properties/property-scripted-event-handler-missing"


def main() -> None:
    info = eb.load_set(
        SET, title='An event handler attribute without the scripted property',
        description='content.xhtml has an onclick attribute, no script element, and no scripted property. Does a validator reject it?',
        subject="EPUB 3.3 scripting")
    out = eb.write_epub(info.book_dir / "property-scripted-event-handler-missing.epub", sv.scripted_event_handler_missing(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
