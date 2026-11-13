# `unique-identifier` naming no element

- Book: `unique-identifier-unknown.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-package-elem/unique-identifier-unknown/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#51](https://github.com/veripublica/epub-test-books/issues/51)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The unique-identifier attribute names an id that no element has. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The identifier's `id` is not the value the attribute references.

## Question

The `unique-identifier` attribute names an `id` that no element has. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-opf-dcidentifier`](https://www.w3.org/TR/epub-33/#sec-opf-dcidentifier):

> This dc:identifier element MUST specify an id attribute whose value is referenced from the package element's unique-identifier attribute.

## Expected result

Invalid. The identifier's `id` is not the value the attribute references.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i unique-identifier-unknown.epub -u --advisory` | ERROR RSC-005, ERROR OPF-030; INVALID | `unique-identifier-unknown.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck unique-identifier-unknown.epub -u` | ERROR RSC-005, ERROR OPF-030; INVALID | `unique-identifier-unknown.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `unique-identifier="uid"` becomes `unique-identifier="nope"`.

## History

- 2026-11-09: First version.
