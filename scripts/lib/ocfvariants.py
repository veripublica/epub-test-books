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


def zip64_unneeded(files):
    # the content document carries ZIP64 sizes (a 0x0001 extra field in both
    # headers, the 32-bit size fields set to 0xFFFFFFFF, version needed 45),
    # though it is far below 4 GiB
    es = _entries(files)
    for e in es:
        if e.name == CONTENT:
            e.zip64 = True
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

def link_into_meta_inf(files):
    d = _get(files, CONTENT).replace(
        "holds only this paragraph.",
        'holds only this paragraph. <a href="../META-INF/container.xml">A link</a>')
    return rz.build(_entries(files, changes={CONTENT: d}))


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

EXT = 'xmlns:ext="https://example.org/epub-test-books/ns"'


def container_foreign_element(files):
    # an extension element after rootfiles; removing it leaves the template
    c = _get(files, CONT).replace(
        "  </rootfiles>\n",
        f"  </rootfiles>\n  <ext:note {EXT}>An element from another namespace.</ext:note>\n")
    return rz.build(_entries(files, changes={CONT: c}))


def container_foreign_attribute(files):
    # an extension attribute on rootfiles; removing it leaves the template
    c = _get(files, CONT).replace("<rootfiles>", f'<rootfiles {EXT} ext:note="An attribute from another namespace.">')
    return rz.build(_entries(files, changes={CONT: c}))


def container_missing(files):
    return rz.build(_entries(files, drop=[CONT]))


def container_version_wrong(files):
    # only the container element's attribute: the XML declaration keeps 1.0
    c = _get(files, CONT).replace('<container version="1.0"', '<container version="2.0"')
    return rz.build(_entries(files, changes={CONT: c}))


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


# --- encryption.xml and font obfuscation ------------------------------------
# These books add a stylesheet that uses a font, so the font is referenced.
# The font is scripts/lib/minifont.py's two-glyph TrueType font (928 bytes,
# so obfuscation changes the whole file: EPUB 3.3 §4.4.4 covers fonts
# shorter than 1040 bytes).

import minifont as mf  # noqa: E402

FONT_HREF = "fonts/box.ttf"
CSS = ('@font-face {\n  font-family: "Box";\n  src: url(fonts/box.ttf);\n}\n\n'
       'body {\n  font-family: "Box", serif;\n}\n')


def _encryption_xml(uri, root="encryption"):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<{root} xmlns="urn:oasis:names:tc:opendocument:xmlns:container"'
            f' xmlns:enc="http://www.w3.org/2001/04/xmlenc#">\n'
            f'  <enc:EncryptedData>\n'
            f'    <enc:EncryptionMethod Algorithm="http://www.idpf.org/2008/embedding"/>\n'
            f'    <enc:CipherData>\n'
            f'      <enc:CipherReference URI="{uri}"/>\n'
            f'    </enc:CipherData>\n'
            f'  </enc:EncryptedData>\n'
            f'</{root}>\n')


def _font_book(info, *, font, css=CSS, encryption=None):
    content = t3.content_doc().replace(
        "    <title>Content</title>\n",
        '    <title>Content</title>\n'
        '    <link rel="stylesheet" type="text/css" href="style.css"/>\n')
    files = t3.package(info, content=content, extra=[
        ("style", "style.css", "text/css", "", css),
        ("font", FONT_HREF, "font/ttf", "", font)])
    if encryption is not None:
        files.insert(1, ("META-INF/encryption.xml", encryption))
    return rz.build(rz.entries_from(files))


def font_obfuscated(info):
    return _font_book(info, font=mf.obfuscate(mf.font(), info.identifier),
                      encryption=_encryption_xml("OEBPS/" + FONT_HREF))


def obfuscated_not_font(info):
    return _font_book(info, font=mf.font(),
                      css=mf.obfuscate(CSS.encode(), info.identifier),
                      encryption=_encryption_xml("OEBPS/style.css"))


def encryption_wrong_root(info):
    return _font_book(info, font=mf.obfuscate(mf.font(), info.identifier),
                      encryption=_encryption_xml("OEBPS/" + FONT_HREF, root="encryptions"))


def zip_encryption(files):
    # traditional PKWARE encryption on the content document (general purpose
    # flag bit 0); the password is "epub-test-books"
    es = _entries(files)
    for e in es:
        if e.name == CONTENT:
            e.password = b"epub-test-books"
    return rz.build(es)


def never_encrypted(files, target):
    # META-INF/encryption.xml declares `target` encrypted with AES-128-CBC.
    # Only the declaration is the defect: the file's bytes stay as they are,
    # since real encryption would also make the file unreadable.
    xml = _encryption_xml(target).replace(
        "http://www.idpf.org/2008/embedding", "http://www.w3.org/2001/04/xmlenc#aes128-cbc")
    files = list(files)
    files.insert(1, ("META-INF/encryption.xml", xml))
    return rz.build(rz.entries_from(files))


