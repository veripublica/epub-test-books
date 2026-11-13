# Two elements with the same `id`

- Book: `id-duplicate.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/attrdef-id/id-duplicate/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#63](https://github.com/veripublica/epub-test-books/issues/63)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Two meta elements have the same id. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The `id` is not unique.

## Question

Two `meta` elements in the package document have the same `id`. Does a validator reject it?

## Clause

EPUB 3.3, [`attrdef-id`](https://www.w3.org/TR/epub-33/#attrdef-id):

> The ID [xml] of the element, which MUST be unique within the document scope.

## Expected result

Invalid. The `id` is not unique.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i id-duplicate.epub -u --advisory` | ERROR RSC-005, ERROR RSC-005; INVALID | `id-duplicate.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck id-duplicate.epub -u` | ERROR RSC-005, ERROR RSC-005; INVALID | `id-duplicate.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, a `meta` with `id="collection"` is added, the id the template already uses.

## History

- 2026-11-09: First version.
