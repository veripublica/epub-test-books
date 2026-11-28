# `ui-serif` as an `@font-face` family name (valid)

- Book: `font-face-ui-serif.epub`, built from the EPUB 3 template
- Built by: `scripts/css-fonts-4/font-family-desc/font-face-ui-serif/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, for its 0.21 release (note 2026-11-18)
- Issue: [#651](https://github.com/veripublica/epub-test-books/issues/651)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @font-face { font-family: ui-serif; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `@font-face { font-family: ui-serif; }`. Does a validator accept the book?

## Clause

CSS Fonts Module Level 4, [`font-family-desc`](https://www.w3.org/TR/css-fonts-4/#font-family-desc) (4.2. Font family: the font-family descriptor; Working Draft, 12 November 2026):

> Name: font-family For: @font-face Value: <font-family-name> Initial: N/A

CSS Fonts Module Level 4, [`font-family-name-syntax`](https://www.w3.org/TR/css-fonts-4/#font-family-name-syntax) (2.1.1. Syntax of <font-family-name>; Working Draft, 12 November 2026):

> Font family names that happen to be the same as a font-family keyword value (e.g. CSS-wide keywords such as inherit, or <generic-font-family> keywords such as serif) must be quoted to prevent confusion with the keywords of the same names. UAs must not consider these keywords as matching the <font-family-name> type.

CSS Fonts Module Level 4, [`generic-family-name-syntax`](https://www.w3.org/TR/css-fonts-4/#generic-family-name-syntax) (2.1.2. Syntax of <generic-font-family>; Working Draft, 12 November 2026):

> <generic-font-incomplete> = ui-serif | ui-sans-serif | ui-monospace | ui-rounded

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One `@font-face` rule, kept, with no descriptors. `ui-serif` is a `<generic-font-family>` keyword, which must not match `<font-family-name>`, so the `font-family` descriptor is invalid and dropped.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i font-face-ui-serif.epub -u --advisory` | USAGE CSS-028, USAGE ADV-024; VALID | `font-face-ui-serif.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck font-face-ui-serif.epub -u` | USAGE CSS-028; VALID | `font-face-ui-serif.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output, except USAGE ADV-024, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `@font-face { font-family: ui-serif; }`, in UTF-8.

## History

- 2026-11-18: First version.
