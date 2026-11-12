# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/media-overlays/sec-smil-text-elem/text-src-no-fragment/text-src-no-fragment.epub: A text src with no fragment (valid).

The EPUB 3 template with one media overlay (content.smil and a silent MP3
from scripts/lib/minimedia.py), and the change for this set.

Run: python3 scripts/epub-3.3/media-overlays/sec-smil-text-elem/text-src-no-fragment/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import minimedia  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/media-overlays/sec-smil-text-elem/text-src-no-fragment"
SMIL = '<?xml version="1.0" encoding="UTF-8"?>\n<smil xmlns="http://www.w3.org/ns/SMIL" xmlns:epub="http://www.idpf.org/2007/ops" version="3.0">\n  <body>\n    <par id="par1"><text src="content.xhtml"/><audio src="audio.mp3" clipBegin="0:00:00" clipEnd="0:00:03"/></par>\n  </body>\n</smil>\n'
META = '<meta property="media:duration" refines="#mo">0:00:03</meta>\n    <meta property="media:duration">0:00:03</meta>'
MEDIA_OVERLAY = ' media-overlay="mo"'
SMIL_TYPE = 'application/smil+xml'
AUDIO = 'mp3'  # "mp3", "wav" or None
CSS = None
SECOND_OVERLAY = False
OPF_EDITS = []
CONTENT_ITEM = '<item id="content" href="content.xhtml" media-type="application/xhtml+xml"/>'


def main() -> None:
    info = eb.load_set(
        SET, title='A text src with no fragment (valid)',
        description='In content.smil, text has src="content.xhtml", with no #p1. Does a validator accept the book?',
        subject="EPUB 3.3 media overlays")
    content = epub3.xhtml("Content", pv.section('    <p id="p1">Content.</p>'))
    extra = [("mo", "content.smil", SMIL_TYPE, "", SMIL.encode("utf-8"))]
    if SECOND_OVERLAY:
        extra.append(("mo2", "content2.smil", "application/smil+xml", "", SMIL.encode("utf-8")))
    if AUDIO == "mp3":
        extra.append(("audio", "audio.mp3", "audio/mpeg", "", minimedia.silent_mp3()))
    elif AUDIO == "wav":
        extra.append(("audio", "audio.wav", "audio/wav", "", minimedia.silent_wav()))
    if CSS is not None:
        content = rv.head_link(content, "style.css")
        extra.append(("style", "style.css", "text/css", "", CSS.encode("utf-8")))
    files = []
    for name, data in epub3.package(info, content=content, extra=extra):
        if name == "OEBPS/package.opf":
            data = rv.swap(data, CONTENT_ITEM, CONTENT_ITEM.replace("/>", MEDIA_OVERLAY + "/>"))
            if META:
                data = rv.swap(data, "  </metadata>", "    " + META + "\n  </metadata>")
            for old, new in OPF_EDITS:
                data = rv.swap(data, old, new)
        files.append((name, data))
    out = eb.write_epub(info.book_dir / "text-src-no-fragment.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
