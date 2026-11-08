# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-font-obfuscation/font-obfuscated/font-obfuscated.epub: An obfuscated font, done right.

Written as a container by scripts/lib/ocfvariants.py `font_obfuscated()`.

Run: python3 scripts/epub-3.3/ocf/sec-font-obfuscation/font-obfuscated/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-font-obfuscation/font-obfuscated"


def main() -> None:
    info = eb.load_set(
        SET, title='An obfuscated font, done right',
        description='The book embeds a font obfuscated with the EPUB algorithm and lists it in META-INF/encryption.xml. Does a validator accept it?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "font-obfuscated.epub"
    out.write_bytes(ov.font_obfuscated(info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
