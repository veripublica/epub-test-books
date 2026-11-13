# An `img` element inside a media overlay `par`

- Book: `unknown-element.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-overlay-req/unknown-element/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: In content.smil, the par also holds <img src="x"/>.

Expected result: Invalid. The schema allows only text and audio in par, and img is not an element of the media overlays schema.

## Question

In `content.smil`, the `par` also holds `<img src="x"/>`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-overlay-req`](https://www.w3.org/TR/epub-33/#sec-overlay-req):

> MUST be valid to the media overlays schema as defined in G.3 Media overlays schema and conform to all content conformance constraints expressed in 9.2.2 Media overlay document definition.

EPUB 3.3, [`sec-smil-par-elem`](https://www.w3.org/TR/epub-33/#sec-smil-par-elem):

> Content Model: In any order: text [exactly 1] audio [0 or 1]

## Expected result

Invalid. The schema allows only `text` and `audio` in `par`, and `img` is not an element of the media overlays schema.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i unknown-element.epub -u --advisory` | ERROR RSC-005; INVALID | `unknown-element.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck unknown-element.epub -u` | ERROR RSC-005; INVALID | `unknown-element.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: In `content.smil`, the `par` also holds `<img src="x"/>`.

## History

- 2026-11-12: First version.
