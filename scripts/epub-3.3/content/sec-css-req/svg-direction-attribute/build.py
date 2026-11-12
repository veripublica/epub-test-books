# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-css-req/svg-direction-attribute/svg-direction-attribute.epub: The SVG direction presentation attribute (valid).

The EPUB 3 template with the edits below, made with scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/content/sec-css-req/svg-direction-attribute/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/content/sec-css-req/svg-direction-attribute"
BODY = '    <svg xmlns="http://www.w3.org/2000/svg" width="100" height="20" role="img" aria-label="abc"><text x="0" y="15" direction="rtl">abc</text></svg>'
CSS = None
SVG = True
OPF_EDITS = []
XHTML_EDITS = []


def main() -> None:
    info = eb.load_set(
        SET, title='The SVG direction presentation attribute (valid)',
        description='content.xhtml holds an inline svg whose text element has direction="rtl". Does a validator accept the book?',
        subject='EPUB 3.3 content documents')
    content = epub3.xhtml("Content", pv.section(BODY))
    extra = []
    if CSS is not None:
        content = rv.head_link(content, "style.css")
        extra.append(("style", "style.css", "text/css", "", CSS.encode("utf-8")))
    for old, new in XHTML_EDITS:
        content = rv.swap(content, old, new)
    files = []
    for name, data in epub3.package(info, content=content, extra=extra):
        if name == "OEBPS/package.opf":
            for old, new in OPF_EDITS:
                data = rv.swap(data, old, new)
            if SVG:
                data = rv.swap(data, 'href="content.xhtml" media-type="application/xhtml+xml"/>',
                               'href="content.xhtml" media-type="application/xhtml+xml" properties="svg"/>')
        files.append((name, data))
    out = eb.write_epub(info.book_dir / "svg-direction-attribute.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
