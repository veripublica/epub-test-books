# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Pieces the fixed-layout sets share (EPUB 3.3 section 8.2 and appendix F).

The fixed-layout form of the EPUB 3 template is the template with
`rendition:layout` set to `pre-paginated` and a viewport meta tag of
`width=1200, height=600` in each spine document. It raises no finding; the
set `layout/layout/fxl-minimal` shows it. Every change asserts that it found
what it expected.
"""

from __future__ import annotations

import packagevariants as pv
import resourcevariants as rv

Files = pv.Files

VIEWPORT = "width=1200, height=600"


def viewport_tag(content: str = VIEWPORT, name: str = "viewport") -> str:
    return f'<meta name="{name}" content="{content}"/>'


def content_doc(epub3, viewport: str | None = VIEWPORT, head: list[str] = ()) -> str:
    """content.xhtml with a viewport tag (none if `viewport` is None), then
    any further head elements."""
    html = epub3.xhtml("Content", pv.section("    <p>Content.</p>"))
    if viewport is not None:
        html = rv.head_add(html, viewport_tag(viewport))
    for element in head:
        html = rv.head_add(html, element)
    return html


def _edit_file(files: Files, name: str, change) -> Files:
    out = []
    for n, data in files:
        if n == name:
            new = change(data)
            assert new != data, "the change did nothing"
            data = new
        out.append((n, data))
    return out


def about_viewport(files: Files) -> Files:
    return _edit_file(files, "OEBPS/about.xhtml",
                      lambda d: rv.head_add(d, viewport_tag()))


def add_meta(files: Files, prop: str, value: str, attrs: str = "") -> Files:
    return rv.add_metadata(files, f'<meta property="{prop}"{attrs}>{value}</meta>')


def fixed(epub3, info, *, content: str | None = None, about: bool = True,
          layout: str | None = "pre-paginated", extra=()) -> Files:
    """The fixed-layout form of the template. `layout=None` leaves out the
    global rendition:layout; `about=False` leaves about.xhtml without a
    viewport."""
    files = epub3.package(info, content=content if content is not None else content_doc(epub3),
                          extra=list(extra))
    if about:
        files = about_viewport(files)
    if layout is not None:
        files = add_meta(files, "rendition:layout", layout)
    return files


def itemref_properties(files: Files, idref: str, props: str) -> Files:
    return pv._replace(files, f'<itemref idref="{idref}"/>',
                       f'<itemref idref="{idref}" properties="{props}"/>')


def svg_page(view_box: bool) -> tuple:
    """A fixed-layout SVG content document, as an extra manifest item."""
    size = 'viewBox="0 0 400 400"' if view_box else 'width="400" height="400"'
    data = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" {size}>'
            '<title>A small picture</title>'
            '<rect width="400" height="400" fill="gray"/></svg>\n')
    return ("picture", "picture.svg", "image/svg+xml", "", data)


def add_itemref_picture(files: Files) -> Files:
    """Put the SVG page from `svg_page()` at the end of the spine."""
    return rv.add_itemref(files, '<itemref idref="picture"/>')
