# A `p` inside a `p`

- Book: `html-p-in-p.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/html-p-in-p/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#174](https://github.com/veripublica/epub-test-books/issues/174)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A p element is nested in another p. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The content model of `p` is phrasing content.

## Question

A `p` element is nested in another `p`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

## Expected result

Invalid. The content model of `p` is phrasing content.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i html-p-in-p.epub -u --advisory` | ERROR RSC-005; INVALID | `html-p-in-p.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck html-p-in-p.epub -u` | ERROR RSC-005; INVALID | `html-p-in-p.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a `p` is nested in another `p`.

## History

- 2026-11-09: First version.
