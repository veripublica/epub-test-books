# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-zip-container-zipreqs/zip64-unneeded/zip64-unneeded.epub: ZIP64 sizes on an entry that does not need them.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `zip64_unneeded()`.

Run: python3 scripts/epub-3.3/ocf/sec-zip-container-zipreqs/zip64-unneeded/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-zip-container-zipreqs/zip64-unneeded"


def main() -> None:
    info = eb.load_set(
        SET, title='ZIP64 sizes on an entry that does not need them',
        description='OEBPS/content.xhtml, a small file, is written with ZIP64 sizes in both headers. Does a validator accept the container?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "zip64-unneeded.epub"
    out.write_bytes(ov.zip64_unneeded(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
