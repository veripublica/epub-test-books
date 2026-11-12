# Two `media:active-class` declarations

- Book: `active-class-twice.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-docs-assoc-style/active-class-twice/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: The package declares media:active-class twice, as active and as playing, and content.xhtml links style.css, which defines both.

Expected result: Invalid. active-class may occur at most once.

## Question

The package declares `media:active-class` twice, as `active` and as `playing`, and `content.xhtml` links `style.css`, which defines both. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-active-class`](https://www.w3.org/TR/epub-33/#sec-active-class):

> Name: active-class Description: EPUB creator -defined CSS class name to apply to the currently playing EPUB content document element. Allowed value(s): xsd:string Cardinality: Zero or one

## Expected result

Invalid. `active-class` may occur at most once.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i active-class-twice.epub -u --advisory` | ERROR RSC-005; INVALID | `active-class-twice.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck active-class-twice.epub -u` | ERROR RSC-005; INVALID | `active-class-twice.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: The package declares `media:active-class` twice, as `active` and as `playing`, and `content.xhtml` links `style.css`, which defines both.

## History

- 2026-11-12: First version.
