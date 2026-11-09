# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/nav/sec-nav-def-model/label-img-no-alt/label-img-no-alt.epub: A navigation image with empty alt.

The EPUB 3 template's files with one change to the navigation document, made
with scripts/lib/navvariants.py.

Run: python3 scripts/epub-3.3/nav/sec-nav-def-model/label-img-no-alt/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import minijpeg  # noqa: E402
import packagevariants as pv  # noqa: E402
import navvariants as nv  # noqa: E402

SET = "epub-3.3/nav/sec-nav-def-model/label-img-no-alt"


def main() -> None:
    info = eb.load_set(
        SET, title='A navigation image with empty alt',
        description='An a element in the toc nav holds only an image with alt="". Does a validator reject it?',
        subject="EPUB 3.3 navigation document")
    files = nv.label_img_no_alt(pv.book_has_image(epub3.package(info, extra=[("image", "image.jpg", "image/jpeg", "", minijpeg.gray_jpeg())])))
    out = eb.write_epub(info.book_dir / "label-img-no-alt.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
