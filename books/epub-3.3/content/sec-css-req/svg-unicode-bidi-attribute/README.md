# The SVG `unicode-bidi` presentation attribute (valid)

- Book: `svg-unicode-bidi-attribute.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-css-req/svg-unicode-bidi-attribute/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: [#430](https://github.com/veripublica/epub-test-books/issues/430)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml holds an inline svg whose text element has unicode-bidi="bidi-override". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. A presentation attribute is not a CSS style sheet, and EPUB 3.3 names the SVG presentation attribute as the alternative to unicode-bidi.

## Question

`content.xhtml` holds an inline `svg` whose `text` element has `unicode-bidi="bidi-override"`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> the dir attribute [html] and direction attribute [svg] for inline base directionality.

> the bdo element with the dir attribute [html] and the presentation attribute alternative for unicode-bidi [svg] for bidirectionality.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

## Expected result

Valid. A presentation attribute is not a CSS style sheet, and EPUB 3.3 names the SVG presentation attribute as the alternative to `unicode-bidi`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i svg-unicode-bidi-attribute.epub -u --advisory` | no findings; VALID | `svg-unicode-bidi-attribute.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-unicode-bidi-attribute.epub -u` | no findings; VALID | `svg-unicode-bidi-attribute.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, the paragraph becomes an inline `svg` with one `text` element that has `unicode-bidi="bidi-override"`; the `content` item gets `properties="svg"`.

## History

- 2026-11-12: First version.
