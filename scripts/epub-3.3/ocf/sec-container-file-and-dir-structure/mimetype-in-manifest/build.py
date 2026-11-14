# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-container-file-and-dir-structure/mimetype-in-manifest/mimetype-in-manifest.epub: The mimetype file listed in the manifest.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `mimetype_in_manifest()`.

Run: python3 scripts/epub-3.3/ocf/sec-container-file-and-dir-structure/mimetype-in-manifest/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-container-file-and-dir-structure/mimetype-in-manifest"


def main() -> None:
    info = eb.load_set(
        SET, title='The mimetype file listed in the manifest',
        description='The package document\'s manifest lists the mimetype file as an item (href="../mimetype"). Does a validator reject it?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "mimetype-in-manifest.epub"
    out.write_bytes(ov.mimetype_in_manifest(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
