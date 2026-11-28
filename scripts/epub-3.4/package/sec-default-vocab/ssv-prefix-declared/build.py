# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.4/package/sec-default-vocab/ssv-prefix-declared/ssv-prefix-declared.epub: A prefix for the structural semantics vocabulary's own URL (invalid).

The EPUB 3 template, with the change for this set, following EPUB 3.4.

Run: python3 scripts/epub-3.4/package/sec-default-vocab/ssv-prefix-declared/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import encodedmedia as em  # noqa: E402,F401
import epubbook as eb  # noqa: E402
import layoutvariants as lv  # noqa: E402,F401
import minifont as mf  # noqa: E402,F401
import navvariants as nv  # noqa: E402,F401
import packagevariants as pv  # noqa: E402,F401
import resourcevariants as rv  # noqa: E402,F401

SET = "epub-3.4/package/sec-default-vocab/ssv-prefix-declared"


def main() -> None:
    info = eb.load_set(
        SET, title="A prefix for the structural semantics vocabulary's own URL (invalid)",
        description='content.xhtml declares epub:prefix="s: http://idpf.org/epub/vocab/structure/#" and uses s:chapter. Does a validator reject the book?',
        subject="EPUB 3.4 package document")
    content = epub3.xhtml("Content", pv.section('    <p epub:type="s:chapter">Content.</p>'))
    content = rv.swap(content, ' xml:lang="en"', ' epub:prefix="s: http://idpf.org/epub/vocab/structure/#" xml:lang="en"')
    files = epub3.package(info, content=content)
    out = eb.write_epub(info.book_dir / "ssv-prefix-declared.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
