# A `toc` link outside the container

- Book: `toc-link-external.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/toc-link-external/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#97](https://github.com/veripublica/epub-test-books/issues/97)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The toc nav has a link to a web address. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The target is not a top-level content document.

## Question

The `toc` nav has an `a` element with an `https` URL. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> MUST, in the case of the toc nav, landmarks nav and page-list nav, resolve to a top-level content document or fragment therein.

## Expected result

Invalid. The target is not a top-level content document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i toc-link-external.epub -u --advisory` | ERROR NAV-010; INVALID | `toc-link-external.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck toc-link-external.epub -u` | ERROR NAV-010; INVALID | `toc-link-external.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, an entry with an `https` URL is added to the `toc` nav.

## History

- 2026-11-09: First version.
