# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/css-syntax-3/input-byte-stream/charset-past-1024/charset-past-1024.epub: A @charset declaration that ends after byte 1024 (valid).

The EPUB 3 template with one linked stylesheet, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/css-syntax-3/input-byte-stream/charset-past-1024/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "css-syntax-3/input-byte-stream/charset-past-1024"
BODY = 'p { margin: 0; }\n.x::before { content: "\u00e9"; }\n'
ASCII = 'p { margin: 0; }\n'


def u8(text: str) -> bytes:
    return text.encode("utf-8")


def main() -> None:
    info = eb.load_set(
        SET, title='A @charset declaration that ends after byte 1024 (valid)',
        description='style.css starts with @charset ", 1,003 spaces, iso-8859-1";, then p { margin: 0; }, all ASCII. Its closing ; is byte 1,025. Which encoding does a CSS parser decode it with, and does a validator accept the book?',
        subject="CSS Syntax Level 3")
    content = rv.head_link(epub3.xhtml("Content", pv.section('    <p class="x">Content.</p>')), "style.css")
    css = u8('@charset "' + ' ' * 1003 + 'iso-8859-1";\n' + ASCII)
    files = epub3.package(info, content=content, extra=[("style", "style.css", "text/css", "", css)])
    out = eb.write_epub(info.book_dir / "charset-past-1024.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
