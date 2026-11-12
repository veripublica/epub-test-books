# An empty nested `ol`

- Book: `sublist-empty.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/sublist-empty/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#105](https://github.com/veripublica/epub-test-books/issues/105)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A list item in the toc nav has a nested ol with no li. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A sublist follows the same rules as the primary list.

## Question

A list item in the `toc` nav has a nested `ol` with no `li`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> Regardless of whether an a or span element precedes it, every sublist MUST adhere to the content requirements defined in this section for constructing the primary navigation list.

> ol In this order: li [1 or more]

## Expected result

Invalid. A sublist follows the same rules as the primary list.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i sublist-empty.epub -u --advisory` | ERROR RSC-005; INVALID | `sublist-empty.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck sublist-empty.epub -u` | ERROR RSC-005; INVALID | `sublist-empty.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, an empty `ol` follows the content document's link.

## History

- 2026-11-09: First version.
