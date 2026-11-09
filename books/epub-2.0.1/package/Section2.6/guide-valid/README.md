# A `guide` element (valid)

- Book: `guide-valid.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.6/guide-valid/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#212](https://github.com/veripublica/epub-test-books/issues/212)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package document has a guide with one reference. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. One guide with one reference is allowed.

## Question

The package document has a `guide` with one `reference`. Does a validator accept it?

## Clause

OPF 2.0.1, [`Section2.6`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.6):

> Within the package there may be one guide element, containing one or more reference elements.

## Expected result

Valid. One guide with one reference is allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i guide-valid.epub -u --advisory` | no findings; VALID | `guide-valid.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck guide-valid.epub -u` | no findings; VALID | `guide-valid.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, a `guide` is added after `spine`.

## History

- 2026-11-09: First version.
