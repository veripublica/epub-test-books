# A `toc` link to a stylesheet

- Book: `toc-link-css.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/toc-link-css/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#98](https://github.com/veripublica/epub-test-books/issues/98)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The toc nav has a link to a CSS file. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The target is not a top-level content document.

## Question

The `toc` nav has an `a` element pointing to a CSS file in the manifest. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> MUST, in the case of the toc nav, landmarks nav and page-list nav, resolve to a top-level content document or fragment therein.

## Expected result

Invalid. The target is not a top-level content document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i toc-link-css.epub -u --advisory` | ERROR RSC-010, USAGE OPF-097; INVALID | `toc-link-css.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck toc-link-css.epub -u` | USAGE OPF-097, ERROR RSC-010; INVALID | `toc-link-css.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/extra.css` is added to the manifest, and `OEBPS/nav.xhtml` links to it.

## History

- 2026-11-09: First version.
