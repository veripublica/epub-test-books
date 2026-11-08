# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-container.xml-rootfile-elem/rootfile-missing-target/rootfile-missing-target.epub: Rootfile points to a file that does not exist.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `rootfile_missing_target()`.

Run: python3 scripts/epub-3.3/ocf/sec-container.xml-rootfile-elem/rootfile-missing-target/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-container.xml-rootfile-elem/rootfile-missing-target"


def main() -> None:
    info = eb.load_set(
        SET, title='Rootfile points to a file that does not exist',
        description="The rootfile element's full-path is OEBPS/missing.opf, which is not in the container. Does a validator reject it?",
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "rootfile-missing-target.epub"
    out.write_bytes(ov.rootfile_missing_target(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
