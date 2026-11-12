# One manifest item in the spine twice

- Book: `itemref-duplicate.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-itemref-elem/itemref-duplicate/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#83](https://github.com/veripublica/epub-test-books/issues/83)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The spine references the content document twice. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The same `id` is referenced twice.

## Question

The spine references the content document twice. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-itemref-elem`](https://www.w3.org/TR/epub-33/#sec-itemref-elem):

> item element IDs MUST NOT be referenced more than once.

## Expected result

Invalid. The same `id` is referenced twice.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i itemref-duplicate.epub -u --advisory` | ERROR RSC-005; INVALID | `itemref-duplicate.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck itemref-duplicate.epub -u` | ERROR RSC-005; INVALID | `itemref-duplicate.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, a second `<itemref idref="content"/>` is added at the end of the spine.

## History

- 2026-11-09: First version.
