# No total `media:duration`

- Book: `duration-total-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-mo-package-metadata/duration-total-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: The package has the overlay's media:duration but not the total.

Expected result: Invalid. The duration of the whole publication is required.

## Question

The package has the overlay's `media:duration` but not the total. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-mo-package-metadata`](https://www.w3.org/TR/epub-33/#sec-mo-package-metadata):

> EPUB creators MUST specify the duration of the entire EPUB publication in the package document using a meta element with the duration property. In addition, EPUB creators MUST provide the duration of each media overlay document. EPUB creators MUST use the refines attribute to associate each duration declaration to the corresponding manifest item.

## Expected result

Invalid. The duration of the whole publication is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i duration-total-missing.epub -u --advisory` | ERROR RSC-005; INVALID | `duration-total-missing.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck duration-total-missing.epub -u` | ERROR RSC-005; INVALID | `duration-total-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: The package has the overlay's `media:duration` but not the total.

## History

- 2026-11-12: First version.
