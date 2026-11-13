# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/resources/sec-core-media-types/script-foreign-media-type/script-foreign-media-type.epub: A script file listed as application/x-javascript (valid).

The EPUB 3 template's files, changed by scripts/lib/scriptvariants.py `script_foreign_media_type()`.

Run: python3 scripts/epub-3.3/resources/sec-core-media-types/script-foreign-media-type/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import scriptvariants as sv  # noqa: E402

SET = "epub-3.3/resources/sec-core-media-types/script-foreign-media-type"


def main() -> None:
    info = eb.load_set(
        SET, title='A script file listed as application/x-javascript (valid)',
        description='script.js is in the manifest as application/x-javascript. Does a validator accept the book?',
        subject="EPUB 3.3 scripting")
    out = eb.write_epub(info.book_dir / "script-foreign-media-type.epub", sv.script_foreign_media_type(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
