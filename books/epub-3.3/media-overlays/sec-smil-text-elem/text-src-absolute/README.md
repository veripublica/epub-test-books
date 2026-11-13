# A `text` src that starts with `/`

- Book: `text-src-absolute.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-smil-text-elem/text-src-absolute/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: In content.smil, text has src="/OEBPS/content.xhtml#p1".

Expected result: Invalid. A path-absolute URL is not a path-relative-scheme-less-URL string.

## Question

In `content.smil`, `text` has `src="/OEBPS/content.xhtml#p1"`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-smil-text-elem`](https://www.w3.org/TR/epub-33/#sec-smil-text-elem):

> Refers to the associated EPUB content document and, optionally, identifies a specific part of it. The value MUST be a path-relative-scheme-less-URL string, optionally followed by U+0023 (#) and a URL-fragment string.

## Expected result

Invalid. A path-absolute URL is not a path-relative-scheme-less-URL string.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i text-src-absolute.epub -u --advisory` | ERROR RSC-026; INVALID | `text-src-absolute.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck text-src-absolute.epub -u` | ERROR RSC-026; INVALID | `text-src-absolute.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: In `content.smil`, `text` has `src="/OEBPS/content.xhtml#p1"`.

## History

- 2026-11-12: First version.
