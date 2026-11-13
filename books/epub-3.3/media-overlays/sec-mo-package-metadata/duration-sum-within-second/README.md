# A total that differs from the sum by less than a second (valid)

- Book: `duration-sum-within-second.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-mo-package-metadata/duration-sum-within-second/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: [#472](https://github.com/veripublica/epub-test-books/issues/472)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: The overlay's duration is 0:00:03 and the total is 0:00:03.900.

Expected result: Valid. The difference, 0.9 seconds, is within one second.

## Question

The overlay's duration is `0:00:03` and the total is `0:00:03.900`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-mo-package-metadata`](https://www.w3.org/TR/epub-33/#sec-mo-package-metadata):

> The sum of the durations for each media overlay document SHOULD equal the total duration plus or minus one second.

## Expected result

Valid. The difference, 0.9 seconds, is within one second.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i duration-sum-within-second.epub -u --advisory` | no findings; VALID | `duration-sum-within-second.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck duration-sum-within-second.epub -u` | no findings; VALID | `duration-sum-within-second.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: The overlay's duration is `0:00:03` and the total is `0:00:03.900`.

## History

- 2026-11-12: First version.
