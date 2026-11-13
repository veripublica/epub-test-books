# `media:active-class` given as a selector, `.active`

- Book: `active-class-selector.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-docs-assoc-style/active-class-selector/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer; parked on 2026-11-12 while both verifiers missed it, shipped after epubveri 0.42.0 reports it
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: The package also declares media:active-class as .active, and content.xhtml links style.css, which defines p.active.

Expected result: Invalid. The property must hold a class name, not a selector.

## Question

The package also declares `media:active-class` as `.active`, and `content.xhtml` links `style.css`, which defines `p.active`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-docs-assoc-style`](https://www.w3.org/TR/epub-33/#sec-docs-assoc-style):

> Each property MUST define a valid CSS class name not including any selectors [css2].

## Expected result

Invalid. The property must hold a class name, not a selector.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i active-class-selector.epub -u --advisory` | ERROR RSC-005; INVALID | `active-class-selector.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck active-class-selector.epub -u` | no findings; VALID | `active-class-selector.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: The package also declares `media:active-class` as `.active`, and `content.xhtml` links `style.css`, which defines `p.active`.

## History

- 2026-11-13: First version.
