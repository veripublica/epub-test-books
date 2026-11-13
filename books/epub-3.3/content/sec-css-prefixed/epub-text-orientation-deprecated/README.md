# `-epub-text-orientation: vertical-right` (valid)

- Book: `epub-text-orientation-deprecated.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-css-prefixed/epub-text-orientation-deprecated/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: [#432](https://github.com/veripublica/epub-test-books/issues/432)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

style.css holds p { -epub-text-orientation: vertical-right; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. vertical-right is a deprecated keyword that -epub-text-orientation still supports.

## Question

`style.css` holds `p { -epub-text-orientation: vertical-right; }`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> MAY include the prefixed properties defined in 6.3.1.3 Prefixed properties.

EPUB 3.3, [`sec-css-prefixed`](https://www.w3.org/TR/epub-33/#sec-css-prefixed):

> For compatibility with existing content, the -epub-text-orientation property also supports the deprecated vertical-right, rotate-right, and rotate-normal keywords.

## Expected result

Valid. `vertical-right` is a deprecated keyword that `-epub-text-orientation` still supports.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i epub-text-orientation-deprecated.epub -u --advisory` | USAGE OBS-001; VALID | `epub-text-orientation-deprecated.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck epub-text-orientation-deprecated.epub -u` | USAGE OBS-001; VALID | `epub-text-orientation-deprecated.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a link to `style.css` (`text/css`, in the manifest), which holds `p { -epub-text-orientation: vertical-right; }`.

## History

- 2026-11-12: First version.
