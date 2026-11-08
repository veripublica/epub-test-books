# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""The OCF sets: each function takes the EPUB 3 template's files (from
templates/epub3-minimal/build.py `package()`) and returns the finished
container as bytes, written with rawzip so every header field is under
control. Each set's build.py calls one of them.
"""

from __future__ import annotations

import struct
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "templates" / "epub3-minimal"))
import build as t3  # noqa: E402
import rawzip as rz  # noqa: E402
from rawzip import E  # noqa: E402

OPF, CONT = "OEBPS/package.opf", "META-INF/container.xml"
CONTENT, NAV = "OEBPS/content.xhtml", "OEBPS/nav.xhtml"


def _entries(files, changes=None, add=(), drop=()):
    out = []
    for n, d in files:
        if n in drop:
            continue
        if changes and n in changes:
            d = changes[n]
        out.append((n, d))
    return rz.entries_from(out + list(add))


def _get(files, name):
    return dict(files)[name]


def _manifest_add(files, xml):
    return _get(files, OPF).replace("  </manifest>", f"    {xml}\n  </manifest>")


def _mimetype(files, data=b"application/epub+zip", **kw):
    es = _entries(files)
    es[0] = E("mimetype", data, method=0, **kw)
    return rz.build(es)


def _rename_content(files, new, href):
    es = _entries(files, changes={
        OPF: _get(files, OPF).replace('href="content.xhtml"', f'href="{href}"'),
        NAV: _get(files, NAV).replace('href="content.xhtml"', f'href="{href}"')})
    for e in es:
        if e.name == CONTENT:
            e.name = "OEBPS/" + new
    return es


# --- sec-zip-container-mime ---------------------------------------------------

def mimetype_wrong_value(files):
    return _mimetype(files, b"application/zip")


def mimetype_trailing_newline(files):
    return _mimetype(files, b"application/epub+zip\n")


def mimetype_leading_space(files):
    return _mimetype(files, b" application/epub+zip")


def mimetype_bom(files):
    return _mimetype(files, b"\xef\xbb\xbfapplication/epub+zip")


def mimetype_extra_field(files):
    # an extended-timestamp extra field (0x5455, 5 bytes), as Info-ZIP writes
    return _mimetype(files, extra=struct.pack("<HHBI", 0x5455, 5, 1, 0))


def mimetype_not_first(files):
    es = _entries(files)
    es[0], es[1] = es[1], es[0]
    return rz.build(es)


def mimetype_missing(files):
    return rz.build(_entries(files)[1:])


# --- sec-zip-container-zipreqs ------------------------------------------------

def compression_bzip2(files):
    es = _entries(files)
    for e in es:
        if e.name == CONTENT:
            e.method, e.version = 12, 46
    return rz.build(es)


def filename_not_utf8(files):
    # OEBPS/content.xhtml becomes "c\x81ntent.xhtml": 0x81 is u-umlaut in
    # CP437, the ZIP default; the UTF-8 flag (bit 11) is clear.
    es = _rename_content(files, "cüntent.xhtml", "c%C3%BCntent.xhtml")
    for e in es:
        if e.name == "OEBPS/cüntent.xhtml":
            e.name, e.flags = b"OEBPS/c\x81ntent.xhtml", 0
    return rz.build(es)


# --- sec-container-file-and-dir-structure ------------------------------------

def container_in_manifest(files):
    return rz.build(_entries(files, changes={OPF: _manifest_add(
        files, '<item id="container" href="../META-INF/container.xml" '
               'media-type="application/xml"/>')}))


# --- sec-container-filenames -------------------------------------------------

def filename_forbidden_char(files):
    return rz.build(_rename_content(files, "con|tent.xhtml", "con%7Ctent.xhtml"))


def filename_space(files):
    return rz.build(_rename_content(files, "con tent.xhtml", "con%20tent.xhtml"))


def filename_case_duplicate(files):
    opf = _manifest_add(files, '<item id="second" href="Content.xhtml" '
                               'media-type="application/xhtml+xml"/>')
    opf = opf.replace('<itemref idref="content"/>',
                      '<itemref idref="content"/>\n    <itemref idref="second"/>')
    second = t3.content_doc().replace("<h1>Content</h1>", "<h1>Second</h1>")
    return rz.build(_entries(files, changes={OPF: opf},
                             add=[("OEBPS/Content.xhtml", second)]))


def filename_nfc_nfd_duplicate(files):
    nfc, nfd = "é.xhtml", "é.xhtml"
    opf = _manifest_add(
        files, '<item id="nfc" href="%C3%A9.xhtml" media-type="application/xhtml+xml"/>\n'
               '    <item id="nfd" href="e%CC%81.xhtml" media-type="application/xhtml+xml"/>')
    opf = opf.replace('<itemref idref="content"/>', '<itemref idref="content"/>\n'
                      '    <itemref idref="nfc"/>\n    <itemref idref="nfd"/>')
    doc = t3.content_doc()
    return rz.build(_entries(files, changes={OPF: opf}, add=[
        ("OEBPS/" + nfc, doc.replace("<h1>Content</h1>", "<h1>Composed</h1>")),
        ("OEBPS/" + nfd, doc.replace("<h1>Content</h1>", "<h1>Decomposed</h1>"))]))


# --- container.xml -------------------------------------------------------------

def container_missing(files):
    return rz.build(_entries(files, drop=[CONT]))


def rootfile_wrong_media_type(files):
    c = _get(files, CONT).replace('media-type="application/oebps-package+xml"',
                                  'media-type="application/xml"')
    return rz.build(_entries(files, changes={CONT: c}))


def rootfile_missing_target(files):
    c = _get(files, CONT).replace("OEBPS/package.opf", "OEBPS/missing.opf")
    return rz.build(_entries(files, changes={CONT: c}))


def no_rootfile(files):
    c = _get(files, CONT)
    start = c.find("    <rootfile ")
    end = c.find("/>", start) + 3
    return rz.build(_entries(files, changes={CONT: c[:start] + c[end:]}))


# --- sec-container-iri -------------------------------------------------------

def url_to_missing_file(files):
    d = _get(files, CONTENT).replace(
        "holds only this paragraph.",
        'holds only this paragraph. <a href="missing.xhtml">A link</a>')
    return rz.build(_entries(files, changes={CONTENT: d}))
