# `-epub-text-combine: horizontal 2` (valid)

- Book: `epub-text-combine-number.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-css-prefixed/epub-text-combine-number/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: [#433](https://github.com/veripublica/epub-test-books/issues/433)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

style.css holds p { -epub-text-combine: horizontal 2; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. horizontal <number> is a value of the deprecated -epub-text-combine.

## Question

`style.css` holds `p { -epub-text-combine: horizontal 2; }`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> MAY include the prefixed properties defined in 6.3.1.3 Prefixed properties.

EPUB 3.3, [`sec-css-prefixed`](https://www.w3.org/TR/epub-33/#sec-css-prefixed):

> Name: -epub-text-combine (deprecated) Value: none | horizontal | horizontal <number>

## Expected result

Valid. `horizontal <number>` is a value of the deprecated `-epub-text-combine`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i epub-text-combine-number.epub -u --advisory` | USAGE OBS-001; VALID | `epub-text-combine-number.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck epub-text-combine-number.epub -u` | USAGE OBS-001; VALID | `epub-text-combine-number.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a link to `style.css` (`text/css`, in the manifest), which holds `p { -epub-text-combine: horizontal 2; }`.

## History

- 2026-11-12: First version.
