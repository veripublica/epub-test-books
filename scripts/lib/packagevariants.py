# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""The package document sets' changes to the template's package.opf.

Each function takes the file list from a template's `package()` and returns
it with one change made to OEBPS/package.opf. Every change asserts that it
found exactly what it expected, so a template change that moves the text
stops the build instead of producing a book with no defect.
"""

from __future__ import annotations

import re

OPF = "OEBPS/package.opf"
Files = list[tuple[str, "str | bytes"]]

RECORD = """<?xml version="1.0" encoding="UTF-8"?>
<record xmlns="https://example.org/epub-test-books/ns">A standalone metadata record.</record>
"""
REMOTE_RECORD = "https://example.org/epub-test-books/record.xml"


def _edit(files: Files, change) -> Files:
    out = []
    for name, data in files:
        if name == OPF:
            new = change(data)
            assert new != data, "the change did nothing"
            data = new
        out.append((name, data))
    return out


def _replace(files: Files, old: str, new: str) -> Files:
    def change(s: str) -> str:
        assert s.count(old) == 1, f"expected exactly one {old!r}"
        return s.replace(old, new)
    return _edit(files, change)


def _remove(files: Files, pattern: str) -> Files:
    def change(s: str) -> str:
        s, n = re.subn(pattern, "", s, flags=re.S)
        assert n == 1, f"expected exactly one match of {pattern!r}"
        return s
    return _edit(files, change)


def _add_metadata(files: Files, line: str) -> Files:
    return _replace(files, "  </metadata>\n", f"    {line}\n  </metadata>\n")


def package_version_wrong(files: Files) -> Files:
    return _replace(files, ' version="3.0" unique-identifier', ' version="3.1" unique-identifier')


def unique_identifier_missing(files: Files) -> Files:
    return _replace(files, ' unique-identifier="uid"', "")


def version_missing(files: Files) -> Files:
    return _replace(files, ' version="3.0"', "")


def identifier_missing(files: Files) -> Files:
    return _remove(files, r'    <dc:identifier id="uid">[^<]*</dc:identifier>\n')


def language_missing(files: Files) -> Files:
    return _remove(files, r"    <dc:language>en</dc:language>\n")


def modified_twice(files: Files) -> Files:
    def change(s: str) -> str:
        s, n = re.subn(r'(    <meta property="dcterms:modified">[^<]*</meta>\n)',
                       r'\1    <meta property="dcterms:modified">2026-01-01T00:00:00Z</meta>\n',
                       s)
        assert n == 1
        return s
    return _edit(files, change)


def refines_self(files: Files) -> Files:
    return _add_metadata(
        files, '<meta id="self" refines="#self" property="schema:alternateName">A test book</meta>')


def meta_no_property(files: Files) -> Files:
    return _add_metadata(files, "<meta>A value with no property</meta>")


def linked_record(files: Files) -> Files:
    """A link to OEBPS/record.xml. The set decides whether the manifest lists it."""
    return _add_metadata(files, '<link rel="record" href="record.xml" media-type="application/xml"/>')


def link_no_rel(files: Files) -> Files:
    return _add_metadata(files, f'<link href="{REMOTE_RECORD}" media-type="application/xml"/>')


def link_no_href(files: Files) -> Files:
    return _add_metadata(files, '<link rel="record" media-type="application/xml"/>')


def manifest_missing(files: Files) -> Files:
    return _remove(files, r"  <manifest>.*?</manifest>\n")


def item_href_path_absolute(files: Files) -> Files:
    return _replace(files, 'id="content" href="content.xhtml"', 'id="content" href="/OEBPS/content.xhtml"')


def itemref_no_idref(files: Files) -> Files:
    return _replace(files, "  </spine>\n", "    <itemref/>\n  </spine>\n")


def book_has_image(files: Files) -> Files:
    """Make the accessibility metadata true of a book with one image."""
    files = _replace(files, '<meta property="schema:accessMode">textual</meta>',
                     '<meta property="schema:accessMode">textual</meta>\n'
                     '    <meta property="schema:accessMode">visual</meta>')
    files = _replace(files, '<meta property="schema:accessibilityFeature">readingOrder</meta>',
                     '<meta property="schema:accessibilityFeature">readingOrder</meta>\n'
                     '    <meta property="schema:accessibilityFeature">alternativeText</meta>')
    return _replace(files, "It has no images, audio, video or other non-text content, and no known hazards.",
                    "It has one small gray image with a text alternative, no audio or video, and no known hazards.")


def section(inner: str, title: str = "Content", id_: str = "content") -> str:
    """The body of a content document, in the template's shape."""
    return (f'    <section id="{id_}" epub:type="chapter" role="doc-chapter">\n'
            f"    <h1>{title}</h1>\n{inner}\n    </section>")


def _add_item(files: Files, line: str) -> Files:
    return _replace(files, "  </manifest>\n", f"    {line}\n  </manifest>\n")


def _add_itemref(files: Files, line: str) -> Files:
    return _replace(files, "  </spine>\n", f"    {line}\n  </spine>\n")


def _sub(files: Files, pattern: str, new: str) -> Files:
    def change(s: str) -> str:
        s, n = re.subn(pattern, new, s, flags=re.S)
        assert n == 1, f"expected exactly one match of {pattern!r}"
        return s
    return _edit(files, change)


def spine_before_manifest(files: Files) -> Files:
    return _sub(files, r"(  <manifest>.*?</manifest>\n)(  <spine>.*?</spine>\n)", r"\2\1")


def unique_identifier_unknown(files: Files) -> Files:
    return _replace(files, ' unique-identifier="uid"', ' unique-identifier="nope"')


