# A nested `toc` (valid)

- Book: `toc-nested.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/toc-nested/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#112](https://github.com/veripublica/epub-test-books/issues/112)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The toc nav has an ol nested after a link. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The nesting is allowed.

## Question

The `toc` nav has an `ol` nested after an `a`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> An ol (ordered list) element representing a subsidiary content level (e.g., all the subsection headings of a section) MAY follow an a element.

## Expected result

Valid. The nesting is allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i toc-nested.epub -u --advisory` | no findings; VALID | `toc-nested.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck toc-nested.epub -u` | no findings; VALID | `toc-nested.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, a nested `ol` follows the content document's link.

## History

- 2026-11-09: First version.
