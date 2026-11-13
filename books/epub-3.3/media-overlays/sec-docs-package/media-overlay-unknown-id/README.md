# A `media-overlay` attribute naming no manifest item

- Book: `media-overlay-unknown-id.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-docs-package/media-overlay-unknown-id/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: content.xhtml's manifest item has media-overlay="nope".

Expected result: Invalid. nope is not the ID of any manifest item.

## Question

`content.xhtml`'s manifest item has `media-overlay="nope"`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-docs-package`](https://www.w3.org/TR/epub-33/#sec-docs-package):

> If an EPUB content document is wholly or partially referenced by a media overlay document, then its manifest item element MUST specify a media-overlay attribute. The attribute MUST reference the ID [xml] of the manifest item for the corresponding media overlay document.

## Expected result

Invalid. `nope` is not the ID of any manifest item.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i media-overlay-unknown-id.epub -u --advisory` | ERROR RSC-005, ERROR RSC-005, ERROR MED_012, USAGE OPF-097; INVALID | `media-overlay-unknown-id.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck media-overlay-unknown-id.epub -u` | ERROR RSC-005, ERROR RSC-005, ERROR MED_012, USAGE OPF-097; INVALID | `media-overlay-unknown-id.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: `content.xhtml`'s manifest item has `media-overlay="nope"`.

## History

- 2026-11-12: First version.
