# Package version="3.1"

- Book: `package-version-wrong.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-package-elem/package-version-wrong/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the package document section
- Issue: [#214](https://github.com/veripublica/epub-test-books/issues/214)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package element has version="3.1" instead of "3.0". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The only allowed value for EPUB 3 is `3.0`, whichever 3.X specification the book follows.

## Question

The `package` element says `version="3.1"`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-package-elem`](https://www.w3.org/TR/epub-33/#sec-package-elem):

> The attribute MUST have the value "3.0" to indicate conformance with EPUB 3.

> Updates to this specification do not represent new versions of EPUB 3

## Expected result

Invalid. The only allowed value for EPUB 3 is `3.0`, whichever 3.X specification the book follows.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i package-version-wrong.epub -u --advisory` | ERROR OPF-001; INVALID | `package-version-wrong.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck package-version-wrong.epub -u` | ERROR OPF-001; INVALID | `package-version-wrong.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `version="3.0"` on the `package` element becomes `version="3.1"`.

## History

- 2026-11-09: First version.
