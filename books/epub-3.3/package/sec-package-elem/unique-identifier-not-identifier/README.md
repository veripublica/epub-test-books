# `unique-identifier` pointing to `dc:title`

- Book: `unique-identifier-not-identifier.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-package-elem/unique-identifier-not-identifier/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#52](https://github.com/veripublica/epub-test-books/issues/52)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The unique-identifier attribute names the id of the dc:title element. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The attribute must reference a `dc:identifier` element.

## Question

The `unique-identifier` attribute names the `id` of the `dc:title` element. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-opf-dcidentifier`](https://www.w3.org/TR/epub-33/#sec-opf-dcidentifier):

> This dc:identifier element MUST specify an id attribute whose value is referenced from the package element's unique-identifier attribute.

## Expected result

Invalid. The attribute must reference a `dc:identifier` element.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i unique-identifier-not-identifier.epub -u --advisory` | ERROR RSC-005, ERROR OPF-030; INVALID | `unique-identifier-not-identifier.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck unique-identifier-not-identifier.epub -u` | ERROR RSC-005, ERROR OPF-030; INVALID | `unique-identifier-not-identifier.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `dc:title` gets `id="title"` and `unique-identifier` becomes `title`.

## History

- 2026-11-09: First version.
