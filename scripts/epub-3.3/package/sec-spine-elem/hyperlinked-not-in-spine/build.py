# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-spine-elem/hyperlinked-not-in-spine/hyperlinked-not-in-spine.epub: A linked document not in the spine.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/packagevariants.py.

Run: python3 scripts/epub-3.3/package/sec-spine-elem/hyperlinked-not-in-spine/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402

SET = "epub-3.3/package/sec-spine-elem/hyperlinked-not-in-spine"


def main() -> None:
    info = eb.load_set(
        SET, title='A linked document not in the spine',
        description='The content document links to another XHTML document that is in the manifest but not in the spine. Does a validator reject it?',
        subject="EPUB 3.3 package document")
    files = epub3.package(info, content=epub3.xhtml("Content", pv.section("    <p><a href=\"extra.xhtml\">Extra</a></p>")), extra=[("extra", "extra.xhtml", "application/xhtml+xml", "", epub3.xhtml("Extra", pv.section("    <p>An extra document.</p>", "Extra", "extra")))])
    out = eb.write_epub(info.book_dir / "hyperlinked-not-in-spine.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
