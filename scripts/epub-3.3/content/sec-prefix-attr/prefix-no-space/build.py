# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-prefix-attr/prefix-no-space/prefix-no-space.epub: An epub:prefix mapping with no space after the colon.

The EPUB 3 template's files, changed by scripts/lib/xhtmlextvariants.py `prefix_no_space()`.

Run: python3 scripts/epub-3.3/content/sec-prefix-attr/prefix-no-space/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import xhtmlextvariants as xv  # noqa: E402

SET = "epub-3.3/content/sec-prefix-attr/prefix-no-space"


def main() -> None:
    info = eb.load_set(
        SET, title='An epub:prefix mapping with no space after the colon',
        description='content.xhtml declares epub:prefix="foo:https://…", with no space after the colon. Does a validator reject it?',
        subject="EPUB 3.3 content documents")
    out = eb.write_epub(info.book_dir / "prefix-no-space.epub", xv.prefix_no_space(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
