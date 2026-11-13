# Two complete viewport tags (valid)

- Book: `viewport-two-tags-both-full.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/sec-fxl-icb-html/viewport-two-tags-both-full/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#269](https://github.com/veripublica/epub-test-books/issues/269)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has two viewport meta tags: width=1200, height=600, and after it width=800, height=400. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid. The first tag has both dimensions. The clause says reading systems ignore later tags; it does not forbid them.

## Question

`content.xhtml` has two viewport meta tags, `width=1200, height=600` and then `width=800, height=400`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-fxl-icb-html`](https://www.w3.org/TR/epub-33/#sec-fxl-icb-html):

> The height and width definitions MUST be specified in the first viewport meta tag in document order in the [html] head element. Reading systems will ignore subsequent viewport meta tags.

## Expected result

Valid. The first tag has both dimensions. The clause says reading systems ignore later tags; it does not forbid them.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i viewport-two-tags-both-full.epub -u --advisory` | USAGE HTM_060a; VALID | `viewport-two-tags-both-full.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck viewport-two-tags-both-full.epub -u` | USAGE HTM_060a; VALID | `viewport-two-tags-both-full.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE HTM_060a says the second viewport tag is not checked, because reading systems ignore it. It is at usage level and does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and a second `<meta name="viewport" content="width=800, height=400"/>` after the first in `content.xhtml`.

## History

- 2026-11-11: First version.
