# Two media overlay documents for one content document

- Book: `two-overlays-same-document.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-overlay-req/two-overlays-same-document/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: [#437](https://github.com/veripublica/epub-test-books/issues/437)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: A second overlay, content2.smil, is a copy of content.smil with its own manifest item and duration (the total becomes 0:00:06).

Expected result: Invalid. Both overlays reference content.xhtml.

## Question

A second overlay, `content2.smil`, is a copy of `content.smil` with its own manifest item and duration (the total becomes `0:00:06`). Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-overlay-req`](https://www.w3.org/TR/epub-33/#sec-overlay-req):

> MAY refer to more than one EPUB content document, but more than one media overlay document MUST NOT reference the same EPUB content document.

## Expected result

Invalid. Both overlays reference `content.xhtml`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i two-overlays-same-document.epub -u --advisory` | ERROR MED_011, USAGE OPF-097; INVALID | `two-overlays-same-document.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck two-overlays-same-document.epub -u` | ERROR MED_011, USAGE OPF-097; INVALID | `two-overlays-same-document.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: A second overlay, `content2.smil`, is a copy of `content.smil` with its own manifest item and duration (the total becomes `0:00:06`).

## History

- 2026-11-12: First version.
