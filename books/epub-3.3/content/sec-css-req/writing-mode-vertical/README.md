# `writing-mode: vertical-rl` (valid)

- Book: `writing-mode-vertical.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-css-req/writing-mode-vertical/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

style.css holds html { writing-mode: vertical-rl; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. writing-mode is neither direction nor unicode-bidi, and EPUB 3.3 allows any other property.

## Question

`style.css` holds `html { writing-mode: vertical-rl; }`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

## Expected result

Valid. `writing-mode` is neither `direction` nor `unicode-bidi`, and EPUB 3.3 allows any other property.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i writing-mode-vertical.epub -u --advisory` | no findings; VALID | `writing-mode-vertical.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck writing-mode-vertical.epub -u` | no findings; VALID | `writing-mode-vertical.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a link to `style.css` (`text/css`, in the manifest), which holds `html { writing-mode: vertical-rl; }`.

## History

- 2026-11-12: First version.
