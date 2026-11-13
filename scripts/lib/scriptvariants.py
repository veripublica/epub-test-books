# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""The scripting sets (EPUB 3.3 §6.3.2 and the `scripted` property): each
function takes the EPUB 3 template module and the set's info, and returns the
book's files for epubbook.write_epub(). Each set's build.py calls one of them.
"""

from __future__ import annotations

import packagevariants as pv
import resourcevariants as rv

INLINE = "    <script>let a = 1;</script>"
JS = "document.documentElement.classList.add('js');\n"
FORM = '    <form action="#"><p><input type="text" name="q" aria-label="Query"/></p></form>'


def _doc(t3, body, head=None):
    html = t3.xhtml("Content", pv.section(body))
    return rv.head_add(html, head) if head else html


def _book(t3, info, content=None, props=None, extra=(), edit=None):
    files = t3.package(info, content=content, extra=list(extra))
    if props is not None:
        files = rv.content_properties(files, props)
    return edit(files) if edit else files


def _external(t3, info, media_type):
    return _book(t3, info, _doc(t3, "    <p>Content.</p>", '<script src="script.js"></script>'), "scripted",
                 [("js", "script.js", media_type, "", JS)])


# --- sec-scripted-content: what counts as scripted content

def inline_script(t3, info):
    return _book(t3, info, _doc(t3, INLINE), "scripted")


def external_script(t3, info):
    return _external(t3, info, "application/javascript")


def module_script(t3, info):
    return _book(t3, info, _doc(t3, '    <script type="module">let a = 1;</script>'), "scripted")


def data_block(t3, info):
    return _book(t3, info, _doc(t3, '    <script type="application/json">{"a": 1}</script>'))


def data_block_unknown_type(t3, info):
    return _book(t3, info, _doc(t3, '    <script type="text/x-template">&lt;p&gt;A template.&lt;/p&gt;</script>'))


def form_element(t3, info):
    return _book(t3, info, _doc(t3, FORM), "scripted")


def input_without_form(t3, info):
    return _book(t3, info, _doc(t3, '    <p><input type="text" name="q" aria-label="Query"/></p>'))


def _svg_doc(props):
    _, href, mt, _, data = rv.standalone_svg('<rect width="40" height="40" fill="gray"/><script>let a = 1;</script>')
    return ("picture", href, mt, props, data)


def svg_document_script(t3, info):
    return _book(t3, info, extra=[_svg_doc("scripted")], edit=lambda f: rv.add_itemref(f, '<itemref idref="picture"/>'))


# --- sec-item-resource-properties: the scripted property missing

def scripted_form_missing(t3, info):
    return _book(t3, info, _doc(t3, FORM))


def scripted_event_handler_missing(t3, info):
    return _book(t3, info, _doc(t3, '    <p onclick="this.hidden = true">Content.</p>'))


def scripted_module_missing(t3, info):
    return _book(t3, info, _doc(t3, '    <script type="module">let a = 1;</script>'))


def scripted_svg_document_missing(t3, info):
    return _book(t3, info, extra=[_svg_doc("")], edit=lambda f: rv.add_itemref(f, '<itemref idref="picture"/>'))


def scripted_inline_svg_missing(t3, info):
    return _book(t3, info, _doc(t3, rv.inline_svg('<rect width="40" height="40" fill="gray"/><script>let a = 1;</script>')), "svg")


def _framed(t3, props):
    return ("framed", "framed.xhtml", "application/xhtml+xml", props,
            t3.xhtml("Framed", pv.section(INLINE, "Framed", "framed")))


def _iframe_doc(t3):
    return _doc(t3, '    <p><iframe src="framed.xhtml" title="A framed document"></iframe></p>')


def scripted_iframe_child(t3, info):
    return _book(t3, info, _iframe_doc(t3), None, [_framed(t3, "scripted")])


def scripted_iframe_child_missing(t3, info):
    return _book(t3, info, _iframe_doc(t3), None, [_framed(t3, "")])


# --- sec-core-media-types and sec-resource-locations

def script_text_javascript(t3, info):
    return _external(t3, info, "text/javascript")


def script_application_ecmascript(t3, info):
    return _external(t3, info, "application/ecmascript")


def script_foreign_media_type(t3, info):
    return _external(t3, info, "application/x-javascript")


def remote_script(t3, info):
    url = rv.REMOTE + "script.js"
    return _book(t3, info, _doc(t3, "    <p>Content.</p>", f'<script src="{url}"></script>'), "scripted remote-resources",
                 edit=lambda f: rv.add_item(f, f'<item id="js" href="{url}" media-type="application/javascript"/>'))


# --- sec-xhtml-req

def noscript(t3, info):
    return _book(t3, info, _doc(t3, INLINE + "\n    <noscript><p>Scripting is off.</p></noscript>"), "scripted")
