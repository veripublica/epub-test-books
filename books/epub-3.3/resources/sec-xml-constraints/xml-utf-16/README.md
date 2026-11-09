# A package document in UTF-16 (valid)

- Book: `xml-utf-16.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-xml-constraints/xml-utf-16/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#147](https://github.com/veripublica/epub-test-books/issues/147)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package document is encoded in UTF-16 with a byte order mark. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. UTF-16 is allowed, although UTF-8 is recommended, so a warning would fit.

## Question

The package document is encoded in UTF-16 with a byte order mark. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-xml-constraints`](https://www.w3.org/TR/epub-33/#sec-xml-constraints):

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. UTF-16 is allowed, although UTF-8 is recommended, so a warning would fit.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i xml-utf-16.epub -u --advisory` | WARNING RSC-027; VALID | `xml-utf-16.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck xml-utf-16.epub -u` | WARNING RSC-027, WARNING RSC-027; VALID | `xml-utf-16.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

WARNING RSC-027 is the recommendation to use UTF-8. It does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/package.opf` is written in UTF-16 with a byte order mark, and its XML declaration says so.

## History

- 2026-11-09: First version.
