# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-zip-container-mime/mimetype-extra-field/mimetype-extra-field.epub: Mimetype has an extra field in its ZIP header.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `mimetype_extra_field()`.

Run: python3 scripts/epub-3.3/ocf/sec-zip-container-mime/mimetype-extra-field/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-zip-container-mime/mimetype-extra-field"


def main() -> None:
    info = eb.load_set(
        SET, title='Mimetype has an extra field in its ZIP header',
        description="The mimetype entry's local header carries an extra field, the extended timestamp many zip tools add. Does a validator reject it?",
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "mimetype-extra-field.epub"
    out.write_bytes(ov.mimetype_extra_field(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
