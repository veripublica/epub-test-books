# An empty `spine`

- Book: `spine-empty.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-spine-elem/spine-empty/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#79](https://github.com/veripublica/epub-test-books/issues/79)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The spine element has no itemref. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The spine specifies nothing. The documents the navigation document links to are then not in the spine. That follows from the same defect.

## Question

The `spine` element has no `itemref`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-spine-elem`](https://www.w3.org/TR/epub-33/#sec-spine-elem):

> The spine MUST specify at least one EPUB content document or foreign content document.

## Expected result

Invalid. The spine specifies nothing. The documents the navigation document links to are then not in the spine. That follows from the same defect.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i spine-empty.epub -u --advisory` | ERROR RSC-005, ERROR RSC-011, ERROR RSC-011, USAGE OPF-097, USAGE OPF-097; INVALID | `spine-empty.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck spine-empty.epub -u` | ERROR RSC-005, USAGE OPF-097, USAGE OPF-097, ERROR RSC-011, ERROR RSC-011; INVALID | `spine-empty.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

The RSC-011 errors are the consequence the expected result names. USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, every `itemref` is removed.

## History

- 2026-11-09: First version.
