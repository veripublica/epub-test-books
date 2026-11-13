# `page-progression-direction="RTL"`

- Book: `ppd-uppercase.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/attrdef-spine-page-progression-direction/ppd-uppercase/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: [#407](https://github.com/veripublica/epub-test-books/issues/407)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The spine element has page-progression-direction="RTL". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The allowed values are ltr, rtl and default, and an XML attribute value is compared as written, so RTL is not one of them.

## Question

The `spine` element has `page-progression-direction="RTL"`. Does a validator reject the book?

## Clause

EPUB 3.3, [`attrdef-spine-page-progression-direction`](https://www.w3.org/TR/epub-33/#attrdef-spine-page-progression-direction):

> The page-progression-direction attribute sets the global direction in which the content flows. Allowed values are ltr (left-to-right), rtl (right-to-left) and default.

## Expected result

Invalid. The allowed values are `ltr`, `rtl` and `default`, and an XML attribute value is compared as written, so `RTL` is not one of them.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i ppd-uppercase.epub -u --advisory` | ERROR RSC-005; INVALID | `ppd-uppercase.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck ppd-uppercase.epub -u` | ERROR RSC-005; INVALID | `ppd-uppercase.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `spine` gets `page-progression-direction="RTL"`.

## History

- 2026-11-12: First version.
