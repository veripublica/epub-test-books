# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Pieces the OPS 2.0.1 content document sets share.

A set's content.xhtml is the EPUB 2 template's, with its own body and head
elements, and any extra manifest items in the form the template's
`package()` takes. Every change asserts that it found what it expected.
"""

from __future__ import annotations

import minijpeg
import minimedia

Files = list[tuple[str, str | bytes]]

DOCTYPE = ('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" '
           '"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">')
LINK = '<link rel="stylesheet" type="text/css" href="style.css"/>'
SVG_NS = 'xmlns="http://www.w3.org/2000/svg"'

JPG = ("image", "image.jpg", "image/jpeg", minijpeg.gray_jpeg())
BMP = ("bmp", "image.bmp", "image/bmp", minimedia.gray_bmp())


def css(data: str | bytes, media_type: str = "text/css") -> tuple:
    return ("css", "style.css", media_type, data)


def doc(epub2, inner: str, head: list[str] = ()) -> str:
    """content.xhtml with `inner` in its div, and `head` elements added."""
    html = epub2.xhtml("Content", '    <div id="content">\n    <h1>Content</h1>\n'
                                  f"{inner}\n    </div>")
    for element in head:
        html = swap(html, "  </head>", f"    {element}\n  </head>")
    return html


def swap(text: str, old: str, new: str) -> str:
    assert text.count(old) == 1, f"expected exactly one {old!r}"
    return text.replace(old, new)


def edit(files: Files, name: str, change) -> Files:
    out = []
    for n, data in files:
        if n == name:
            new = change(data)
            assert new != data, "the change did nothing"
            data = new
        out.append((n, data))
    return out


def content(files: Files, change) -> Files:
    return edit(files, "OEBPS/content.xhtml", change)


def encoded(html: str, encoding: str, charset: str) -> bytes:
    """The document re-declared and encoded in another encoding."""
    html = swap(html, 'encoding="UTF-8"', f'encoding="{encoding}"')
    html = swap(html, "charset=utf-8", f"charset={charset}")
    return html.encode(encoding.lower())
