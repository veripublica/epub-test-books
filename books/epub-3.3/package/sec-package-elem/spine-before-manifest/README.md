# `spine` before `manifest`

- Book: `spine-before-manifest.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-package-elem/spine-before-manifest/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#217](https://github.com/veripublica/epub-test-books/issues/217)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The spine element comes before the manifest element. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The order of the children of `package` is fixed.

## Question

The `spine` element comes before the `manifest` element. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-package-elem`](https://www.w3.org/TR/epub-33/#sec-package-elem):

> In this order: metadata [exactly 1] manifest [exactly 1] spine [exactly 1]

## Expected result

Invalid. The order of the children of `package` is fixed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i spine-before-manifest.epub -u --advisory` | ERROR RSC-005, ERROR RSC-005; INVALID | `spine-before-manifest.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck spine-before-manifest.epub -u` | ERROR RSC-005, ERROR OPF-049, ERROR OPF-049, ERROR RSC-005, USAGE OPF-097, USAGE OPF-097, ERROR RSC-011, ERROR RSC-011; INVALID | `spine-before-manifest.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the `spine` element is moved in front of the `manifest` element.

## History

- 2026-11-09: First version.
