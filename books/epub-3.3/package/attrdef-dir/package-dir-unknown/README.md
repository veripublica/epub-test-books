# `dir="right"` on `package`

- Book: `package-dir-unknown.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/attrdef-dir/package-dir-unknown/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: [#413](https://github.com/veripublica/epub-test-books/issues/413)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package element has dir="right". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. right is not one of the allowed values ltr, rtl and auto.

## Question

The `package` element has `dir="right"`. Does a validator reject the book?

## Clause

EPUB 3.3, [`attrdef-dir`](https://www.w3.org/TR/epub-33/#attrdef-dir):

> Allowed values are: ltr — left-to-right base direction; rtl — right-to-left base direction; and auto — base direction is determined using the Unicode Bidi Algorithm [bidi].

## Expected result

Invalid. `right` is not one of the allowed values `ltr`, `rtl` and `auto`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i package-dir-unknown.epub -u --advisory` | ERROR RSC-005; INVALID | `package-dir-unknown.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck package-dir-unknown.epub -u` | ERROR RSC-005; INVALID | `package-dir-unknown.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the `package` element has `dir="right"`.

## History

- 2026-11-12: First version.
