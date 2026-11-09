# A navigation link with no text

- Book: `label-empty.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/label-empty/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#92](https://github.com/veripublica/epub-test-books/issues/92)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

One link in the toc nav has no content. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The label has zero length.

## Question

An `a` element in the `toc` nav has no content. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> The child a or span element MUST provide a non-zero-length text label after concatenation of all child content and application of whitespace normalization rules.

## Expected result

Invalid. The label has zero length.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i label-empty.epub -u --advisory` | ERROR RSC-005; INVALID | `label-empty.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck label-empty.epub -u` | ERROR RSC-005; INVALID | `label-empty.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, the text of the content document's link is removed.

## History

- 2026-11-09: First version.
