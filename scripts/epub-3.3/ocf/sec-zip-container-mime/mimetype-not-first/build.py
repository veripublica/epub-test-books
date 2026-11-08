# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-zip-container-mime/mimetype-not-first/mimetype-not-first.epub: Mimetype is not the first entry.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `mimetype_not_first()`.

Run: python3 scripts/epub-3.3/ocf/sec-zip-container-mime/mimetype-not-first/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-zip-container-mime/mimetype-not-first"


def main() -> None:
    info = eb.load_set(
        SET, title='Mimetype is not the first entry',
        description='The mimetype file is present and correct, but it is the second entry in the ZIP file, after META-INF/container.xml. Does a validator reject it?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "mimetype-not-first.epub"
    out.write_bytes(ov.mimetype_not_first(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
