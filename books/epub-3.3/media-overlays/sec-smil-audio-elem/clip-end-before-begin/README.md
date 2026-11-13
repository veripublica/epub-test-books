# `clipEnd` before `clipBegin`

- Book: `clip-end-before-begin.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-smil-audio-elem/clip-end-before-begin/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: [#452](https://github.com/veripublica/epub-test-books/issues/452)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: In content.smil, audio has clipBegin="0:00:02" clipEnd="0:00:01".

Expected result: Invalid. clipEnd must be after clipBegin.

## Question

In `content.smil`, `audio` has `clipBegin="0:00:02" clipEnd="0:00:01"`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-smil-audio-elem`](https://www.w3.org/TR/epub-33/#sec-smil-audio-elem):

> clipBegin [optional] A clock value that specifies the offset into the physical media corresponding to the start point of an audio clip.

> The chronological offset of the terminating position MUST be after the starting offset specified in the clipBegin attribute.

## Expected result

Invalid. `clipEnd` must be after `clipBegin`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i clip-end-before-begin.epub -u --advisory` | ERROR MED-008; INVALID | `clip-end-before-begin.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck clip-end-before-begin.epub -u` | ERROR MED-008; INVALID | `clip-end-before-begin.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: In `content.smil`, `audio` has `clipBegin="0:00:02" clipEnd="0:00:01"`.

## History

- 2026-11-12: First version.
