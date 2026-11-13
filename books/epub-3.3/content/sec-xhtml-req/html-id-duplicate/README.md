# Two HTML elements with the same `id`

- Book: `html-id-duplicate.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/html-id-duplicate/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#173](https://github.com/veripublica/epub-test-books/issues/173)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Two elements in the content document have the same id. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. HTML requires each `id` to be unique in the document.

## Question

Two elements in the content document have the same `id`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

## Expected result

Invalid. HTML requires each `id` to be unique in the document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i html-id-duplicate.epub -u --advisory` | ERROR RSC-005, ERROR RSC-005; INVALID | `html-id-duplicate.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck html-id-duplicate.epub -u` | ERROR RSC-005, ERROR RSC-005; INVALID | `html-id-duplicate.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, two `p` elements with `id="same"` are added.

## History

- 2026-11-09: First version.
