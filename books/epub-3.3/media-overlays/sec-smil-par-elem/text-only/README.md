# A `par` with `text` and no `audio` (valid)

- Book: `text-only.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-smil-par-elem/text-only/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: [#443](https://github.com/veripublica/epub-test-books/issues/443)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: In content.smil, the par holds only <text src="content.xhtml#p1"/>, and the book has no audio file.

Expected result: Valid. audio is optional in par (0 or 1).

## Question

In `content.smil`, the `par` holds only `<text src="content.xhtml#p1"/>`, and the book has no audio file. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-smil-par-elem`](https://www.w3.org/TR/epub-33/#sec-smil-par-elem):

> Content Model: In any order: text [exactly 1] audio [0 or 1]

## Expected result

Valid. `audio` is optional in `par` (0 or 1).

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i text-only.epub -u --advisory` | no findings; VALID | `text-only.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck text-only.epub -u` | no findings; VALID | `text-only.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: In `content.smil`, the `par` holds only `<text src="content.xhtml#p1"/>`, and the book has no audio file.

## History

- 2026-11-12: First version.
