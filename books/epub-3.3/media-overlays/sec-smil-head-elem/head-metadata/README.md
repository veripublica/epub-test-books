# A media overlay with an empty `head` and `metadata` (valid)

- Book: `head-metadata.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-smil-head-elem/head-metadata/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: [#439](https://github.com/veripublica/epub-test-books/issues/439)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: In content.smil, <head><metadata/></head> comes before body.

Expected result: Valid. head is optional, and metadata may hold zero elements.

## Question

In `content.smil`, `<head><metadata/></head>` comes before `body`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-smil-head-elem`](https://www.w3.org/TR/epub-33/#sec-smil-head-elem):

> As this specification does not define any metadata properties that must occur in the media overlay document, the head element is OPTIONAL.

## Expected result

Valid. `head` is optional, and `metadata` may hold zero elements.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i head-metadata.epub -u --advisory` | no findings; VALID | `head-metadata.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck head-metadata.epub -u` | no findings; VALID | `head-metadata.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: In `content.smil`, `<head><metadata/></head>` comes before `body`.

## History

- 2026-11-12: First version.
