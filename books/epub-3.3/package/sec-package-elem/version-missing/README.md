# Package without version

- Book: `version-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-package-elem/version-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the package document section
- Issue: [#40](https://github.com/veripublica/epub-test-books/issues/40)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package element has no version attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The attribute is required. A tool may also be unable to tell which EPUB version the book claims. That follows from the same defect.

## Question

The `package` element has no `version` attribute. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-package-elem`](https://www.w3.org/TR/epub-33/#sec-package-elem):

> version [required]

## Expected result

Invalid. The attribute is required. A tool may also be unable to tell which EPUB version the book claims. That follows from the same defect.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i version-missing.epub -u --advisory` | ERROR OPF-001; INVALID | `version-missing.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck version-missing.epub -u` | ERROR OPF-001; INVALID | `version-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the `version` attribute is removed from the `package` element.

## History

- 2026-11-09: First version.
