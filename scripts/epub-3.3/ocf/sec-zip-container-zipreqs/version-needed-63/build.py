# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-zip-container-zipreqs/version-needed-63/version-needed-63.epub: A file whose 'version needed to extract' is 63.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `version_needed_63()`.

Run: python3 scripts/epub-3.3/ocf/sec-zip-container-zipreqs/version-needed-63/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-zip-container-zipreqs/version-needed-63"


def main() -> None:
    info = eb.load_set(
        SET, title="A file whose 'version needed to extract' is 63",
        description='The ZIP headers of OEBPS/content.xhtml give 63 as the version needed to extract. Does a validator reject the book?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "version-needed-63.epub"
    out.write_bytes(ov.version_needed_63(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
