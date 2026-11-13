# `media:active-class` with a `refines` attribute

- Book: `active-class-refines.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-docs-assoc-style/active-class-refines/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: [#478](https://github.com/veripublica/epub-test-books/issues/478)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: The package also declares <meta property="media:active-class" refines="#mo">active</meta>, and content.xhtml links style.css, which defines p.active.

Expected result: Invalid. The class properties must not be used with refines.

## Question

The package also declares `<meta property="media:active-class" refines="#mo">active</meta>`, and `content.xhtml` links `style.css`, which defines `p.active`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-docs-assoc-style`](https://www.w3.org/TR/epub-33/#sec-docs-assoc-style):

> EPUB creators MUST NOT use the active-class and playback-active-class properties in conjunction with a refines attribute as they always apply to the entire EPUB publication.

## Expected result

Invalid. The class properties must not be used with `refines`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i active-class-refines.epub -u --advisory` | ERROR RSC-005; INVALID | `active-class-refines.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck active-class-refines.epub -u` | ERROR RSC-005; INVALID | `active-class-refines.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: The package also declares `<meta property="media:active-class" refines="#mo">active</meta>`, and `content.xhtml` links `style.css`, which defines `p.active`.

## History

- 2026-11-12: First version.
