# A `par` with `audio` and no `text`

- Book: `par-no-text.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-smil-par-elem/par-no-text/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: [#444](https://github.com/veripublica/epub-test-books/issues/444)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: In content.smil, the par holds only the audio element.

Expected result: Invalid. par must hold exactly one text.

## Question

In `content.smil`, the `par` holds only the `audio` element. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-smil-par-elem`](https://www.w3.org/TR/epub-33/#sec-smil-par-elem):

> Content Model: In any order: text [exactly 1] audio [0 or 1]

## Expected result

Invalid. `par` must hold exactly one `text`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i par-no-text.epub -u --advisory` | ERROR MED_013; INVALID | `par-no-text.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck par-no-text.epub -u` | ERROR RSC-005, ERROR MED_013; INVALID | `par-no-text.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: In `content.smil`, the `par` holds only the `audio` element.

## History

- 2026-11-12: First version.
