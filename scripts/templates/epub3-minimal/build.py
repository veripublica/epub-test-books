# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/templates/epub3-minimal/epub3-minimal.epub.

Every part EPUB 3.3 requires, plus the SHOULDs and the metadata decided for
the library; the README lists each part with its clause. A set's build script
calls `package()` with its own SetInfo and documents, and changes only what
its question needs.

Run: python3 scripts/templates/epub3-minimal/build.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "lib"))
import epubbook as eb  # noqa: E402

SET = "templates/epub3-minimal"

CONTAINER = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/package.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
"""

A11Y_SUMMARY = ("A short text-only book with a table of contents and a "
                "logical reading order. It has no images, audio, video or "
                "other non-text content, and no known hazards.")


def xhtml(title: str, body: str) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en" lang="en">
  <head>
    <meta charset="UTF-8"/>
    <title>{eb.esc(title)}</title>
  </head>
  <body>
{body}
  </body>
</html>
"""


def about_doc(info: eb.SetInfo) -> str:
    body = (f'    <section id="about" epub:type="preface" role="doc-preface">\n'
            f"    <h1>About this book</h1>\n"
            f"{eb.blocks_to_xhtml(info.about)}\n"
            f"    <p>{eb.esc(eb.CREDIT)}</p>\n"
            f"    </section>")
    return xhtml("About this book", body)


def content_doc() -> str:
    body = ("    <section id=\"content\" epub:type=\"chapter\" role=\"doc-chapter\">\n"
            "    <h1>Content</h1>\n"
            "    <p>This is the document a set changes. In the template it "
            "holds only this paragraph.</p>\n"
            "    </section>")
    return xhtml("Content", body)


def nav_doc(entries: list[tuple[str, str]]) -> str:
    items = "\n".join(f'        <li><a href="{eb.esc(h)}">{eb.esc(t)}</a></li>'
                      for h, t in entries)
    body = (f'    <nav epub:type="toc" id="toc" role="doc-toc">\n'
            f"      <h1>Contents</h1>\n"
            f"      <ol>\n{items}\n      </ol>\n"
            f"    </nav>")
    return xhtml("Contents", body)


def opf(info: eb.SetInfo, manifest: list[tuple[str, str, str, str]],
        spine: list[str]) -> str:
    contributor = (f"    <dc:contributor>{eb.esc(info.contributor)}</dc:contributor>\n"
                   if info.contributor else "")
    items = "\n".join(
        f'    <item id="{i}" href="{h}" media-type="{m}"'
        + (f' properties="{p}"' if p else "") + "/>"
        for i, h, m, p in manifest)
    refs = "\n".join(f'    <itemref idref="{i}"/>' for i in spine)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid" xml:lang="en">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="uid">{info.identifier}</dc:identifier>
    <dc:title>{eb.esc(info.title)}</dc:title>
    <dc:language>en</dc:language>
    <dc:creator>veripublica</dc:creator>
    <dc:publisher>veripublica</dc:publisher>
{contributor}    <dc:date>{info.first_date}</dc:date>
    <dc:description>{eb.esc(info.description)}</dc:description>
    <dc:subject>{eb.esc(info.subject)}</dc:subject>
    <dc:rights>{eb.esc(eb.CREDIT)}</dc:rights>
    <dc:source>{eb.REPO_URL}</dc:source>
    <meta property="dcterms:modified">{info.modified}</meta>
    <meta property="belongs-to-collection" id="collection">{eb.COLLECTION}</meta>
    <meta refines="#collection" property="collection-type">set</meta>
    <meta property="schema:accessMode">textual</meta>
    <meta property="schema:accessModeSufficient">textual</meta>
    <meta property="schema:accessibilityFeature">tableOfContents</meta>
    <meta property="schema:accessibilityFeature">readingOrder</meta>
    <meta property="schema:accessibilityFeature">structuralNavigation</meta>
    <meta property="schema:accessibilityHazard">none</meta>
    <meta property="schema:accessibilitySummary">{eb.esc(A11Y_SUMMARY)}</meta>
  </metadata>
  <manifest>
{items}
  </manifest>
  <spine>
{refs}
  </spine>
</package>
"""


def package(info: eb.SetInfo, *, content: str | None = None,
            extra: list[tuple[str, str, str, str, str | bytes]] = (),
            out_name: str | None = None) -> list[tuple[str, str | bytes]]:
    """The files of a book built from this template, in ZIP order (after
    mimetype). `extra` adds (id, href, media-type, properties, data) items to
    the manifest; a set that needs more than that edits the list it gets
    back."""
    manifest = [
        ("about", "about.xhtml", "application/xhtml+xml", ""),
        ("content", "content.xhtml", "application/xhtml+xml", ""),
        ("nav", "nav.xhtml", "application/xhtml+xml", "nav"),
    ] + [(i, h, m, p) for i, h, m, p, _ in extra]
    files: list[tuple[str, str | bytes]] = [
        ("META-INF/container.xml", CONTAINER),
        ("OEBPS/package.opf", opf(info, manifest, ["about", "content"])),
        ("OEBPS/about.xhtml", about_doc(info)),
        ("OEBPS/content.xhtml", content if content is not None else content_doc()),
        ("OEBPS/nav.xhtml", nav_doc([("about.xhtml", "About this book"),
                                     ("content.xhtml", "Content")])),
    ] + [(f"OEBPS/{h}", d) for _, h, _, _, d in extra]
    return files


def main() -> None:
    info = eb.load_set(
        SET, title="Test book",
        description="The EPUB 3.3 template: every required part, and nothing "
                    "that raises a finding.",
        subject="EPUB 3.3")
    out = eb.write_epub(info.book_dir / "epub3-minimal.epub", package(info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
