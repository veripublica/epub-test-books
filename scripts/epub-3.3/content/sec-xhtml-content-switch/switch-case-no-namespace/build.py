# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-xhtml-content-switch/switch-case-no-namespace/switch-case-no-namespace.epub: An epub:case without required-namespace.

The EPUB 3 template's files, changed by scripts/lib/xhtmlextvariants.py `switch_case_no_namespace()`.

Run: python3 scripts/epub-3.3/content/sec-xhtml-content-switch/switch-case-no-namespace/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import xhtmlextvariants as xv  # noqa: E402

SET = "epub-3.3/content/sec-xhtml-content-switch/switch-case-no-namespace"


def main() -> None:
    info = eb.load_set(
        SET, title='An epub:case without required-namespace',
        description='content.xhtml has an epub:case without required-namespace. Does a validator reject it?',
        subject="EPUB 3.3 content documents")
    out = eb.write_epub(info.book_dir / "switch-case-no-namespace.epub", xv.switch_case_no_namespace(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
