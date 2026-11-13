# A `link` element with text inside

- Book: `link-with-content.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-link-elem/link-with-content/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#218](https://github.com/veripublica/epub-test-books/issues/218)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A link element has text content. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The element must be empty.

## Question

A `link` element has text content. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-link-elem`](https://www.w3.org/TR/epub-33/#sec-link-elem):

> rel [required] Content Model: Empty

## Expected result

Invalid. The element must be empty.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i link-with-content.epub -u --advisory` | ERROR RSC-005; INVALID | `link-with-content.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck link-with-content.epub -u` | ERROR RSC-005; INVALID | `link-with-content.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, a `link` with the text `Text` inside is added to the metadata.

## History

- 2026-11-09: First version.
