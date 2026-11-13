# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-xhtml-rdfa/rdfa-prefix-no-colon/rdfa-prefix-no-colon.epub: An RDFa prefix attribute with no colon.

The EPUB 3 template's files, changed by scripts/lib/xhtmlextvariants.py `rdfa_prefix_no_colon()`.

Run: python3 scripts/epub-3.3/content/sec-xhtml-rdfa/rdfa-prefix-no-colon/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import xhtmlextvariants as xv  # noqa: E402

SET = "epub-3.3/content/sec-xhtml-rdfa/rdfa-prefix-no-colon"


def main() -> None:
    info = eb.load_set(
        SET, title='An RDFa prefix attribute with no colon',
        description='content.xhtml has prefix="dc http://purl.org/dc/terms/", with no colon. Does a validator reject it?',
        subject="EPUB 3.3 content documents")
    out = eb.write_epub(info.book_dir / "rdfa-prefix-no-colon.epub", xv.rdfa_prefix_no_colon(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
