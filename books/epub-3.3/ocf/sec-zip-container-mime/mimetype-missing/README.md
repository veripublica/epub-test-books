# No mimetype file

- Book: `mimetype-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-mime/mimetype-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#21](https://github.com/veripublica/epub-test-books/issues/21)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container has no mimetype file at all. Everything else is the EPUB 3 template. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The mimetype file is required.

## Question

The container has no mimetype file at all. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-zip-container-mime`](https://www.w3.org/TR/epub-33/#sec-zip-container-mime):

> EPUB creators MUST include the mimetype file as the first file in the OCF ZIP container.

## Expected result

Invalid. The mimetype file is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i mimetype-missing.epub -u --advisory` | ERROR PKG-006; INVALID | `mimetype-missing.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck mimetype-missing.epub -u` | ERROR PKG-006; INVALID | `mimetype-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The template's entries are written without the mimetype entry.

## History

- 2026-11-08: First version.
