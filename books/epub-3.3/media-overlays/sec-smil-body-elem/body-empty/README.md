# A media overlay with an empty `body`

- Book: `body-empty.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-smil-body-elem/body-empty/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: In content.smil, body is empty.

Expected result: Invalid. body must hold at least one par or seq.

## Question

In `content.smil`, `body` is empty. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-smil-body-elem`](https://www.w3.org/TR/epub-33/#sec-smil-body-elem):

> In any order: seq [0 or more] par [0 or more] MUST include at least one par or seq.

## Expected result

Invalid. `body` must hold at least one `par` or `seq`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i body-empty.epub -u --advisory` | ERROR MED_013, USAGE OPF-097; INVALID | `body-empty.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck body-empty.epub -u` | ERROR RSC-005, ERROR MED_013, USAGE OPF-097; INVALID | `body-empty.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: In `content.smil`, `body` is empty.

## History

- 2026-11-12: First version.
