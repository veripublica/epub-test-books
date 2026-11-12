# Two `toc` nav elements

- Book: `toc-twice.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-content-req/toc-twice/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#91](https://github.com/veripublica/epub-test-books/issues/91)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The navigation document has two toc nav elements. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Exactly one is allowed.

## Question

The navigation document has two `toc` nav elements. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-content-req`](https://www.w3.org/TR/epub-33/#sec-nav-content-req):

> MUST include exactly one toc nav element as defined in 7.4.2 The toc nav element.

## Expected result

Invalid. Exactly one is allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i toc-twice.epub -u --advisory` | ERROR RSC-005; INVALID | `toc-twice.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck toc-twice.epub -u` | ERROR RSC-005; INVALID | `toc-twice.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, a second `toc` nav is added.

## History

- 2026-11-09: First version.
