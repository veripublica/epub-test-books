# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ocf/Section3.5.6/rights-xml-namespaced/rights-xml-namespaced.epub: A META-INF/rights.xml with a namespace-qualified root (valid).

The EPUB 2 template's files are built for this set, then written as a
container by scripts/lib/ocf2variants.py.

Run: python3 scripts/epub-2.0.1/ocf/Section3.5.6/rights-xml-namespaced/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epubbook as eb  # noqa: E402
import ocf2variants as ov2  # noqa: E402

SET = "epub-2.0.1/ocf/Section3.5.6/rights-xml-namespaced"


def main() -> None:
    info = eb.load_set(
        SET, title='A META-INF/rights.xml with a namespace-qualified root (valid)',
        description='The container also holds META-INF/rights.xml, an empty ext:rights element in its own namespace. Does a validator accept the book?',
        subject="EPUB 2.0.1 OCF")
    files = epub2.package(info)
    out = info.book_dir / "rights-xml-namespaced.epub"
    out.write_bytes(ov2.rights_xml_namespaced(files))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
