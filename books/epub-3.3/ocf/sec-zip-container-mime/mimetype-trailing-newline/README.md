# Mimetype ends with a newline

- Book: `mimetype-trailing-newline.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-mime/mimetype-trailing-newline/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#23](https://github.com/veripublica/epub-test-books/issues/23)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The mimetype file holds application/epub+zip followed by a line feed (U+000A). Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A line feed is trailing whitespace.

## Question

The mimetype file holds `application/epub+zip` followed by a line feed. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-zip-container-mime`](https://www.w3.org/TR/epub-33/#sec-zip-container-mime):

> The mimetype file MUST NOT contain any leading or trailing padding or whitespace.

## Expected result

Invalid. A line feed is trailing whitespace.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.37.1 | `epubveri -i mimetype-trailing-newline.epub -u --advisory` | ERROR PKG-007; INVALID | `mimetype-trailing-newline.epubveri-0.37.1.txt` |
| epubcheck 5.4.0 | `epubcheck mimetype-trailing-newline.epub -u` | ERROR PKG-007; INVALID | `mimetype-trailing-newline.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The mimetype entry holds `application/epub+zip\n` (21 bytes), stored, first in the container.

## History

- 2026-11-08: First version.
