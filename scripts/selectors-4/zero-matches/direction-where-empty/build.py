# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/selectors-4/zero-matches/direction-where-empty/direction-where-empty.epub: direction: rtl in a rule whose :where() is left empty, :where(:foo).

The EPUB 3 template with one linked stylesheet, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/selectors-4/zero-matches/direction-where-empty/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "selectors-4/zero-matches/direction-where-empty"
CSS = ':where(:foo) { direction: rtl; }\n'


def main() -> None:
    info = eb.load_set(
        SET, title='direction: rtl in a rule whose :where() is left empty, :where(:foo)',
        description='style.css holds :where(:foo) { direction: rtl; }. Does a validator reject the book?',
        subject='Selectors Level 4')
    content = rv.head_link(epub3.xhtml("Content", pv.section('    <p class="x">Content.</p>')), "style.css")
    files = epub3.package(info, content=content, extra=[("style", "style.css", "text/css", "", CSS.encode("utf-8"))])
    out = eb.write_epub(info.book_dir / "direction-where-empty.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
