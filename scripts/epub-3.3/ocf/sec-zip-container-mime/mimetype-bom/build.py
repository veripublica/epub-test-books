# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-zip-container-mime/mimetype-bom/mimetype-bom.epub: Mimetype starts with a byte order mark.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `mimetype_bom()`.

Run: python3 scripts/epub-3.3/ocf/sec-zip-container-mime/mimetype-bom/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-zip-container-mime/mimetype-bom"


def main() -> None:
    info = eb.load_set(
        SET, title='Mimetype starts with a byte order mark',
        description='The mimetype file starts with the UTF-8 byte order mark, then application/epub+zip. Does a validator reject it?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "mimetype-bom.epub"
    out.write_bytes(ov.mimetype_bom(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
