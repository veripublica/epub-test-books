# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-zip-container-mime/mimetype-wrong-value/mimetype-wrong-value.epub: Mimetype holds the wrong media type.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `mimetype_wrong_value()`.

Run: python3 scripts/epub-3.3/ocf/sec-zip-container-mime/mimetype-wrong-value/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-zip-container-mime/mimetype-wrong-value"


def main() -> None:
    info = eb.load_set(
        SET, title='Mimetype holds the wrong media type',
        description='The mimetype file holds application/zip instead of application/epub+zip. Does a validator reject it?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "mimetype-wrong-value.epub"
    out.write_bytes(ov.mimetype_wrong_value(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
