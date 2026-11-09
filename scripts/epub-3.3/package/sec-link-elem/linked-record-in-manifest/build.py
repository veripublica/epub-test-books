# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-link-elem/linked-record-in-manifest/linked-record-in-manifest.epub: a linked record that is also in the manifest.

The EPUB 3 template's files with one change to the package document, made by
scripts/lib/packagevariants.py.

Run: python3 scripts/epub-3.3/package/sec-link-elem/linked-record-in-manifest/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402

SET = "epub-3.3/package/sec-link-elem/linked-record-in-manifest"


def main() -> None:
    info = eb.load_set(
        SET, title='A linked record that is also in the manifest',
        description='A link element points to a standalone XML record in the container, and the manifest lists that record too. The record is not in the spine or embedded in a content document. Does a validator reject it?',
        subject="EPUB 3.3 package document")
    files = epub3.package(info, extra=[("record", "record.xml", "application/xml", "", pv.RECORD)])
    out = eb.write_epub(info.book_dir / "linked-record-in-manifest.epub", pv.linked_record(files))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
