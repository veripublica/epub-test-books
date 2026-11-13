# `xml:lang` with an underscore

- Book: `xml-lang-malformed.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/attrdef-xml-lang/xml-lang-malformed/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#59](https://github.com/veripublica/epub-test-books/issues/59)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The xml:lang attribute on the package element is en_US. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A BCP 47 tag separates its subtags with hyphens, so `en_US` is not well-formed.

## Question

The `xml:lang` attribute on `package` is `en_US`. Does a validator reject it?

## Clause

EPUB 3.3, [`attrdef-xml-lang`](https://www.w3.org/TR/epub-33/#attrdef-xml-lang):

> The value of each xml:lang attribute MUST be a well-formed language tag [bcp47].

## Expected result

Invalid. A BCP 47 tag separates its subtags with hyphens, so `en_US` is not well-formed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i xml-lang-malformed.epub -u --advisory` | ERROR OPF-092, ERROR RSC-005; INVALID | `xml-lang-malformed.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck xml-lang-malformed.epub -u` | ERROR RSC-005, ERROR OPF-092; INVALID | `xml-lang-malformed.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `xml:lang` on `package` becomes `en_US`.

## History

- 2026-11-09: First version.
