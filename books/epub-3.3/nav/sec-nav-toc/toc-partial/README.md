# A `toc` that omits a spine item (valid)

- Book: `toc-partial.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-toc/toc-partial/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#121](https://github.com/veripublica/epub-test-books/issues/121)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The toc nav links to only one of the two documents in the spine. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. No rule requires the `toc` to list every spine item.

## Question

The `toc` nav links to only one of the two spine documents. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> MUST, in the case of the toc nav, landmarks nav and page-list nav, resolve to a top-level content document or fragment therein.

## Expected result

Valid. No rule requires the `toc` to list every spine item.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i toc-partial.epub -u --advisory` | no findings; VALID | `toc-partial.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck toc-partial.epub -u` | no findings; VALID | `toc-partial.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, the content document's entry is removed.

## History

- 2026-11-09: First version.
