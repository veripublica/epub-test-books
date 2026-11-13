# Two total `media:duration` declarations

- Book: `duration-total-twice.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-mo-package-metadata/duration-total-twice/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer; parked on 2026-11-12 while both verifiers missed it, shipped after epubveri 0.42.0 reports it
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: The package gives the total media:duration twice, both 0:00:03.

Expected result: Invalid. The total duration may be given exactly once.

## Question

The package gives the total `media:duration` twice, both `0:00:03`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-duration`](https://www.w3.org/TR/epub-33/#sec-duration):

> Cardinality: Exactly one for the EPUB publication and for each media overlay document.

EPUB 3.3, [`sec-property-field-definitions`](https://www.w3.org/TR/epub-33/#sec-property-field-definitions):

> Cardinality Specifies the number of times EPUB creators MAY specify the property, whether globally or attached to another element or property.

## Expected result

Invalid. The total duration may be given exactly once.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i duration-total-twice.epub -u --advisory` | ERROR RSC-005; INVALID | `duration-total-twice.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck duration-total-twice.epub -u` | no findings; VALID | `duration-total-twice.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: The package gives the total `media:duration` twice, both `0:00:03`.

## History

- 2026-11-13: First version.
