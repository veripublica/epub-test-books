# `-epub-writing-mode: vertical-rl` (valid)

- Book: `epub-writing-mode.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-css-prefixed/epub-writing-mode/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

style.css holds html { -epub-writing-mode: vertical-rl; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. -epub-writing-mode is one of the prefixed properties EPUB 3.3 keeps.

## Question

`style.css` holds `html { -epub-writing-mode: vertical-rl; }`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> MAY include the prefixed properties defined in 6.3.1.3 Prefixed properties.

EPUB 3.3, [`sec-css-prefixed`](https://www.w3.org/TR/epub-33/#sec-css-prefixed):

> This property is a prefixed version of the writing-mode property [css-writing-modes-3], with the same syntax and behavior.

## Expected result

Valid. `-epub-writing-mode` is one of the prefixed properties EPUB 3.3 keeps.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i epub-writing-mode.epub -u --advisory` | USAGE OBS-001; VALID | `epub-writing-mode.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck epub-writing-mode.epub -u` | USAGE OBS-001; VALID | `epub-writing-mode.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a link to `style.css` (`text/css`, in the manifest), which holds `html { -epub-writing-mode: vertical-rl; }`.

## History

- 2026-11-12: First version.
