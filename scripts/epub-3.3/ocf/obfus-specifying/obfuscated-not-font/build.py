# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/obfus-specifying/obfuscated-not-font/obfuscated-not-font.epub: A stylesheet obfuscated as if it were a font.

Written as a container by scripts/lib/ocfvariants.py `obfuscated_not_font()`.

Run: python3 scripts/epub-3.3/ocf/obfus-specifying/obfuscated-not-font/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/obfus-specifying/obfuscated-not-font"


def main() -> None:
    info = eb.load_set(
        SET, title='A stylesheet obfuscated as if it were a font',
        description='META-INF/encryption.xml lists a stylesheet as obfuscated with the font algorithm. Does a validator reject it?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "obfuscated-not-font.epub"
    out.write_bytes(ov.obfuscated_not_font(info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
