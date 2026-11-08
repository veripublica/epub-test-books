# Mimetype starts with a byte order mark

- Book: `mimetype-bom.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-mime/mimetype-bom/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#18](https://github.com/veripublica/epub-test-books/issues/18)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The mimetype file starts with the UTF-8 byte order mark (EF BB BF), then application/epub+zip. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The file begins with U+FEFF.

## Question

The mimetype file starts with the UTF-8 byte order mark, then `application/epub+zip`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-zip-container-mime`](https://www.w3.org/TR/epub-33/#sec-zip-container-mime):

> The mimetype file MUST NOT begin with the Unicode byte order mark U+FEFF.

## Expected result

Invalid. The file begins with U+FEFF.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i mimetype-bom.epub -u --advisory` | ERROR PKG-007; INVALID | `mimetype-bom.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck mimetype-bom.epub -u` | ERROR PKG-007; INVALID | `mimetype-bom.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The mimetype entry holds `EF BB BF` and then `application/epub+zip` (23 bytes), stored, first in the container.

## History

- 2026-11-08: First version.
