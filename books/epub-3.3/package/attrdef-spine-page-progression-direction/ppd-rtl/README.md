# `page-progression-direction="rtl"` (valid)

- Book: `ppd-rtl.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/attrdef-spine-page-progression-direction/ppd-rtl/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The spine element has page-progression-direction="rtl". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. rtl is one of the three allowed values.

## Question

The `spine` element has `page-progression-direction="rtl"`. Does a validator accept the book?

## Clause

EPUB 3.3, [`attrdef-spine-page-progression-direction`](https://www.w3.org/TR/epub-33/#attrdef-spine-page-progression-direction):

> The page-progression-direction attribute sets the global direction in which the content flows. Allowed values are ltr (left-to-right), rtl (right-to-left) and default.

## Expected result

Valid. `rtl` is one of the three allowed values.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i ppd-rtl.epub -u --advisory` | no findings; VALID | `ppd-rtl.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck ppd-rtl.epub -u` | no findings; VALID | `ppd-rtl.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `spine` gets `page-progression-direction="rtl"`.

## History

- 2026-11-12: First version.
