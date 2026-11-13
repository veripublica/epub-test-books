# `media:active-class` with two class names

- Book: `active-class-two-names.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-docs-assoc-style/active-class-two-names/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: The package also declares media:active-class as active playing, and content.xhtml links style.css, which defines both classes.

Expected result: Invalid. Each property must define exactly one class name.

## Question

The package also declares `media:active-class` as `active playing`, and `content.xhtml` links `style.css`, which defines both classes. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-docs-assoc-style`](https://www.w3.org/TR/epub-33/#sec-docs-assoc-style):

> When used, EPUB creators MUST declare the class names in the package document using the active-class and playback-active-class properties.

> EPUB creators MUST define exactly one CSS class name in each property they define.

## Expected result

Invalid. Each property must define exactly one class name.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i active-class-two-names.epub -u --advisory` | ERROR RSC-005; INVALID | `active-class-two-names.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck active-class-two-names.epub -u` | ERROR RSC-005; INVALID | `active-class-two-names.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: The package also declares `media:active-class` as `active playing`, and `content.xhtml` links `style.css`, which defines both classes.

## History

- 2026-11-12: First version.
