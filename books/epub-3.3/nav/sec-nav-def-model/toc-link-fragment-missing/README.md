# A `toc` link to a fragment that does not exist

- Book: `toc-link-fragment-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/toc-link-fragment-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#99](https://github.com/veripublica/epub-test-books/issues/99)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The toc nav has a link to a fragment that does not exist. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The URL resolves to no fragment of the document.

## Question

The `toc` nav has an `a` element whose fragment names an `id` the document does not have. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> MUST, in the case of the toc nav, landmarks nav and page-list nav, resolve to a top-level content document or fragment therein.

## Expected result

Invalid. The URL resolves to no fragment of the document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i toc-link-fragment-missing.epub -u --advisory` | ERROR RSC-012; INVALID | `toc-link-fragment-missing.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck toc-link-fragment-missing.epub -u` | ERROR RSC-012; INVALID | `toc-link-fragment-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, an entry for `content.xhtml#nope` is added.

## History

- 2026-11-09: First version.
