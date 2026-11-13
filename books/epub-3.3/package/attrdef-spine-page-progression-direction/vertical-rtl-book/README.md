# A Japanese book in vertical writing, paged right to left (valid)

- Book: `vertical-rtl-book.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/attrdef-spine-page-progression-direction/vertical-rtl-book/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: [#409](https://github.com/veripublica/epub-test-books/issues/409)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

spine has page-progression-direction="rtl", content.xhtml is in Japanese (ja), and its stylesheet sets writing-mode: vertical-rl on html. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. rtl is an allowed value, and EPUB 3.3 says a content document may override the global direction with writing-mode. writing-mode is neither direction nor unicode-bidi.

## Question

`spine` has `page-progression-direction="rtl"`, `content.xhtml` is in Japanese (`ja`), and its stylesheet sets `writing-mode: vertical-rl` on `html`. Does a validator accept the book?

## Clause

EPUB 3.3, [`attrdef-spine-page-progression-direction`](https://www.w3.org/TR/epub-33/#attrdef-spine-page-progression-direction):

> The page-progression-direction attribute sets the global direction in which the content flows. Allowed values are ltr (left-to-right), rtl (right-to-left) and default.

EPUB 3.3, [`attrdef-spine-page-progression-direction`](https://www.w3.org/TR/epub-33/#attrdef-spine-page-progression-direction):

> Although the page-progression-direction attribute sets the global flow direction, individual EPUB content documents and parts of EPUB content documents MAY override this setting (e.g., via the writing-mode CSS property).

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

## Expected result

Valid. `rtl` is an allowed value, and EPUB 3.3 says a content document may override the global direction with `writing-mode`. `writing-mode` is neither `direction` nor `unicode-bidi`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i vertical-rtl-book.epub -u --advisory` | no findings; VALID | `vertical-rtl-book.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck vertical-rtl-book.epub -u` | no findings; VALID | `vertical-rtl-book.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `spine` gets `page-progression-direction="rtl"`. `content.xhtml` gets `xml:lang="ja" lang="ja"` and links `style.css` (`text/css`), which holds `html { writing-mode: vertical-rl; }`.

## History

- 2026-11-12: First version.
