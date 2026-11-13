# Mimetype is not the first entry

- Book: `mimetype-not-first.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-mime/mimetype-not-first/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#22](https://github.com/veripublica/epub-test-books/issues/22)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The mimetype file is present and correct, but it is the second entry in the ZIP file, after META-INF/container.xml. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The mimetype file must be the first file.

## Question

The mimetype file is present and correct, but it is the second entry in the ZIP file, after `META-INF/container.xml`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-zip-container-mime`](https://www.w3.org/TR/epub-33/#sec-zip-container-mime):

> EPUB creators MUST include the mimetype file as the first file in the OCF ZIP container.

## Expected result

Invalid. The mimetype file must be the first file.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i mimetype-not-first.epub -u --advisory` | ERROR PKG-006; INVALID | `mimetype-not-first.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck mimetype-not-first.epub -u` | ERROR PKG-006; INVALID | `mimetype-not-first.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The first two entries swap places: `META-INF/container.xml`, then `mimetype`.

## History

- 2026-11-08: First version.
