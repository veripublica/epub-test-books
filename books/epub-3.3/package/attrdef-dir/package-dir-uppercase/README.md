# `dir="RTL"` on `package`

- Book: `package-dir-uppercase.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/attrdef-dir/package-dir-uppercase/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: [#414](https://github.com/veripublica/epub-test-books/issues/414)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package element has dir="RTL". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The allowed values are ltr, rtl and auto, and an XML attribute value is compared as written, so RTL is not one of them. (In HTML the same value is valid: see books/epub-3.3/content/sec-xhtml-req/html-dir-uppercase.)

## Question

The `package` element has `dir="RTL"`. Does a validator reject the book?

## Clause

EPUB 3.3, [`attrdef-dir`](https://www.w3.org/TR/epub-33/#attrdef-dir):

> Allowed values are: ltr — left-to-right base direction; rtl — right-to-left base direction; and auto — base direction is determined using the Unicode Bidi Algorithm [bidi].

## Expected result

Invalid. The allowed values are `ltr`, `rtl` and `auto`, and an XML attribute value is compared as written, so `RTL` is not one of them. (In HTML the same value is valid: see `books/epub-3.3/content/sec-xhtml-req/html-dir-uppercase`.)

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i package-dir-uppercase.epub -u --advisory` | ERROR RSC-005; INVALID | `package-dir-uppercase.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck package-dir-uppercase.epub -u` | ERROR RSC-005; INVALID | `package-dir-uppercase.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the `package` element has `dir="RTL"`.

## History

- 2026-11-12: First version.