def package_document_obfuscated(info, files):
    # The package document really obfuscated with the font algorithm (its
    # first 1040 bytes XORed with the key from the unique identifier), and
    # listed in META-INF/encryption.xml.
    opf = "OEBPS/package.opf"
    out = [(n, mf.obfuscate(d.encode("utf-8") if isinstance(d, str) else d, info.identifier) if n == opf else d)
           for n, d in files]
    out.insert(1, ("META-INF/encryption.xml", _encryption_xml(opf)))
    return rz.build(rz.entries_from(out))


# --- AES-encrypted resources (sec-container-metainf-encryption.xml, sec-enc-compression)
# The content document is really encrypted with AES-128-CBC (scripts/lib/miniaes.py),
# and META-INF/encryption.xml describes it as in EPUB 3.3's example 7: an
# EncryptedKey (an RSA-wrapped key, named "epub-test-books") and an EncryptedData
# that refers to it. The key and IV are fixed, so the books are reproducible; the
# wrapped key is 128 fixed bytes, since nothing in a validator can unwrap it.

import base64  # noqa: E402
import hashlib  # noqa: E402
import zlib  # noqa: E402

import miniaes  # noqa: E402

AES_KEY = hashlib.sha1(b"epub-test-books key").digest()[:16]
AES_IV = hashlib.sha1(b"epub-test-books iv").digest()[:16]
AES128 = "http://www.w3.org/2001/04/xmlenc#aes128-cbc"
_WRAPPED = base64.b64encode(hashlib.sha512(b"wrapped key").digest() * 2).decode()


def _aes_xml(target, alg=AES128, props=""):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<encryption xmlns="urn:oasis:names:tc:opendocument:xmlns:container"'
            ' xmlns:enc="http://www.w3.org/2001/04/xmlenc#" xmlns:ds="http://www.w3.org/2000/09/xmldsig#">\n'
            '  <enc:EncryptedKey Id="EK">\n'
            '    <enc:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#rsa-1_5"/>\n'
            '    <ds:KeyInfo><ds:KeyName>epub-test-books</ds:KeyName></ds:KeyInfo>\n'
            f'    <enc:CipherData><enc:CipherValue>{_WRAPPED}</enc:CipherValue></enc:CipherData>\n'
            '  </enc:EncryptedKey>\n'
            '  <enc:EncryptedData Id="ED1">\n'
            f'    <enc:EncryptionMethod Algorithm="{alg}"/>\n'
            '    <ds:KeyInfo><ds:RetrievalMethod URI="#EK" Type="http://www.w3.org/2001/04/xmlenc#EncryptedKey"/></ds:KeyInfo>\n'
            f'    <enc:CipherData><enc:CipherReference URI="{target}"/></enc:CipherData>\n'
            f'{props}'
            '  </enc:EncryptedData>\n'
            '</encryption>\n')


def _compression(method, length):
    return ('    <enc:EncryptionProperties>\n'
            '      <enc:EncryptionProperty xmlns:c="http://www.idpf.org/2016/encryption#compression">\n'
            f'        <c:Compression Method="{method}" OriginalLength="{length}"/>\n'
            '      </enc:EncryptionProperty>\n'
            '    </enc:EncryptionProperties>\n')


def _aes_book(files, *, xml=None, data=None, zip_method=0):
    plain = _get(files, CONTENT)
    plain = plain.encode("utf-8") if isinstance(plain, str) else plain
    es = _entries(files)
    for e in es:
        if e.name == CONTENT:
            e.data = miniaes.encrypt(plain if data is None else data(plain), AES_KEY, AES_IV)
            e.method = zip_method
    if xml is not None:
        es.insert(1, rz.E("META-INF/encryption.xml", xml(plain).encode("utf-8")))
    return rz.build(es)


def _deflate(data):
    c = zlib.compressobj(9, zlib.DEFLATED, -15)
    return c.compress(data) + c.flush()


def aes_encrypted_content(files):
    return _aes_book(files, xml=lambda p: _aes_xml(CONTENT))


def aes_unknown_algorithm(files):
    return _aes_book(files, xml=lambda p: _aes_xml(CONTENT, alg="https://example.org/epub-test-books/no-such-cipher"))


def aes_deflated_in_zip(files):
    return _aes_book(files, xml=lambda p: _aes_xml(CONTENT), zip_method=8)


def aes_no_encryption_xml(files):
    return _aes_book(files)


def aes_compressed_first(files, method=8):
    # Deflate first (raw, no zlib header), then AES; the Compression property
    # gives `method` and the length before compression
    return _aes_book(files, xml=lambda p: _aes_xml(CONTENT, props=_compression(method, len(p))), data=_deflate)
