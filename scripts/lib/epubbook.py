# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Shared pieces for building the books in epub-test-books.

Every book is built from its set README (books/<set>/README.md) and its own
build script (scripts/<set>/build.py). The build is reproducible: the same
sources give a byte-identical .epub, so a pinned tag always means the same
bytes.

What comes from the README:
- the "About this book" section becomes about.xhtml inside the book;
- the "History" section gives dc:date (first entry) and dcterms:modified
  (last entry), so the date in the book says when the book last changed.

Books and other output these scripts produce are CC BY 4.0 (see NOTICE).
"""

from __future__ import annotations

import html
import re
import uuid
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

REPO_URL = "https://github.com/veripublica/epub-test-books"
CREDIT = ("EPUB test books © veripublica contributors, CC BY 4.0, "
          + REPO_URL)
COLLECTION = "epub-test-books"
ROOT = Path(__file__).resolve().parents[2]

# Fixed ZIP timestamp: the earliest DOS date. Entry times carry no meaning
# here; dcterms:modified inside the book does.
ZIP_TIME = (1980, 1, 1, 0, 0, 0)


@dataclass
class SetInfo:
    """What a build script needs to know about its set."""

    path: str                     # e.g. "templates/epub3-minimal"
    title: str                    # dc:title
    description: str              # dc:description: the question, one sentence
    subject: str                  # dc:subject: the area
    contributor: str | None = None  # dc:contributor: who asked for the set
    about: list[tuple[str, object]] = field(default_factory=list)
    first_date: str = ""          # YYYY-MM-DD
    last_date: str = ""           # YYYY-MM-DD

    @property
    def book_dir(self) -> Path:
        return ROOT / "books" / self.path

    @property
    def identifier(self) -> str:
        """One fixed UUID per set, derived from its path (UUID v5)."""
        return "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL,
                                            f"{REPO_URL}/books/{self.path}"))

    @property
    def modified(self) -> str:
        """dcterms:modified: the last History date, in UTC with a Z."""
        return f"{self.last_date}T00:00:00Z"


def load_set(path: str, *, title: str, description: str, subject: str,
             contributor: str | None = None) -> SetInfo:
    info = SetInfo(path=path, title=title, description=description,
                   subject=subject, contributor=contributor)
    text = (info.book_dir / "README.md").read_text(encoding="utf-8")
    info.about = parse_blocks(section(text, "About this book"))
    dates = re.findall(r"^- (\d{4}-\d{2}-\d{2}):", section(text, "History"),
                       re.M)
    if not dates:
        raise SystemExit(f"{path}: README has no dated History entry")
    if dates != sorted(dates):
        raise SystemExit(f"{path}: History dates are not in order")
    info.first_date, info.last_date = dates[0], dates[-1]
    return info


def section(text: str, heading: str) -> str:
    """The body of a '## heading' section, up to the next '## '."""
    m = re.search(rf"^## {re.escape(heading)}\s*$(.*?)(?=^## |\Z)", text,
                  re.M | re.S)
    if not m:
        raise SystemExit(f"README has no '## {heading}' section")
    return m.group(1).strip()


def parse_blocks(text: str) -> list[tuple[str, object]]:
    """A small Markdown subset: paragraphs, '- ' lists, '### ' headings,
    and '> ' quotes. Anything else is kept as plain text."""
    blocks: list[tuple[str, object]] = []
    for chunk in re.split(r"\n\s*\n", text):
        lines = [ln.rstrip() for ln in chunk.strip().splitlines()]
        if not lines:
            continue
        if lines[0].startswith("### "):
            blocks.append(("h2", lines[0][4:].strip()))
            lines = lines[1:]
            if not lines:
                continue
        if all(ln.startswith("- ") or ln.startswith("  ") for ln in lines):
            items: list[str] = []
            for ln in lines:
                if ln.startswith("- "):
                    items.append(ln[2:].strip())
                else:
                    items[-1] += " " + ln.strip()
            blocks.append(("ul", items))
        elif all(ln.startswith(">") for ln in lines):
            blocks.append(("quote", " ".join(ln.lstrip("> ").strip()
                                             for ln in lines)))
        else:
            blocks.append(("p", " ".join(ln.strip() for ln in lines)))
    return blocks


def inline(text: str) -> str:
    """Escape, then turn `code` into <code> and drop ** and * emphasis
    markers (kept as plain text: the book stays unstyled)."""
    out = []
    for i, part in enumerate(re.split(r"`([^`]*)`", text)):
        part = html.escape(part, quote=False)
        if i % 2:
            out.append(f"<code>{part}</code>")
        else:
            out.append(re.sub(r"\*\*?([^*]+)\*\*?", r"\1", part))
    return "".join(out)


def blocks_to_xhtml(blocks: list[tuple[str, object]]) -> str:
    out = []
    for kind, value in blocks:
        if kind == "h2":
            out.append(f"<h2>{inline(value)}</h2>")
        elif kind == "ul":
            items = "".join(f"<li>{inline(v)}</li>" for v in value)
            out.append(f"<ul>{items}</ul>")
        elif kind == "quote":
            out.append(f"<blockquote><p>{inline(value)}</p></blockquote>")
        else:
            out.append(f"<p>{inline(value)}</p>")
    return "\n".join("    " + line for line in out)


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def write_epub(out: Path, files: list[tuple[str, str | bytes]]) -> Path:
    """Write a reproducible OCF ZIP container.

    `mimetype` goes first, stored, with no extra field; every other entry is
    Deflate-compressed, in the order given. Timestamps, permissions and the
    creating system are fixed, so the output is byte-identical across runs
    and machines."""
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".tmp")
    entries = [("mimetype", b"application/epub+zip")]
    entries += [(n, d.encode("utf-8") if isinstance(d, str) else d)
                for n, d in files]
    with zipfile.ZipFile(tmp, "w") as z:
        for i, (name, data) in enumerate(entries):
            zi = zipfile.ZipInfo(name, date_time=ZIP_TIME)
            zi.create_system = 3                  # Unix
            zi.external_attr = 0o100644 << 16     # regular file, rw-r--r--
            if i == 0:
                zi.compress_type = zipfile.ZIP_STORED
                z.writestr(zi, data)
            else:
                zi.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(zi, data, compresslevel=9)
    raw = tmp.read_bytes()
    # mimetype must be the first entry, stored, with no extra field (OCF).
    assert raw[:4] == b"PK\x03\x04" and raw[30:38] == b"mimetype", out
    assert raw[8:10] == b"\x00\x00" and raw[28:30] == b"\x00\x00", out
    tmp.replace(out)
    return out
