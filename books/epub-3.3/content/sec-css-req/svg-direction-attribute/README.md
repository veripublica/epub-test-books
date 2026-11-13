# The SVG `direction` presentation attribute (valid)

- Book: `svg-direction-attribute.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-css-req/svg-direction-attribute/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: [#429](https://github.com/veripublica/epub-test-books/issues/429)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml holds an inline svg whose text element has direction="rtl". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. A presentation attribute is not a CSS style sheet, and EPUB 3.3 names the SVG direction attribute as the way to set base direction.

## Question

`content.xhtml` holds an inline `svg` whose `text` element has `direction="rtl"`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> the dir attribute [html] and direction attribute [svg] for inline base directionality.

> the bdo element with the dir attribute [html] and the presentation attribute alternative for unicode-bidi [svg] for bidirectionality.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

## Expected result

Valid. A presentation attribute is not a CSS style sheet, and EPUB 3.3 names the SVG `direction` attribute as the way to set base direction.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i svg-direction-attribute.epub -u --advisory` | no findings; VALID | `svg-direction-attribute.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-direction-attribute.epub -u` | no findings; VALID | `svg-direction-attribute.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, the paragraph becomes an inline `svg` with one `text` element that has `direction="rtl"`; the `content` item gets `properties="svg"`.

## History

- 2026-11-12: First version.
