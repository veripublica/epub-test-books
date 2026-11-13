# A `seq` around the `par`, with `epub:textref` and `epub:type` (valid)

- Book: `seq.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-smil-seq-elem/seq/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: In content.smil, the par is inside <seq id="s1" epub:textref="content.xhtml#content" epub:type="chapter">.

Expected result: Valid. A seq may be a child of body, and it has the epub:textref it needs.

## Question

In `content.smil`, the `par` is inside `<seq id="s1" epub:textref="content.xhtml#content" epub:type="chapter">`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-smil-seq-elem`](https://www.w3.org/TR/epub-33/#sec-smil-seq-elem):

> One or more seq elements MAY occur as children of the body element and of the seq element.

EPUB 3.3, [`sec-media-overlays-structure`](https://www.w3.org/TR/epub-33/#sec-media-overlays-structure):

> The seq element MUST contain an epub:textref attribute.

## Expected result

Valid. A `seq` may be a child of `body`, and it has the `epub:textref` it needs.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i seq.epub -u --advisory` | no findings; VALID | `seq.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck seq.epub -u` | no findings; VALID | `seq.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: In `content.smil`, the `par` is inside `<seq id="s1" epub:textref="content.xhtml#content" epub:type="chapter">`.

## History

- 2026-11-12: First version.
