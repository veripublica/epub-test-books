# `-epub-direction: rtl` (valid)

- Book: `epub-direction.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-css-prefixed/epub-direction/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

style.css holds p { -epub-direction: rtl; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. -epub-direction is not a prefixed property EPUB defines, and it is not the direction property, so the sheet does not include direction.

## Question

`style.css` holds `p { -epub-direction: rtl; }`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-css-prefixed`](https://www.w3.org/TR/epub-33/#sec-css-prefixed):

> Unless otherwise noted, prefixed properties and values behave exactly as their unprefixed equivalents as described in the appropriate CSS specification.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

## Expected result

Valid. `-epub-direction` is not a prefixed property EPUB defines, and it is not the `direction` property, so the sheet does not include `direction`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i epub-direction.epub -u --advisory` | USAGE OBS-001; VALID | `epub-direction.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck epub-direction.epub -u` | USAGE OBS-001; VALID | `epub-direction.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a link to `style.css` (`text/css`, in the manifest), which holds `p { -epub-direction: rtl; }`.

## History

- 2026-11-12: First version.
