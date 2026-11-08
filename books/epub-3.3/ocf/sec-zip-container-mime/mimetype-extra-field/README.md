# Mimetype has an extra field in its ZIP header

- Book: `mimetype-extra-field.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-mime/mimetype-extra-field/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The ZIP local header of the mimetype entry carries an extra field: the 9-byte extended timestamp (0x5455) that many zip tools add by default. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The mimetype entry's header has an extra field, so `application/epub+zip` no longer starts at byte 38 either.

## Question

The mimetype entry's local header carries an extra field, the extended timestamp many zip tools add. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-zip-container-mime`](https://www.w3.org/TR/epub-33/#sec-zip-container-mime):

> EPUB creators MUST NOT include an extra field in its ZIP header.

## Expected result

Invalid. The mimetype entry's header has an extra field, so `application/epub+zip` no longer starts at byte 38 either.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.37.1 | `epubveri -i mimetype-extra-field.epub -u --advisory` | ERROR PKG-005; INVALID | `mimetype-extra-field.epubveri-0.37.1.txt` |
| epubcheck 5.4.0 | `epubcheck mimetype-extra-field.epub -u` | ERROR PKG-005; INVALID | `mimetype-extra-field.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The mimetype entry's local header gets a 9-byte extended-timestamp extra field (`0x5455`, length 5, flags 1, time 0).

## History

- 2026-11-08: First version.
