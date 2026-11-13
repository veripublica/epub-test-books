# `-epub-ruby-position`, a prefixed property EPUB 3.3 removed (valid)

- Book: `epub-removed-property.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-css-prefixed/epub-removed-property/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: [#434](https://github.com/veripublica/epub-test-books/issues/434)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

style.css holds p { -epub-ruby-position: over; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. -epub-ruby-position was removed from EPUB, so it is now just a property no reading system has to know. EPUB 3.3 allows any property except direction and unicode-bidi.

## Question

`style.css` holds `p { -epub-ruby-position: over; }`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-css-prefixed`](https://www.w3.org/TR/epub-33/#sec-css-prefixed):

> This specification retains the widely used prefixed properties from [epubcontentdocs-301] but removes support for the less-used ones.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

## Expected result

Valid. `-epub-ruby-position` was removed from EPUB, so it is now just a property no reading system has to know. EPUB 3.3 allows any property except `direction` and `unicode-bidi`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i epub-removed-property.epub -u --advisory` | USAGE OBS-001; VALID | `epub-removed-property.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck epub-removed-property.epub -u` | USAGE OBS-001; VALID | `epub-removed-property.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a link to `style.css` (`text/css`, in the manifest), which holds `p { -epub-ruby-position: over; }`.

## History

- 2026-11-12: First version.
