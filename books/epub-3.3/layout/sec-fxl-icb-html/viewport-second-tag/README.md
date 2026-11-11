# The dimensions in the second viewport tag

- Book: `viewport-second-tag.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/sec-fxl-icb-html/viewport-second-tag/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#268](https://github.com/veripublica/epub-test-books/issues/268)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The first viewport meta tag of content.xhtml is initial-scale=1.0; a second one, after it, has width=1200, height=600. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. The height and width must be in the first viewport meta tag; later ones are ignored.

## Question

The first viewport meta tag of `content.xhtml` is `initial-scale=1.0`; a second one has `width=1200, height=600`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-fxl-icb-html`](https://www.w3.org/TR/epub-33/#sec-fxl-icb-html):

> The height and width definitions MUST be specified in the first viewport meta tag in document order in the [html] head element. Reading systems will ignore subsequent viewport meta tags.

## Expected result

Invalid. The height and width must be in the first viewport meta tag; later ones are ignored.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i viewport-second-tag.epub -u --advisory` | ERROR HTM_056, ERROR HTM_056, USAGE HTM_060a; INVALID | `viewport-second-tag.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck viewport-second-tag.epub -u` | ERROR HTM_056, ERROR HTM_056, USAGE HTM_060a; INVALID | `viewport-second-tag.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE HTM_060a says the second viewport tag is not checked, because reading systems ignore it. That is the point of the set, not a second defect.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with the viewport in `content.xhtml` set to `content="initial-scale=1.0"`, and a second `<meta name="viewport" content="width=1200, height=600"/>` after it.

## History

- 2026-11-11: First version.
