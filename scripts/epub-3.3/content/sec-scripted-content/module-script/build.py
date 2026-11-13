# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-scripted-content/module-script/module-script.epub: A module script, with the scripted property (valid).

The EPUB 3 template's files, changed by scripts/lib/scriptvariants.py `module_script()`.

Run: python3 scripts/epub-3.3/content/sec-scripted-content/module-script/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import scriptvariants as sv  # noqa: E402

SET = "epub-3.3/content/sec-scripted-content/module-script"


def main() -> None:
    info = eb.load_set(
        SET, title='A module script, with the scripted property (valid)',
        description='content.xhtml has <script type="module"> and the scripted property. Does a validator accept the book?',
        subject="EPUB 3.3 scripting")
    out = eb.write_epub(info.book_dir / "module-script.epub", sv.module_script(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
