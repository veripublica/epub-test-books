# An `audio` with neither `clipBegin` nor `clipEnd` (valid)

- Book: `clip-none.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-smil-audio-elem/clip-none/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: [#454](https://github.com/veripublica/epub-test-books/issues/454)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: In content.smil, audio has only src.

Expected result: Valid. Both attributes are optional.

## Question

In `content.smil`, `audio` has only `src`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-smil-audio-elem`](https://www.w3.org/TR/epub-33/#sec-smil-audio-elem):

> clipBegin [optional] A clock value that specifies the offset into the physical media corresponding to the start point of an audio clip.

> The chronological offset of the terminating position MUST be after the starting offset specified in the clipBegin attribute.

## Expected result

Valid. Both attributes are optional.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i clip-none.epub -u --advisory` | no findings; VALID | `clip-none.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck clip-none.epub -u` | no findings; VALID | `clip-none.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: In `content.smil`, `audio` has only `src`.

## History

- 2026-11-12: First version.
