# `dir="auto"` on `package` (valid)

- Book: `package-dir-auto.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/attrdef-dir/package-dir-auto/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: [#411](https://github.com/veripublica/epub-test-books/issues/411)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package element has dir="auto". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. auto is an allowed value, and dir is allowed on package.

## Question

The `package` element has `dir="auto"`. Does a validator accept the book?

## Clause

EPUB 3.3, [`attrdef-dir`](https://www.w3.org/TR/epub-33/#attrdef-dir):

> Allowed values are: ltr — left-to-right base direction; rtl — right-to-left base direction; and auto — base direction is determined using the Unicode Bidi Algorithm [bidi].

EPUB 3.3, [`attrdef-dir`](https://www.w3.org/TR/epub-33/#attrdef-dir):

> Allowed on: collection, Dublin Core elements, meta, and package.

## Expected result

Valid. `auto` is an allowed value, and `dir` is allowed on `package`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i package-dir-auto.epub -u --advisory` | no findings; VALID | `package-dir-auto.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck package-dir-auto.epub -u` | no findings; VALID | `package-dir-auto.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the `package` element has `dir="auto"`.

## History

- 2026-11-12: First version.
