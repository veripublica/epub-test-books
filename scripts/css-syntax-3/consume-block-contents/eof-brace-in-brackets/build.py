# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/css-syntax-3/consume-block-contents/eof-brace-in-brackets/eof-brace-in-brackets.epub: A block open at EOF whose last } is inside [, p { margin: 0; [} (valid).

The EPUB 3 template with one linked stylesheet, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/css-syntax-3/consume-block-contents/eof-brace-in-brackets/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "css-syntax-3/consume-block-contents/eof-brace-in-brackets"
CSS = 'p { margin: 0; [}'


def main() -> None:
    info = eb.load_set(
        SET, title='A block open at EOF whose last } is inside [, p { margin: 0; [} (valid)',
        description='style.css holds p { margin: 0; [} and nothing after it: the last byte of the file is the }. Does a validator accept the book?',
        subject='CSS Syntax Level 3')
    content = rv.head_link(epub3.xhtml("Content", pv.section('    <p class="x">Content.</p>')), "style.css")
    extra = [("style", "style.css", "text/css", "", CSS.encode("utf-8"))]
    files = epub3.package(info, content=content, extra=extra)
    out = eb.write_epub(info.book_dir / "eof-brace-in-brackets.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