def unique_identifier_not_identifier(files: Files) -> Files:
    files = _replace(files, "<dc:title>", '<dc:title id="title">')
    return _replace(files, ' unique-identifier="uid"', ' unique-identifier="title"')


def title_missing(files: Files) -> Files:
    return _remove(files, r"    <dc:title>[^<]*</dc:title>\n")


def title_spaces(files: Files) -> Files:
    return _sub(files, r"<dc:title>[^<]*</dc:title>", "<dc:title>   </dc:title>")


def identifier_spaces(files: Files) -> Files:
    return _sub(files, r'<dc:identifier id="uid">[^<]*</dc:identifier>',
                '<dc:identifier id="uid">   </dc:identifier>')


def language_empty(files: Files) -> Files:
    return _replace(files, "<dc:language>en</dc:language>", "<dc:language></dc:language>")


def meta_value_empty(files: Files) -> Files:
    return _add_metadata(files, '<meta property="schema:alternateName">   </meta>')


def language_malformed(files: Files) -> Files:
    return _replace(files, "<dc:language>en</dc:language>", "<dc:language>en_US</dc:language>")


def xml_lang_malformed(files: Files) -> Files:
    return _replace(files, ' xml:lang="en">', ' xml:lang="en_US">')


def date_twice(files: Files) -> Files:
    return _add_metadata(files, "<dc:date>2026-01-01</dc:date>")


def modified_missing(files: Files) -> Files:
    return _remove(files, r'    <meta property="dcterms:modified">[^<]*</meta>\n')


def modified_no_zulu(files: Files) -> Files:
    return _sub(files, r'(<meta property="dcterms:modified">[^<]*?)Z(</meta>)', r"\1+00:00\2")


def id_duplicate(files: Files) -> Files:
    return _add_metadata(files, '<meta id="collection" property="schema:alternateName">A test book</meta>')


def refines_cycle(files: Files) -> Files:
    files = _add_metadata(files, '<meta id="a" refines="#b" property="schema:alternateName">A test book</meta>')
    return _add_metadata(files, '<meta id="b" refines="#a" property="schema:alternateName">A test book</meta>')


def refines_target_missing(files: Files) -> Files:
    return _add_metadata(files, '<meta refines="#nope" property="schema:alternateName">A test book</meta>')


def link_href_manifest_id(files: Files) -> Files:
    return _add_metadata(files, '<link rel="record" href="#content" media-type="application/xhtml+xml"/>')


def link_media_type_missing(files: Files) -> Files:
    return _add_metadata(files + [("OEBPS/record.xml", RECORD)], '<link rel="record" href="record.xml"/>')


def link_hreflang_malformed(files: Files) -> Files:
    return _add_metadata(files, f'<link rel="record" href="{REMOTE_RECORD}" media-type="application/xml" hreflang="en_US"/>')


def link_with_content(files: Files) -> Files:
    return _add_metadata(files, f'<link rel="record" href="{REMOTE_RECORD}" media-type="application/xml">Text</link>')


def manifest_lists_package_doc(files: Files) -> Files:
    return _add_item(files, '<item id="opf" href="package.opf" media-type="application/oebps-package+xml"/>')


def item_duplicate_after_parsing(files: Files) -> Files:
    return _add_item(files, '<item id="content-again" href="./content.xhtml" media-type="application/xhtml+xml"/>')


def item_fallback_unknown(files: Files) -> Files:
    return _replace(files, 'id="content" href="content.xhtml"', 'id="content" fallback="nope" href="content.xhtml"')


def item_media_type_missing(files: Files) -> Files:
    return _add_item(files + [("OEBPS/extra.txt", "A plain text file.\n")], '<item id="extra" href="extra.txt"/>')


def nav_missing(files: Files) -> Files:
    return _replace(files, ' properties="nav"', "")


def spine_missing(files: Files) -> Files:
    return _remove(files, r"  <spine>.*?</spine>\n")


def spine_empty(files: Files) -> Files:
    return _sub(files, r"<spine>.*?</spine>", "<spine></spine>")


def nav_links_extra(files: Files) -> Files:
    """Add an entry for extra.xhtml to the navigation document."""
    out = []
    old = '        <li><a href="content.xhtml">Content</a></li>\n'
    for name, data in files:
        if name == "OEBPS/nav.xhtml":
            assert data.count(old) == 1
            data = data.replace(old, old + '        <li><a href="extra.xhtml">Extra</a></li>\n')
        out.append((name, data))
    return out


def itemref_unknown(files: Files) -> Files:
    return _add_itemref(files, '<itemref idref="nope"/>')


def itemref_duplicate(files: Files) -> Files:
    return _add_itemref(files, '<itemref idref="content"/>')


def itemref_not_content(files: Files) -> Files:
    return _add_itemref(files, '<itemref idref="extra-css"/>')


def no_linear_itemref(files: Files) -> Files:
    def change(s: str) -> str:
        s, n = re.subn(r'<itemref idref="(\w+)"/>', r'<itemref idref="\1" linear="no"/>', s)
        assert n == 2
        return s
    return _edit(files, change)


def non_linear_unreachable(files: Files) -> Files:
    return _add_itemref(files, '<itemref idref="extra" linear="no"/>')


def _subject_id(files: Files) -> Files:
    return _replace(files, "<dc:subject>", '<dc:subject id="subject">')


def subject_authority_no_term(files: Files) -> Files:
    return _add_metadata(_subject_id(files),
                         '<meta refines="#subject" property="authority">https://example.org/epub-test-books/scheme</meta>')


def subject_term_no_authority(files: Files) -> Files:
    return _add_metadata(_subject_id(files), '<meta refines="#subject" property="term">A1</meta>')


def meta_scheme_no_prefix(files: Files) -> Files:
    return _add_metadata(files, '<meta property="schema:alternateName" scheme="nope">A test book</meta>')
