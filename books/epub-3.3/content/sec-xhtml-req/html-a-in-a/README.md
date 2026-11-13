# An `a` inside an `a`

- Book: `html-a-in-a.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/html-a-in-a/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#177](https://github.com/veripublica/epub-test-books/issues/177)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An a element is nested in another a. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. HTML forbids interactive content inside `a`.

## Question

An `a` element is nested in another `a`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

## Expected result

Invalid. HTML forbids interactive content inside `a`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i html-a-in-a.epub -u --advisory` | ERROR RSC-005; INVALID | `html-a-in-a.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck html-a-in-a.epub -u` | ERROR RSC-005; INVALID | `html-a-in-a.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, an `a` is nested in another `a`.

## History

- 2026-11-09: First version.
