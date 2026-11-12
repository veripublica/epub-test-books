# Two `par` elements with the same `id`

- Book: `duplicate-id.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-smil-par-elem/duplicate-id/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubveri: missed
- Asked for by: the maintainer, to start the media overlays section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: In content.smil, the par is there twice, both with id="par1".

Expected result: Invalid. An id must be unique within the document.

## Question

In `content.smil`, the `par` is there twice, both with `id="par1"`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-smil-par-elem`](https://www.w3.org/TR/epub-33/#sec-smil-par-elem):

> id [optional] The ID [xml] of the element, which MUST be unique within the document scope.

## Expected result

Invalid. An `id` must be unique within the document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i duplicate-id.epub -u --advisory` | no findings; VALID | `duplicate-id.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck duplicate-id.epub -u` | ERROR RSC-005, ERROR RSC-005; INVALID | `duplicate-id.epubcheck-5.4.0.txt` |

epubcheck agrees with the expected result. epubveri does not: it reports nothing for the repeated `id`.

- **epubveri: missed.** epubveri issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: In `content.smil`, the `par` is there twice, both with `id="par1"`.

## History

- 2026-11-12: First version.
