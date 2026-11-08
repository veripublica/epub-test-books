# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-encryption.xml-encryption/encryption-wrong-root/encryption-wrong-root.epub: encryption.xml with the wrong root element.

Written as a container by scripts/lib/ocfvariants.py `encryption_wrong_root()`.

Run: python3 scripts/epub-3.3/ocf/sec-encryption.xml-encryption/encryption-wrong-root/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-encryption.xml-encryption/encryption-wrong-root"


def main() -> None:
    info = eb.load_set(
        SET, title='encryption.xml with the wrong root element',
        description='The root element of META-INF/encryption.xml is encryptions instead of encryption. Does a validator reject it?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "encryption-wrong-root.epub"
    out.write_bytes(ov.encryption_wrong_root(info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
