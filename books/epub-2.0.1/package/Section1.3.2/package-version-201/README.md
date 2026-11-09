# `version="2.0.1"` on `package`

- Book: `package-version-201.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section1.3.2/package-version-201/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#224](https://github.com/veripublica/epub-test-books/issues/224)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package element says version="2.0.1". Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The value must be `2.0`, even though the specification is numbered 2.0.1.

## Question

The `package` element says `version="2.0.1"`. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section1.3.2`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section1.3.2):

> to be processed as an OPF 2.0 package, a version attribute with a value of 2.0 must be specified on the package element.

## Expected result

Invalid. The value must be `2.0`, even though the specification is numbered 2.0.1.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i package-version-201.epub -u --advisory` | ERROR OPF-001; INVALID | `package-version-201.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck package-version-201.epub -u` | ERROR OPF-001; INVALID | `package-version-201.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `version="2.0"` becomes `version="2.0.1"`.

## History

- 2026-11-09: First version.
