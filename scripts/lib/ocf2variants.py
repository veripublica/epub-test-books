# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""The OCF 2.0.1 sets: each function takes the EPUB 2 template's files (from
templates/epub2-minimal/build.py `package()`) and returns the finished
container as bytes, written with rawzip so every header field is under
control. Each set's build.py calls one of them.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "templates" / "epub2-minimal"))
import build as t2  # noqa: E402
import rawzip as rz  # noqa: E402
from rawzip import E  # noqa: E402

OPF, CONT = "OEBPS/package.opf", "META-INF/container.xml"
CONTENT, NCX = "OEBPS/content.xhtml", "OEBPS/toc.ncx"
RF = '    <rootfile full-path="OEBPS/package.opf" media-type="application/oebps-package+xml"/>\n'
EXT = 'xmlns:ext="https://example.org/epub-test-books/ns"'
ITEMREF = '<itemref idref="content"/>'


def _get(files, name):
    return dict(files)[name]


def _swap(text, old, new):
    assert text.count(old) == 1, f"expected exactly one {old!r}"
    return text.replace(old, new)


def _entries(files, changes=None, add=(), drop=(), insert=()):
    out = [(n, (changes or {}).get(n, d)) for n, d in files if n not in drop]
    for i, nd in insert:
        out.insert(i, nd)
    return rz.entries_from(out + list(add))


def _container(files, old, new):
    return rz.build(_entries(files, changes={CONT: _swap(_get(files, CONT), old, new)}))


def _rename_content(files, new, href):
    es = _entries(files, changes={
        OPF: _swap(_get(files, OPF), 'href="content.xhtml"', f'href="{href}"'),
        NCX: _swap(_get(files, NCX), 'src="content.xhtml"', f'src="{href}"')})
    for e in es:
        if e.name == CONTENT:
            e.name = "OEBPS/" + new
    return es


def _second_docs(files, docs):
    """Add content documents (id, href, path, h1) to the manifest and spine."""
    opf = _get(files, OPF)
    items = "".join(f'    <item id="{i}" href="{h}" media-type="application/xhtml+xml"/>\n' for i, h, _, _ in docs)
    refs = "".join(f'\n    <itemref idref="{i}"/>' for i, _, _, _ in docs)
    opf = _swap(_swap(opf, "  </manifest>", items + "  </manifest>"), ITEMREF, ITEMREF + refs)
    add = [(p, t2.content_doc().replace("<h1>Content</h1>", f"<h1>{h1}</h1>")) for _, _, p, h1 in docs]
    return rz.build(_entries(files, changes={OPF: opf}, add=add))


def _set_entry(files, name, **fields):
    es = _entries(files)
    for e in es:
        if e.name == name:
            for k, v in fields.items():
                setattr(e, k, v)
    return rz.build(es)


# --- 3.4 and 4: the mimetype file ---------------------------------------------

def _mimetype(files, data=b"application/epub+zip", **kw):
    es = _entries(files)
    es[0] = E("mimetype", data, method=0, **kw)
    return rz.build(es)


def mimetype_compressed(files):
    # the mimetype entry is Flate-compressed (method 8)
    es = _entries(files)
    es[0].method = 8
    return rz.build(es)


def mimetype_wrong_value(files):
    return _mimetype(files, b"application/epub")


def mimetype_trailing_newline(files):
    return _mimetype(files, b"application/epub+zip\n")


def mimetype_uppercase(files):
    return _mimetype(files, b"APPLICATION/EPUB+ZIP")


def mimetype_extra_field(files):
    # an unknown extra field (header ID 0xCAFE, no data) in the local header (rawzip writes no central extra field)
    return _mimetype(files, extra=b"\xfe\xca\x00\x00")


def mimetype_missing(files):
    return rz.build(_entries(files)[1:])


def mimetype_not_first(files):
    es = _entries(files)
    return rz.build([es[1], es[0]] + es[2:])


# --- 3.5.1 container.xml -------------------------------------------------------

def container_missing(files):
    return rz.build(_entries(files, drop=[CONT]))


def container_no_version(files):
    return _container(files, '<container version="1.0"', "<container")


def container_version_2(files):
    return _container(files, '<container version="1.0"', '<container version="2.0"')


def container_foreign_element(files):
    return _container(files, "  </rootfiles>\n", f"  </rootfiles>\n  <ext:note {EXT}>An element from another namespace.</ext:note>\n")


def container_foreign_attribute(files):
    return _container(files, "<rootfiles>", f'<rootfiles {EXT} ext:note="An attribute from another namespace.">')


def container_unqualified_element(files):
    return _container(files, "  </rootfiles>\n", "  </rootfiles>\n  <foo/>\n")


def container_unqualified_attribute(files):
    return _container(files, "<rootfiles>", '<rootfiles identifier="bar">')


def rootfile_wrong_media_type(files):
    return _container(files, 'media-type="application/oebps-package+xml"', 'media-type="application/xml"')


def rootfile_missing_target(files):
    return _container(files, 'full-path="OEBPS/package.opf"', 'full-path="OEBPS/missing.opf"')


def rootfile_absolute_path(files):
    return _container(files, 'full-path="OEBPS/package.opf"', 'full-path="/OEBPS/package.opf"')


def no_rootfile(files):
    return _container(files, RF, "")


