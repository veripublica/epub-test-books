# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""The XHTML extension and SVG content document sets (EPUB 3.3 §6.1.3, §6.2.2,
C.2, D.1): epub:type, epub:prefix, RDFa and microdata, the deprecated switch
and trigger elements, and SVG content documents. Each function takes the
EPUB 3 template module and the set's info, and returns the book's files for
epubbook.write_epub(). Each set's build.py calls one of them.
"""

from __future__ import annotations

import minimedia
import packagevariants as pv
import resourcevariants as rv

P = "    <p>Content.</p>"
VOCAB = "https://example.org/epub-test-books/vocab#"


def _doc(t3, body, head=None, root=None):
    html = t3.xhtml("Content", pv.section(body))
    if head:
        html = rv.head_add(html, head)
    if root:
        html = rv.swap(html, "<html ", f"<html {root} ")
    return html


def _book(t3, info, content=None, props=None, extra=(), edit=None):
    files = t3.package(info, content=content, extra=list(extra))
    if props is not None:
        files = rv.content_properties(files, props)
    return edit(files) if edit else files


def _type_p(value):
    return f'    <p epub:type="{value}">Content.</p>'


# --- sec-xhtml-structural-semantics: where epub:type may go

def type_on_meta(t3, info):
    return _book(t3, info, _doc(t3, P, '<meta name="description" content="A test book." epub:type="chapter"/>'))


def type_on_link(t3, info):
    return _book(t3, info, _doc(t3, P, '<link rel="stylesheet" href="style.css" epub:type="chapter"/>'),
                 extra=[("style", "style.css", "text/css", "", "p { margin: 0; }\n")])


def type_on_style(t3, info):
    return _book(t3, info, _doc(t3, P, '<style epub:type="chapter">p { margin: 0; }</style>'))


def type_on_script_head(t3, info):
    return _book(t3, info, _doc(t3, P, '<script epub:type="chapter">let a = 1;</script>'), "scripted")


def type_on_script_body(t3, info):
    return _book(t3, info, _doc(t3, '    <script epub:type="chapter">let a = 1;</script>'), "scripted")


def type_on_meta_in_body(t3, info):
    return _book(t3, info, _doc(t3, '    <div itemscope=""><meta itemprop="name" content="A test book." epub:type="chapter"/></div>'))


def type_on_body(t3, info):
    return _book(t3, info, rv.swap(_doc(t3, P), "<body>", '<body epub:type="bodymatter">'))


def type_on_html(t3, info):
    return _book(t3, info, _doc(t3, P, root='epub:type="bodymatter"'))


def type_unknown_term(t3, info):
    return _book(t3, info, _doc(t3, _type_p("no-such-term")))


def type_two_terms(t3, info):
    return _book(t3, info, _doc(t3, _type_p("chapter bodymatter")))


# --- sec-epub-type-attribute and sec-property-datatype: the value

def type_empty(t3, info):
    return _book(t3, info, _doc(t3, _type_p("")))


def type_whitespace_only(t3, info):
    return _book(t3, info, _doc(t3, _type_p("  ")))


def type_prefix_only(t3, info):
    return _book(t3, info, _doc(t3, _type_p("foo:"), root=f'epub:prefix="foo: {VOCAB}"'))


# --- sec-prefix-attr and sec-reserved-prefixes

def prefix_declared(t3, info):
    return _book(t3, info, _doc(t3, _type_p("foo:bar"), root=f'epub:prefix="foo: {VOCAB}"'))


def prefix_undeclared(t3, info):
    return _book(t3, info, _doc(t3, _type_p("foo:bar")))


def prefix_two(t3, info):
    return _book(t3, info, _doc(t3, _type_p("foo:bar baz:qux"),
                                root=f'epub:prefix="foo: {VOCAB} baz: https://example.org/epub-test-books/other#"'))


def prefix_on_non_root(t3, info):
    return _book(t3, info, _doc(t3, f'    <div epub:prefix="foo: {VOCAB}">\n' + _type_p("foo:bar") + "\n    </div>"))


def prefix_no_space(t3, info):
    return _book(t3, info, _doc(t3, _type_p("foo:bar"), root=f'epub:prefix="foo:{VOCAB}"'))


def prefix_underscore(t3, info):
    return _book(t3, info, _doc(t3, _type_p("_:bar"), root=f'epub:prefix="_: {VOCAB}"'))


def prefix_override_reserved(t3, info):
    return _book(t3, info, _doc(t3, _type_p("msv:article"), root=f'epub:prefix="msv: {VOCAB}"'))


def reserved_prefix_msv(t3, info):
    return _book(t3, info, _doc(t3, _type_p("msv:article")))


def reserved_prefix_prism(t3, info):
    return _book(t3, info, _doc(t3, _type_p("prism:article")))


def z3998_undeclared(t3, info):
    return _book(t3, info, _doc(t3, _type_p("z3998:fiction")))


# --- sec-xhtml-rdfa: RDFa and microdata

def rdfa_attributes(t3, info):
    return _book(t3, info, _doc(t3, '    <div vocab="https://schema.org/" typeof="Book"><p property="name">A test book.</p></div>'))


def rdfa_prefix_no_colon(t3, info):
    return _book(t3, info, _doc(t3, '    <div prefix="dc http://purl.org/dc/terms/"><p property="dc:title">A test book.</p></div>'))


def microdata_attributes(t3, info):
    return _book(t3, info, _doc(t3, '    <div itemscope="" itemtype="https://schema.org/Book"><p itemprop="name">A test book.</p></div>'))


def rdfa_prefix_two_spaces(t3, info):
    return _book(t3, info, _doc(t3, '    <div prefix="dc:  http://purl.org/dc/terms/"><p property="dc:title">A test book.</p></div>'))


def rdfa_prefix_tab(t3, info):
    # &#9; is a character reference, so attribute-value normalization keeps the tab
    return _book(t3, info, _doc(t3, '    <div prefix="dc:&#9;http://purl.org/dc/terms/"><p property="dc:title">A test book.</p></div>'))


def microdata_itemtype_no_itemscope(t3, info):
    return _book(t3, info, _doc(t3, '    <div itemtype="https://schema.org/Book"><p>A test book.</p></div>'))


def microdata_itemref_no_itemscope(t3, info):
    return _book(t3, info, _doc(t3, '    <div itemref="title"><p>A test book.</p></div>\n    <p id="title">Content.</p>'))


def microdata_itemid_no_itemtype(t3, info):
    return _book(t3, info, _doc(t3, '    <div itemscope="" itemid="urn:isbn:9780306406157"><p itemprop="name">A test book.</p></div>'))


# --- sec-xhtml-content-switch (deprecated)

def _switch(case_attr=' required-namespace="http://www.w3.org/1998/Math/MathML"', default=True):
    return ('    <epub:switch id="sw1">\n'
            f'      <epub:case{case_attr}><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></epub:case>\n'
            + ('      <epub:default><p>x</p></epub:default>\n' if default else "")
            + '    </epub:switch>')


def switch_element(t3, info):
    return _book(t3, info, _doc(t3, _switch()), "mathml switch")


def switch_no_default(t3, info):
    return _book(t3, info, _doc(t3, _switch(default=False)), "mathml switch")


def switch_case_no_namespace(t3, info):
    return _book(t3, info, _doc(t3, _switch(case_attr="")), "mathml switch")


def switch_property_missing(t3, info):
    return _book(t3, info, _doc(t3, _switch()), "mathml")


# --- sec-xhtml-epub-trigger (deprecated)

MP3 = ("sound", "sound.mp3", "audio/mpeg", "", None)
PLAYER = ('    <p><audio id="a1" src="sound.mp3" controls="controls">A short silent sound.</audio></p>\n'
          '    <p id="b1">Show</p>')


def _trigger(action="show", ref="b1"):
    return (f'<epub:trigger xmlns:ev="http://www.w3.org/2001/xml-events" action="{action}" ref="{ref}"'
            ' ev:observer="b1" ev:event="click"/>')


def _trigger_book(t3, info, body, head=None):
    mp3 = MP3[:4] + (minimedia.silent_mp3(),)
    return _book(t3, info, _doc(t3, body, head), extra=[mp3], edit=rv.book_has_audio)


def trigger_in_head(t3, info):
    return _trigger_book(t3, info, PLAYER, _trigger())


def trigger_in_body(t3, info):
    return _trigger_book(t3, info, PLAYER + "\n    " + _trigger())


def trigger_ref_missing(t3, info):
    return _trigger_book(t3, info, PLAYER, _trigger(ref="nowhere"))


def trigger_unknown_action(t3, info):
    return _trigger_book(t3, info, PLAYER, _trigger(action="explode"))


# --- sec-svg-req: SVG content documents

PICTURE = '<title>A small picture</title><rect width="40" height="40" fill="gray"/>'
XMLDECL = '<?xml version="1.0" encoding="UTF-8"?>\n'
SVGROOT = '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40">'


def _svg_book(t3, info, data):
    return _book(t3, info, extra=[("picture", "picture.svg", "image/svg+xml", "", data)],
                 edit=lambda f: rv.add_itemref(f, '<itemref idref="picture"/>'))


def svg_document(t3, info):
    return _svg_book(t3, info, f"{XMLDECL}{SVGROOT}{PICTURE}</svg>\n")


def svg_no_namespace(t3, info):
    return _svg_book(t3, info, f'{XMLDECL}<svg width="40" height="40">{PICTURE}</svg>\n')


def svg_root_not_svg(t3, info):
    return _svg_book(t3, info, f'{XMLDECL}<g xmlns="http://www.w3.org/2000/svg">{PICTURE}</g>\n')


def svg_not_well_formed(t3, info):
    return _svg_book(t3, info, f"{XMLDECL}{SVGROOT}{PICTURE}\n")


def svg_doctype_svg11(t3, info):
    return _svg_book(t3, info, f'{XMLDECL}<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" '
                               f'"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n{SVGROOT}{PICTURE}</svg>\n')


def svg_undeclared_xlink_prefix(t3, info):
    return _svg_book(t3, info, f'{XMLDECL}{SVGROOT}{PICTURE}<use xlink:href="#r"/></svg>\n')
