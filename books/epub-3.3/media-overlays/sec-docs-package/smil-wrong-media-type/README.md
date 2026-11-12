# A media overlay item with media type `application/xml`

- Book: `smil-wrong-media-type.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-docs-package/smil-wrong-media-type/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: content.smil's manifest item has media-type="application/xml".

Expected result: Invalid. A media overlay's item must have the media type application/smil+xml.

## Question

`content.smil`'s manifest item has `media-type="application/xml"`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-docs-package`](https://www.w3.org/TR/epub-33/#sec-docs-package):

> Manifest items for media overlay documents MUST have the media type application/smil+xml.

## Expected result

Invalid. A media overlay's item must have the media type `application/smil+xml`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i smil-wrong-media-type.epub -u --advisory` | ERROR RSC-005, ERROR MED_013, USAGE OPF-097; INVALID | `smil-wrong-media-type.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck smil-wrong-media-type.epub -u` | ERROR RSC-005, ERROR MED_013, USAGE OPF-097; INVALID | `smil-wrong-media-type.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: `content.smil`'s manifest item has `media-type="application/xml"`.

## History

- 2026-11-12: First version.
