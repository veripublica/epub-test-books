# `dir="rtl"` on `dc:title` (valid)

- Book: `title-dir-rtl.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/attrdef-dir/title-dir-rtl/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The dc:title element has dir="rtl". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. rtl is an allowed value, and dir is allowed on Dublin Core elements.

## Question

The `dc:title` element has `dir="rtl"`. Does a validator accept the book?

## Clause

EPUB 3.3, [`attrdef-dir`](https://www.w3.org/TR/epub-33/#attrdef-dir):

> Allowed values are: ltr — left-to-right base direction; rtl — right-to-left base direction; and auto — base direction is determined using the Unicode Bidi Algorithm [bidi].

EPUB 3.3, [`attrdef-dir`](https://www.w3.org/TR/epub-33/#attrdef-dir):

> Allowed on: collection, Dublin Core elements, meta, and package.

## Expected result

Valid. `rtl` is an allowed value, and `dir` is allowed on Dublin Core elements.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i title-dir-rtl.epub -u --advisory` | no findings; VALID | `title-dir-rtl.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck title-dir-rtl.epub -u` | no findings; VALID | `title-dir-rtl.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the `dc:title` element has `dir="rtl"`.

## History

- 2026-11-12: First version.
