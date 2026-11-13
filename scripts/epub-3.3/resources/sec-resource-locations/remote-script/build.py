# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/resources/sec-resource-locations/remote-script/remote-script.epub: A script outside the container.

The EPUB 3 template's files, changed by scripts/lib/scriptvariants.py `remote_script()`.

Run: python3 scripts/epub-3.3/resources/sec-resource-locations/remote-script/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import scriptvariants as sv  # noqa: E402

SET = "epub-3.3/resources/sec-resource-locations/remote-script"


def main() -> None:
    info = eb.load_set(
        SET, title='A script outside the container',
        description='content.xhtml loads a script from an https URL. Does a validator reject it?',
        subject="EPUB 3.3 scripting")
    out = eb.write_epub(info.book_dir / "remote-script.epub", sv.remote_script(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
