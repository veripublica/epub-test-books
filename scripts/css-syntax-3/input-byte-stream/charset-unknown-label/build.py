# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/css-syntax-3/input-byte-stream/charset-unknown-label/charset-unknown-label.epub: A stylesheet that declares an unknown label, @charset "x-unknown"; (valid).

The EPUB 3 template with one linked stylesheet, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/css-syntax-3/input-byte-stream/charset-unknown-label/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "css-syntax-3/input-byte-stream/charset-unknown-label"
BODY = 'p { margin: 0; }\n.x::before { content: "\u00e9"; }\n'
ASCII = 'p { margin: 0; }\n'


def u8(text: str) -> bytes:
    return text.encode("utf-8")


def main() -> None:
    info = eb.load_set(
        SET, title='A stylesheet that declares an unknown label, @charset "x-unknown"; (valid)',
        description='style.css starts with @charset "x-unknown";, then p { margin: 0; }, all ASCII. Which encoding does a CSS parser decode it with, and does a validator accept the book?',
        subject="CSS Syntax Level 3")
    content = rv.head_link(epub3.xhtml("Content", pv.section('    <p class="x">Content.</p>')), "style.css")
    css = u8('@charset "x-unknown";\n' + ASCII)
    files = epub3.package(info, content=content, extra=[("style", "style.css", "text/css", "", css)])
    out = eb.write_epub(info.book_dir / "charset-unknown-label.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
