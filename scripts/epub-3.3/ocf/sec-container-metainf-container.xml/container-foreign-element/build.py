# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-container-metainf-container.xml/container-foreign-element/container-foreign-element.epub: An element from another namespace in container.xml.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `container_foreign_element()`.

Run: python3 scripts/epub-3.3/ocf/sec-container-metainf-container.xml/container-foreign-element/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-container-metainf-container.xml/container-foreign-element"


def main() -> None:
    info = eb.load_set(
        SET, title='An element from another namespace in container.xml',
        description='META-INF/container.xml has an element from another namespace after rootfiles. Does a validator accept it?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "container-foreign-element.epub"
    out.write_bytes(ov.container_foreign_element(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
