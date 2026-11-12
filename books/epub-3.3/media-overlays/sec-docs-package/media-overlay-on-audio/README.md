# A `media-overlay` attribute on the audio item

- Book: `media-overlay-on-audio.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-docs-package/media-overlay-on-audio/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: The manifest item of audio.mp3 also has media-overlay="mo".

Expected result: Invalid. audio.mp3 is not an EPUB content document.

## Question

The manifest item of `audio.mp3` also has `media-overlay="mo"`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-docs-package`](https://www.w3.org/TR/epub-33/#sec-docs-package):

> EPUB creators MUST only specify the media-overlay attribute on manifest item elements that reference EPUB content documents.

## Expected result

Invalid. `audio.mp3` is not an EPUB content document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i media-overlay-on-audio.epub -u --advisory` | ERROR RSC-005; INVALID | `media-overlay-on-audio.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck media-overlay-on-audio.epub -u` | ERROR RSC-005; INVALID | `media-overlay-on-audio.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: The manifest item of `audio.mp3` also has `media-overlay="mo"`.

## History

- 2026-11-12: First version.
