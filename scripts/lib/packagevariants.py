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
