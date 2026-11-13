# A media overlay with `version="3.1"`

- Book: `version-wrong.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-smil-smil-elem/version-wrong/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: [#438](https://github.com/veripublica/epub-test-books/issues/438)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: In content.smil, smil has version="3.1".

Expected result: Invalid. The version attribute must be 3.0.

## Question

In `content.smil`, `smil` has `version="3.1"`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-smil-smil-elem`](https://www.w3.org/TR/epub-33/#sec-smil-smil-elem):

> Specifies the version number of the [smil3] specification to which the media overlay document adheres. This attribute MUST have the value "3.0".

## Expected result

Invalid. The `version` attribute must be `3.0`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i version-wrong.epub -u --advisory` | ERROR RSC-005; INVALID | `version-wrong.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck version-wrong.epub -u` | ERROR RSC-005; INVALID | `version-wrong.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: In `content.smil`, `smil` has `version="3.1"`.

## History

- 2026-11-12: First version.
