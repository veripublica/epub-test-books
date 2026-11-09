# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-meta-elem/meta-scheme-no-prefix/meta-scheme-no-prefix.epub: A scheme value with no prefix.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/packagevariants.py.

Run: python3 scripts/epub-3.3/package/sec-meta-elem/meta-scheme-no-prefix/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402

SET = "epub-3.3/package/sec-meta-elem/meta-scheme-no-prefix"


def main() -> None:
    info = eb.load_set(
        SET, title='A scheme value with no prefix',
        description="A meta element's scheme attribute is nope, with no prefix. Does a validator reject it?",
        subject="EPUB 3.3 package document")
    files = pv.meta_scheme_no_prefix(epub3.package(info))
    out = eb.write_epub(info.book_dir / "meta-scheme-no-prefix.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
