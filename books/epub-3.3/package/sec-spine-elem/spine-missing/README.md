# No `spine`

- Book: `spine-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-spine-elem/spine-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#78](https://github.com/veripublica/epub-test-books/issues/78)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package document has no spine element. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The element is required. The documents the navigation document links to are then not in a spine. That follows from the same defect.

## Question

The package document has no `spine` element. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-spine-elem`](https://www.w3.org/TR/epub-33/#sec-spine-elem):

> REQUIRED third child of package, following manifest.

## Expected result

Invalid. The element is required. The documents the navigation document links to are then not in a spine. That follows from the same defect.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i spine-missing.epub -u --advisory` | ERROR RSC-005, ERROR RSC-011, ERROR RSC-011, USAGE OPF-097, USAGE OPF-097; INVALID | `spine-missing.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck spine-missing.epub -u` | ERROR RSC-005, USAGE OPF-097, USAGE OPF-097, ERROR RSC-011, ERROR RSC-011; INVALID | `spine-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

The RSC-011 errors are the consequence the expected result names. USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the `spine` element is removed.

## History

- 2026-11-09: First version.
