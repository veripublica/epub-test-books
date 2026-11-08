# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/templates/epub2-minimal/epub2-minimal.epub.

Every part EPUB 2.0.1 requires (OPF, OPS and OCF 2.0.1), plus the SHOULDs and
the library's metadata in their EPUB 2 forms; the README lists each part with
its clause. A set's build script calls `package()` with its own SetInfo.

Run: python3 scripts/templates/epub2-minimal/build.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "lib"))
import epubbook as eb  # noqa: E402

SET = "templates/epub2-minimal"

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
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
  <head>
    <meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8"/>
    <title>{eb.esc(title)}</title>
  </head>
  <body>
{body}
  </body>
</html>
"""


def about_doc(info: eb.SetInfo) -> str:
    body = (f'    <div id="about">\n'
            f"    <h1>About this book</h1>\n"
            f"{eb.blocks_to_xhtml(info.about)}\n"
            f"    <p>{eb.esc(eb.CREDIT)}</p>\n"
            f"    </div>")
    return xhtml("About this book", body)


def content_doc() -> str:
    body = ('    <div id="content">\n'
            "    <h1>Content</h1>\n"
            "    <p>This is the document a set changes. In the template it "
            "holds only this paragraph.</p>\n"
            "    </div>")
    return xhtml("Content", body)


def ncx(info: eb.SetInfo, entries: list[tuple[str, str]]) -> str:
    points = "\n".join(
        f'    <navPoint id="np{n}" playOrder="{n}">\n'
        f"      <navLabel><text>{eb.esc(t)}</text></navLabel>\n"
        f'      <content src="{eb.esc(h)}"/>\n'
        f"    </navPoint>"
        for n, (h, t) in enumerate(entries, 1))
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="en">
  <head>
    <meta name="dtb:uid" content="{info.identifier}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>{eb.esc(info.title)}</text></docTitle>
  <navMap>
{points}
  </navMap>
</ncx>
"""


def opf(info: eb.SetInfo, manifest: list[tuple[str, str, str]],
        spine: list[str]) -> str:
    contributor = (f"    <dc:contributor>{eb.esc(info.contributor)}</dc:contributor>\n"
                   if info.contributor else "")
    items = "\n".join(f'    <item id="{i}" href="{h}" media-type="{m}"/>'
                      for i, h, m in manifest)
    refs = "\n".join(f'    <itemref idref="{i}"/>' for i in spine)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="2.0" unique-identifier="uid">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <dc:identifier id="uid">{info.identifier}</dc:identifier>
    <dc:title>{eb.esc(info.title)}</dc:title>
    <dc:language>en</dc:language>
    <dc:creator>veripublica</dc:creator>
    <dc:publisher>veripublica</dc:publisher>
{contributor}    <dc:date opf:event="publication">{info.first_date}</dc:date>
    <dc:date opf:event="modification">{info.last_date}</dc:date>
    <dc:description>{eb.esc(info.description)}</dc:description>
    <dc:subject>{eb.esc(info.subject)}</dc:subject>
    <dc:rights>{eb.esc(eb.CREDIT)}</dc:rights>
    <dc:source>{eb.REPO_URL}</dc:source>
    <meta name="schema:accessMode" content="textual"/>
    <meta name="schema:accessModeSufficient" content="textual"/>
    <meta name="schema:accessibilityFeature" content="tableOfContents"/>
    <meta name="schema:accessibilityFeature" content="readingOrder"/>
    <meta name="schema:accessibilityFeature" content="structuralNavigation"/>
    <meta name="schema:accessibilityHazard" content="none"/>
    <meta name="schema:accessibilitySummary" content="{eb.esc(A11Y_SUMMARY)}"/>
  </metadata>
  <manifest>
{items}
  </manifest>
  <spine toc="ncx">
{refs}
  </spine>
</package>
"""


def package(info: eb.SetInfo, *, content: str | None = None,
            extra: list[tuple[str, str, str, str | bytes]] = ()
            ) -> list[tuple[str, str | bytes]]:
    """The files of a book built from this template, in ZIP order (after
    mimetype). `extra` adds (id, href, media-type, data) manifest items."""
    manifest = [
        ("about", "about.xhtml", "application/xhtml+xml"),
        ("content", "content.xhtml", "application/xhtml+xml"),
        ("ncx", "toc.ncx", "application/x-dtbncx+xml"),
    ] + [(i, h, m) for i, h, m, _ in extra]
    return [
        ("META-INF/container.xml", CONTAINER),
        ("OEBPS/package.opf", opf(info, manifest, ["about", "content"])),
        ("OEBPS/about.xhtml", about_doc(info)),
        ("OEBPS/content.xhtml", content if content is not None else content_doc()),
        ("OEBPS/toc.ncx", ncx(info, [("about.xhtml", "About this book"),
                                     ("content.xhtml", "Content")])),
    ] + [(f"OEBPS/{h}", d) for _, h, _, d in extra]


def main() -> None:
    info = eb.load_set(
        SET, title="Test book",
        description="The EPUB 2.0.1 template: every required part, and "
                    "nothing that raises a finding.",
        subject="EPUB 2.0.1")
    out = eb.write_epub(info.book_dir / "epub2-minimal.epub", package(info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
