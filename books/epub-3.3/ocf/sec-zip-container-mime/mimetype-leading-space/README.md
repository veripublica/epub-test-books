# Mimetype starts with a space

- Book: `mimetype-leading-space.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-mime/mimetype-leading-space/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#20](https://github.com/veripublica/epub-test-books/issues/20)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The mimetype file holds a space (U+0020) and then application/epub+zip. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The space is leading whitespace.

## Question

The mimetype file holds a space and then `application/epub+zip`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-zip-container-mime`](https://www.w3.org/TR/epub-33/#sec-zip-container-mime):

> The mimetype file MUST NOT contain any leading or trailing padding or whitespace.

## Expected result

Invalid. The space is leading whitespace.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i mimetype-leading-space.epub -u --advisory` | ERROR PKG-007; INVALID | `mimetype-leading-space.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck mimetype-leading-space.epub -u` | ERROR PKG-007; INVALID | `mimetype-leading-space.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The mimetype entry holds ` application/epub+zip` (21 bytes), stored, first in the container.

## History

- 2026-11-08: First version.
