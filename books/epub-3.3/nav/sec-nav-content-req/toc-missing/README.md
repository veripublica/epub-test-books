# No `toc` nav

- Book: `toc-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-content-req/toc-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#90](https://github.com/veripublica/epub-test-books/issues/90)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The navigation document has no toc nav element: its only nav element has epub:type="lot". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Exactly one is required.

## Question

The navigation document has no `toc` nav element. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-content-req`](https://www.w3.org/TR/epub-33/#sec-nav-content-req):

> MUST include exactly one toc nav element as defined in 7.4.2 The toc nav element.

## Expected result

Invalid. Exactly one is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i toc-missing.epub -u --advisory` | ERROR RSC-005; INVALID | `toc-missing.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck toc-missing.epub -u` | ERROR RSC-005; INVALID | `toc-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, the `nav` element's `epub:type` becomes `lot`.

## History

- 2026-11-09: First version.
