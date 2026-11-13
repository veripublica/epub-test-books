# A nested navigation link with no text

- Book: `sublist-no-label.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/sublist-no-label/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#106](https://github.com/veripublica/epub-test-books/issues/106)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A nested list item in the toc nav has a link with no content. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A sublist follows the same rules as the primary list.

## Question

A nested list item in the `toc` nav has an `a` with no content. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> Regardless of whether an a or span element precedes it, every sublist MUST adhere to the content requirements defined in this section for constructing the primary navigation list.

> The child a or span element MUST provide a non-zero-length text label after concatenation of all child content and application of whitespace normalization rules.

## Expected result

Invalid. A sublist follows the same rules as the primary list.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i sublist-no-label.epub -u --advisory` | ERROR RSC-005; INVALID | `sublist-no-label.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck sublist-no-label.epub -u` | ERROR RSC-005; INVALID | `sublist-no-label.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, a nested `ol` with an empty `a` follows the content document's link.

## History

- 2026-11-09: First version.
