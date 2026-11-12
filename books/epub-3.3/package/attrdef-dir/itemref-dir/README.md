# `dir` on an `itemref`

- Book: `itemref-dir.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/attrdef-dir/itemref-dir/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The itemref element for content.xhtml has dir="rtl". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. dir is allowed on collection, the Dublin Core elements, meta and package. itemref is none of them; the reading direction of the spine is page-progression-direction.

## Question

The `itemref` element for `content.xhtml` has `dir="rtl"`. Does a validator reject the book?

## Clause

EPUB 3.3, [`attrdef-dir`](https://www.w3.org/TR/epub-33/#attrdef-dir):

> Allowed on: collection, Dublin Core elements, meta, and package.

## Expected result

Invalid. `dir` is allowed on `collection`, the Dublin Core elements, `meta` and `package`. `itemref` is none of them; the reading direction of the spine is `page-progression-direction`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i itemref-dir.epub -u --advisory` | ERROR RSC-005; INVALID | `itemref-dir.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck itemref-dir.epub -u` | ERROR RSC-005; INVALID | `itemref-dir.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the `itemref` element for `content.xhtml` has `dir="rtl"`.

## History

- 2026-11-12: First version.
