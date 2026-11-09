# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Small changes to the EPUB 2 template's package.opf and toc.ncx.

Every change asserts that it found exactly what it expected, so a template
change that moves the text stops the build instead of producing a book with
no defect.
"""

from __future__ import annotations

import re

OPF = "OEBPS/package.opf"
NCX = "OEBPS/toc.ncx"
XHTML = "application/xhtml+xml"
Files = list[tuple[str, "str | bytes"]]


def _in(files: Files, target: str, old: str, new: str) -> Files:
    out = []
    for name, data in files:
        if name == target:
            assert data.count(old) == 1, f"expected exactly one {old!r}"
            data = data.replace(old, new)
        out.append((name, data))
    return out


def opf(files: Files, old: str, new: str) -> Files:
    return _in(files, OPF, old, new)


def ncx(files: Files, old: str, new: str) -> Files:
    return _in(files, NCX, old, new)


def opf_re(files: Files, pattern: str, new: str) -> Files:
    out = []
    for name, data in files:
        if name == OPF:
            data, n = re.subn(pattern, new, data, flags=re.S)
            assert n == 1, f"expected exactly one match of {pattern!r}"
        out.append((name, data))
    return out


def ncx_re(files: Files, pattern: str, new: str) -> Files:
    out = []
    for name, data in files:
        if name == NCX:
            data, n = re.subn(pattern, new, data, flags=re.S)
            assert n == 1, f"expected exactly one match of {pattern!r}"
        out.append((name, data))
    return out


def add_item(files: Files, line: str) -> Files:
    return opf(files, "  </manifest>\n", f"    {line}\n  </manifest>\n")


def add_itemref(files: Files, line: str) -> Files:
    return opf(files, "  </spine>\n", f"    {line}\n  </spine>\n")


def after_spine(files: Files, block: str) -> Files:
    return opf(files, "  </spine>\n", f"  </spine>\n  {block}\n")


def extra_page(epub2) -> str:
    return epub2.xhtml("Extra", "    <h1>Extra</h1>\n    <p>An extra document.</p>")


def extra_item(epub2, id_: str = "extra", href: str = "extra.xhtml") -> tuple:
    return (id_, href, XHTML, extra_page(epub2))


def fallback(files: Files, item: str, target: str) -> Files:
    return opf(files, f'id="{item}" href=', f'id="{item}" fallback="{target}" href=')


def no_toc(files: Files) -> Files:
    return opf(files, '<spine toc="ncx">', "<spine>")


def without(files: Files, name: str) -> Files:
    out = [f for f in files if f[0] != name]
    assert len(out) == len(files) - 1
    return out


def wrap_dc_metadata(files: Files) -> Files:
    """Move the Dublin Core elements into dc-metadata and the meta elements into x-metadata."""
    out = []
    for name, data in files:
        if name == OPF:
            m = re.search(r"(  <metadata[^>]*>\n)(.*?)(  </metadata>\n)", data, flags=re.S)
            lines = m.group(2).splitlines(keepends=True)
            dc = "".join("  " + x for x in lines if x.lstrip().startswith("<dc:"))
            meta = "".join("  " + x for x in lines if x.lstrip().startswith("<meta"))
            assert dc and meta and len(lines) == dc.count("\n") + meta.count("\n")
            data = data.replace(m.group(0),
                                m.group(1) + "    <dc-metadata>\n" + dc + "    </dc-metadata>\n"
                                "    <x-metadata>\n" + meta + "    </x-metadata>\n" + m.group(3))
        out.append((name, data))
    return out