def rootfile_two_opf(files):
    # a second rootfile for a copy of the package document, OEBPS/second.opf
    c = _swap(_get(files, CONT), RF, RF + RF.replace("package.opf", "second.opf"))
    return rz.build(_entries(files, changes={CONT: c}, add=[("OEBPS/second.opf", _get(files, OPF))]))


PDF = (b"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
       b"2 0 obj<</Type/Pages/Kids[]/Count 0>>endobj\ntrailer<</Root 1 0 R>>\n%%EOF\n")
PDF_RF = '    <rootfile full-path="PDF/book.pdf" media-type="application/pdf"/>\n'


def rootfile_pdf_alternate(files):
    c = _swap(_get(files, CONT), RF, RF + PDF_RF)
    return rz.build(_entries(files, changes={CONT: c}, add=[("PDF/book.pdf", PDF)]))


def rootfile_pdf_first(files):
    c = _swap(_get(files, CONT), RF, PDF_RF + RF)
    return rz.build(_entries(files, changes={CONT: c}, add=[("PDF/book.pdf", PDF)]))


# --- 3.5.2-3.5.6: the other META-INF files --------------------------------------

def _meta_inf(files, name, xml):
    return rz.build(_entries(files, add=[(f"META-INF/{name}", xml)]))


def metadata_xml_namespaced(files):
    return _meta_inf(files, "metadata.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<ext:metadata {EXT}><ext:note>Container-level metadata.</ext:note></ext:metadata>\n')


def rights_xml_namespaced(files):
    return _meta_inf(files, "rights.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<ext:rights {EXT}/>\n')


def manifest_xml_odf(files):
    return _meta_inf(files, "manifest.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
                     '<manifest:manifest xmlns:manifest="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0">\n'
                     '  <manifest:file-entry manifest:media-type="application/epub+zip" manifest:full-path="/"/>\n'
                     '</manifest:manifest>\n')


def metadata_xml_unqualified(files):
    return _meta_inf(files, "metadata.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<metadata><note>Container-level metadata.</note></metadata>\n')


def rights_xml_not_well_formed(files):
    # the root element is never closed
    return _meta_inf(files, "rights.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<ext:rights ' + EXT + '>\n')


def manifest_xml_wrong_root(files):
    return _meta_inf(files, "manifest.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<files/>\n')


def signatures_xml_wrong_root(files):
    return _meta_inf(files, "signatures.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
                     '<sigs xmlns="urn:oasis:names:tc:opendocument:xmlns:container"/>\n')


def never_encrypted(files, target):
    # META-INF/encryption.xml declares `target` encrypted with AES-128-CBC.
    # Only the declaration is the defect: the file's bytes stay as they are.
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<encryption xmlns="urn:oasis:names:tc:opendocument:xmlns:container" xmlns:enc="http://www.w3.org/2001/04/xmlenc#">\n'
           '  <enc:EncryptedData>\n'
           '    <enc:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc"/>\n'
           f'    <enc:CipherData><enc:CipherReference URI="{target}"/></enc:CipherData>\n'
           '  </enc:EncryptedData>\n'
           '</encryption>\n')
    return rz.build(_entries(files, insert=[(1, ("META-INF/encryption.xml", xml))]))


# --- 3.3 file names ----------------------------------------------------------

def filename(files, name, href):
    return rz.build(_rename_content(files, name, href))


def filename_case_duplicate(files):
    return _second_docs(files, [("second", "Content.xhtml", "OEBPS/Content.xhtml", "Second")])


def filename_nfc_nfd_duplicate(files):
    return _second_docs(files, [("nfc", "%C3%A9.xhtml", "OEBPS/é.xhtml", "Composed"),
                                ("nfd", "e%CC%81.xhtml", "OEBPS/é.xhtml", "Decomposed")])


def filename_not_utf8(files):
    # OEBPS/content.xhtml becomes "c\x81ntent.xhtml": 0x81 is u-umlaut in
    # CP437, the ZIP default; the UTF-8 flag (bit 11) is clear.
    es = _rename_content(files, "cüntent.xhtml", "c%C3%BCntent.xhtml")
    for e in es:
        if e.name == "OEBPS/cüntent.xhtml":
            e.name, e.flags = b"OEBPS/c\x81ntent.xhtml", 0
    return rz.build(es)


# --- 4 ZIP container ---------------------------------------------------------

def compression_bzip2(files):
    return _set_entry(files, CONTENT, method=12, version=46)


def version_needed_63(files):
    # "version needed to extract" 63 (ZIP 6.3) for the content document, in
    # both headers; the file is still deflated as before
    return _set_entry(files, CONTENT, version=63)


def zip64_unneeded(files):
    # ZIP64 sizes on the content document (0x0001 extra field in both headers,
    # 32-bit sizes 0xFFFFFFFF, version needed 45), which does not need them
    return _set_entry(files, CONTENT, zip64=True)


def zip_encryption(files):
    # traditional PKWARE encryption on the content document; password "epub-test-books"
    return _set_entry(files, CONTENT, password=b"epub-test-books")


# --- 3.5.1: the manifest and the ZIP archive -----------------------------------

def manifest_file_missing(files):
    return rz.build(_entries(files, drop=[CONTENT]))


def extra_unlisted_file(files, path):
    return rz.build(_entries(files, add=[(path, b"A file that is not in the manifest.\n")]))
