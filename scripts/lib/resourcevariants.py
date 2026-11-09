# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Pieces the publication resource sets share.

Extra manifest items in the form the template's `package()` takes, and small
changes to package.opf. Every change asserts that it found what it expected.
"""

from __future__ import annotations

import base64

import minijpeg
import minimedia
import packagevariants as pv

Files = pv.Files

JPG = ("image", "image.jpg", "image/jpeg", "", minijpeg.gray_jpeg())
BMP = ("foreign", "image.bmp", "image/bmp", "", minimedia.gray_bmp())
XBM = ("foreign2", "image.xbm", "image/x-xbitmap", "", minimedia.gray_xbm())
WAV = ("sound", "sound.wav", "audio/wav", "", minimedia.silent_wav())
REMOTE = "https://example.org/epub-test-books/"


def img(src: str) -> str:
    return f'    <p><img src="{src}" alt="A small gray square."/></p>'


def extra_doc(epub3) -> tuple:
    body = pv.section("    <p>An extra document.</p>", "Extra", "extra")
    return ("extra", "extra.xhtml", "application/xhtml+xml", "", epub3.xhtml("Extra", body))


def data_url(media_type: str, data: bytes) -> str:
    return f"data:{media_type};base64,{base64.b64encode(data).decode()}"


def gray_jpeg_url() -> str:
    return data_url("image/jpeg", minijpeg.gray_jpeg())


def gray_bmp_url() -> str:
    return data_url("image/bmp", minimedia.gray_bmp())


def add_item(files: Files, line: str) -> Files:
    return pv._add_item(files, line)


def add_itemref(files: Files, line: str) -> Files:
    return pv._add_itemref(files, line)


def add_metadata(files: Files, line: str) -> Files:
    return pv._add_metadata(files, line)


def set_fallback(files: Files, item: str, target: str) -> Files:
    return pv._replace(files, f'id="{item}" href=', f'id="{item}" fallback="{target}" href=')


def content_properties(files: Files, value: str) -> Files:
    return pv._replace(files, 'href="content.xhtml" media-type="application/xhtml+xml"/>',
                       f'href="content.xhtml" media-type="application/xhtml+xml" properties="{value}"/>')


def book_has_audio(files: Files) -> Files:
    """Make the accessibility metadata true of a book with audio."""
    files = pv._replace(files, '<meta property="schema:accessMode">textual</meta>',
                        '<meta property="schema:accessMode">textual</meta>\n'
                        '    <meta property="schema:accessMode">auditory</meta>')
    return pv._replace(files, "It has no images, audio, video or other non-text content, and no known hazards.",
                       "It has a very short silent audio clip, no images or video, and no known hazards.")


def head_link(html: str, href: str) -> str:
    assert html.count("  </head>") == 1
    return html.replace("  </head>", f'    <link rel="stylesheet" href="{href}"/>\n  </head>')


def encoded(html: str, encoding: str, name: str) -> bytes:
    """The document in another encoding, with its declarations changed to say so."""
    assert html.count('encoding="UTF-8"') == 1 and html.count('    <meta charset="UTF-8"/>\n') == 1
    html = html.replace('encoding="UTF-8"', f'encoding="{name}"').replace('    <meta charset="UTF-8"/>\n', "")
    return html.encode(encoding)


def package_utf16(files: Files) -> Files:
    """package.opf in UTF-16 with a byte order mark, its XML declaration saying so."""
    out = []
    for name, data in files:
        if name == pv.OPF:
            assert data.count('encoding="UTF-8"') == 1
            data = data.replace('encoding="UTF-8"', 'encoding="UTF-16"').encode("utf-16")
        out.append((name, data))
    return out


def swap(text: str, old: str, new: str) -> str:
    assert text.count(old) == 1, f"expected exactly one {old!r}"
    return text.replace(old, new)


def head_add(html: str, element: str) -> str:
    return swap(html, "  </head>", f"    {element}\n  </head>")


def inline_svg(inner: str) -> str:
    return ('    <p><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 40 40" '
            f'role="img" aria-label="A small gray square.">{inner}</svg></p>')


def standalone_svg(inner: str) -> tuple:
    """An SVG content document, as an extra manifest item."""
    data = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 40 40">'
            f'<title>A small picture</title>{inner}</svg>\n')
    return ("picture", "picture.svg", "image/svg+xml", "", data)


def doctype(html: str, new: str) -> str:
    assert html.count("<!DOCTYPE html>") == 1
    return html.replace("<!DOCTYPE html>", new)
