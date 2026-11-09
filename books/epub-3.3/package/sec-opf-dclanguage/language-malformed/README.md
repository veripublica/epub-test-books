# `dc:language` with an underscore

- Book: `language-malformed.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-opf-dclanguage/language-malformed/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#58](https://github.com/veripublica/epub-test-books/issues/58)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The dc:language value is en_US. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A BCP 47 tag separates its subtags with hyphens, so `en_US` is not well-formed.

## Question

The `dc:language` value is `en_US`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-opf-dclanguage`](https://www.w3.org/TR/epub-33/#sec-opf-dclanguage):

> The value of each dc:language element MUST be a well-formed language tag [bcp47].

## Expected result

Invalid. A BCP 47 tag separates its subtags with hyphens, so `en_US` is not well-formed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i language-malformed.epub -u --advisory` | ERROR OPF-092; INVALID | `language-malformed.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck language-malformed.epub -u` | ERROR OPF-092; INVALID | `language-malformed.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the value of `dc:language` becomes `en_US`.

## History

- 2026-11-09: First version.
