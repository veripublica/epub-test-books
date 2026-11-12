# The `:dir(rtl)` pseudo-class (valid)

- Book: `dir-pseudo-class.epub`, built from the EPUB 3 template
- Built by: `scripts/selectors-4/the-dir-pseudo/dir-pseudo-class/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p:dir(rtl) { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. :dir() selects by the document's directionality and is not the direction property, so the sheet holds neither direction nor unicode-bidi. It is UTF-8, so EPUB 3.3 asks nothing more of it.

## Question

`style.css` holds `p:dir(rtl) { margin: 0; }`. Does a validator accept the book?

## Clause

Selectors Level 4, [`the-dir-pseudo`](https://www.w3.org/TR/selectors-4/#the-dir-pseudo) (7.1. The Directionality Pseudo-class: :dir(); Working Draft, 22 January 2026):

> The :dir() pseudo-class does not select based on stylistic states—for example, the CSS direction property does not affect whether it matches.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. `:dir()` selects by the document's directionality and is not the `direction` property, so the sheet holds neither `direction` nor `unicode-bidi`. It is UTF-8, so EPUB 3.3 asks nothing more of it.

CSS result: One rule, kept: every `p` whose directionality is right-to-left. The book has none, so the rule matches nothing.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i dir-pseudo-class.epub -u --advisory` | no findings; VALID | `dir-pseudo-class.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck dir-pseudo-class.epub -u` | no findings; VALID | `dir-pseudo-class.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p:dir(rtl) { margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
