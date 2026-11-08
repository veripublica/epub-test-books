# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-container-file-and-dir-structure/link-into-meta-inf/link-into-meta-inf.epub: A link into META-INF.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `link_into_meta_inf()`.

Run: python3 scripts/epub-3.3/ocf/sec-container-file-and-dir-structure/link-into-meta-inf/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-container-file-and-dir-structure/link-into-meta-inf"


def main() -> None:
    info = eb.load_set(
        SET, title='A link into META-INF',
        description="The content document links to META-INF/container.xml. Does a validator reject it?",
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "link-into-meta-inf.epub"
    out.write_bytes(ov.link_into_meta_inf(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
