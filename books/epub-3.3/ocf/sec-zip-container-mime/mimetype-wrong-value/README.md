# Mimetype holds the wrong media type

- Book: `mimetype-wrong-value.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-mime/mimetype-wrong-value/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#24](https://github.com/veripublica/epub-test-books/issues/24)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The mimetype file holds application/zip instead of application/epub+zip. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The mimetype file must hold exactly `application/epub+zip`.

## Question

The mimetype file holds `application/zip` instead of `application/epub+zip`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-zip-container-mime`](https://www.w3.org/TR/epub-33/#sec-zip-container-mime):

> The contents of the mimetype file MUST be the MIME media type [rfc2046] string application/epub+zip encoded in US-ASCII [us-ascii].

## Expected result

Invalid. The mimetype file must hold exactly `application/epub+zip`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.37.1 | `epubveri -i mimetype-wrong-value.epub -u --advisory` | ERROR PKG-007; INVALID | `mimetype-wrong-value.epubveri-0.37.1.txt` |
| epubcheck 5.4.0 | `epubcheck mimetype-wrong-value.epub -u` | ERROR PKG-007; INVALID | `mimetype-wrong-value.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The mimetype entry holds the 15 bytes `application/zip`, stored, first in the container.

## History

- 2026-11-08: First version.
