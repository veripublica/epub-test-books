# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-container-filenames/filename-forbidden-char/filename-forbidden-char.epub: A file name with a vertical line.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `filename_forbidden_char()`.

Run: python3 scripts/epub-3.3/ocf/sec-container-filenames/filename-forbidden-char/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-container-filenames/filename-forbidden-char"


def main() -> None:
    info = eb.load_set(
        SET, title='A file name with a vertical line',
        description='The content document is named con|tent.xhtml. Does a validator reject it?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "filename-forbidden-char.epub"
    out.write_bytes(ov.filename_forbidden_char(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
