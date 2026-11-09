# Package without unique-identifier

- Book: `unique-identifier-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-package-elem/unique-identifier-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the package document section
- Issue: [#39](https://github.com/veripublica/epub-test-books/issues/39)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package element has no unique-identifier attribute. The dc:identifier element is still there. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The attribute is required.

## Question

The `package` element has no `unique-identifier` attribute. The `dc:identifier` element is still there. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-package-elem`](https://www.w3.org/TR/epub-33/#sec-package-elem):

> unique-identifier [required]

## Expected result

Invalid. The attribute is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i unique-identifier-missing.epub -u --advisory` | ERROR RSC-005, ERROR OPF-048, ERROR OPF-030; INVALID | `unique-identifier-missing.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck unique-identifier-missing.epub -u` | ERROR RSC-005, ERROR OPF-048, ERROR OPF-030; INVALID | `unique-identifier-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

All three errors are about the missing attribute.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the `unique-identifier` attribute is removed from the `package` element.

## History

- 2026-11-09: First version.
