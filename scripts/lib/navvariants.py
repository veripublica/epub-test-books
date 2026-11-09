# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""The navigation document sets' changes to the template's nav.xhtml.

Each function takes the file list from a template's `package()` and returns
it with one change made to OEBPS/nav.xhtml. Every change asserts that it
found exactly what it expected, so a template change that moves the text
stops the build instead of producing a book with no defect.
"""

from __future__ import annotations

import re

NAV = "OEBPS/nav.xhtml"
Files = list[tuple[str, "str | bytes"]]

OPEN = '    <nav epub:type="toc" id="toc" role="doc-toc">'
ABOUT_LI = '        <li><a href="about.xhtml">About this book</a></li>\n'
CONTENT_LI = '        <li><a href="content.xhtml">Content</a></li>\n'
HEADING = "      <h1>Contents</h1>\n"
END_OL = "      </ol>\n    </nav>\n"
END_BODY = "  </body>\n"
EXTERNAL = "https://example.org/epub-test-books/"

SVG = ('<svg xmlns="http://www.w3.org/2000/svg" width="8" height="8">'
       '<rect width="8" height="8" fill="gray"/></svg>')

PAGE_LIST = ('    <nav epub:type="page-list">\n      <h2>Pages</h2>\n      <ol>\n'
             '        <li><a href="content.xhtml#content">1</a></li>\n      </ol>\n    </nav>\n')
LANDMARKS = ('    <nav epub:type="landmarks">\n      <h2>Guide</h2>\n      <ol>\n'
             '        <li><a epub:type="bodymatter" href="content.xhtml">Start</a></li>\n'
             '      </ol>\n    </nav>\n')


def _replace(files: Files, old: str, new: str) -> Files:
    out = []
    for name, data in files:
        if name == NAV:
            assert data.count(old) == 1, f"expected exactly one {old!r}"
            data = data.replace(old, new)
        out.append((name, data))
    return out


def _add_nav(files: Files, block: str) -> Files:
    return _replace(files, END_BODY, block + END_BODY)


def _content_li(files: Files, li: str) -> Files:
    return _replace(files, CONTENT_LI, f"        {li}\n")


def _add_li(files: Files, li: str) -> Files:
    return _replace(files, CONTENT_LI, CONTENT_LI + f"        {li}\n")


def toc_missing(files: Files) -> Files:
    return _replace(files, OPEN, '    <nav epub:type="lot" id="toc">')


def toc_twice(files: Files) -> Files:
    return _add_nav(files, '    <nav epub:type="toc">\n      <h2>Contents again</h2>\n      <ol>\n'
                           '        <li><a href="content.xhtml">Content</a></li>\n      </ol>\n    </nav>\n')


def label_empty(files: Files) -> Files:
    return _content_li(files, '<li><a href="content.xhtml"></a></li>')


def label_spaces(files: Files) -> Files:
    return _content_li(files, '<li><a href="content.xhtml">   </a></li>')


def label_empty_span(files: Files) -> Files:
    return _content_li(files, '<li><span></span><ol><li><a href="content.xhtml">Content</a></li></ol></li>')


def label_img_no_alt(files: Files) -> Files:
    return _content_li(files, '<li><a href="content.xhtml"><img src="image.jpg" alt=""/></a></li>')


def label_img_alt(files: Files) -> Files:
    return _content_li(files, '<li><a href="content.xhtml"><img src="image.jpg" alt="Content"/></a></li>')


def label_svg_no_title(files: Files) -> Files:
    return _content_li(files, f'<li><a href="content.xhtml">{SVG}</a></li>')


def toc_link_external(files: Files) -> Files:
    return _add_li(files, f'<li><a href="{EXTERNAL}">Elsewhere</a></li>')


def toc_link_css(files: Files) -> Files:
    return _add_li(files, '<li><a href="extra.css">A stylesheet</a></li>')


def toc_link_fragment_missing(files: Files) -> Files:
    return _add_li(files, '<li><a href="content.xhtml#nope">Nowhere</a></li>')


def span_leaf(files: Files) -> Files:
    return _add_li(files, "<li><span>A group</span></li>")


def li_no_label(files: Files) -> Files:
    return _add_li(files, '<li><ol><li><a href="content.xhtml#content">Content</a></li></ol></li>')


def li_two_links(files: Files) -> Files:
    return _content_li(files, '<li><a href="content.xhtml">Content</a><a href="content.xhtml#content">Again</a></li>')


def ol_empty(files: Files) -> Files:
    files = _replace(files, ABOUT_LI, "")
    return _replace(files, CONTENT_LI, "")


def nav_two_ol(files: Files) -> Files:
    return _replace(files, END_OL, "      </ol>\n      <ol>\n        "
                    '<li><a href="content.xhtml#content">Again</a></li>\n' + END_OL)


def heading_after_ol(files: Files) -> Files:
    files = _replace(files, HEADING, "")
    return _replace(files, END_OL, "      </ol>\n" + HEADING + "    </nav>\n")


def two_headings(files: Files) -> Files:
    return _replace(files, HEADING, HEADING + "      <h2>More contents</h2>\n")


def heading_p(files: Files) -> Files:
    return _replace(files, HEADING, "      <p>Contents</p>\n")


def sublist_empty(files: Files) -> Files:
    return _content_li(files, '<li><a href="content.xhtml">Content</a><ol></ol></li>')


def sublist_no_label(files: Files) -> Files:
    return _content_li(files, '<li><a href="content.xhtml">Content</a><ol><li><a href="content.xhtml#content"></a></li></ol></li>')


def page_list_twice(files: Files) -> Files:
    return _add_nav(files, PAGE_LIST + PAGE_LIST)


def landmarks_twice(files: Files) -> Files:
    return _add_nav(files, LANDMARKS + LANDMARKS)


def landmarks_no_type(files: Files) -> Files:
    return _add_nav(files, LANDMARKS.replace(' epub:type="bodymatter"', ""))


def landmarks_duplicate(files: Files) -> Files:
    li = '        <li><a epub:type="bodymatter" href="content.xhtml">Start</a></li>\n'
    return _add_nav(files, LANDMARKS.replace(li, li + li))


def other_nav_restricted(files: Files) -> Files:
    return _add_nav(files, '    <nav epub:type="lot">\n      <h2>Tables</h2>\n      <ul>\n'
                           '        <li><a href="content.xhtml">A table</a></li>\n      </ul>\n    </nav>\n')


def toc_nested(files: Files) -> Files:
    return _content_li(files, '<li><a href="content.xhtml">Content</a><ol><li><a href="content.xhtml#content">A part</a></li></ol></li>')


def span_group(files: Files) -> Files:
    return _content_li(files, '<li><span>A group</span><ol><li><a href="content.xhtml">Content</a></li></ol></li>')


def page_list(files: Files) -> Files:
    return _add_nav(files, PAGE_LIST)


def landmarks(files: Files) -> Files:
    return _add_nav(files, LANDMARKS)


def landmarks_same_type_different_resources(files: Files) -> Files:
    return _add_nav(files, '    <nav epub:type="landmarks">\n      <h2>Guide</h2>\n      <ol>\n'
                           '        <li><a epub:type="chapter" href="about.xhtml">About</a></li>\n'
                           '        <li><a epub:type="chapter" href="content.xhtml">Start</a></li>\n'
                           '      </ol>\n    </nav>\n')


def other_nav_no_heading(files: Files) -> Files:
    return _add_nav(files, '    <nav epub:type="lot">\n      <ol>\n'
                           '        <li><a href="content.xhtml">A table</a></li>\n      </ol>\n    </nav>\n')


def other_nav_no_type(files: Files) -> Files:
    return _add_nav(files, '    <nav>\n      <h2>Other</h2>\n      <ul>\n'
                           '        <li><a href="content.xhtml">A link</a></li>\n      </ul>\n    </nav>\n')


def other_nav_external(files: Files) -> Files:
    return _add_nav(files, '    <nav epub:type="lot">\n      <h2>Tables</h2>\n      <ol>\n'
                           f'        <li><a href="{EXTERNAL}">Elsewhere</a></li>\n      </ol>\n    </nav>\n')


def page_list_hidden(files: Files) -> Files:
    return _add_nav(files, PAGE_LIST.replace('<nav epub:type="page-list">', '<nav epub:type="page-list" hidden="hidden">'))


def toc_partial(files: Files) -> Files:
    return _replace(files, CONTENT_LI, "")
