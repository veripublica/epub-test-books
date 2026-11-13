# An invalid selector inside `:is()`, `:is(p, :foo)` (valid)

- Book: `is-forgiving.epub`, built from the EPUB 3 template
- Built by: `scripts/selectors-4/matches/is-forgiving/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#399](https://github.com/veripublica/epub-test-books/issues/399)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds :is(p, :foo) { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `:is(p, :foo) { margin: 0; }`. Does a validator accept the book?

## Clause

Selectors Level 4, [`matches`](https://www.w3.org/TR/selectors-4/#matches) (4.2. The Matches-Any Pseudo-class: :is(); Working Draft, 22 January 2026):

> The matches-any pseudo-class, :is(), is a functional pseudo-class taking a <forgiving-selector-list> as its sole argument. If the argument, after parsing, is an empty list, the pseudo-class is valid but matches nothing.

Selectors Level 4, [`forgiving-selector`](https://www.w3.org/TR/selectors-4/#forgiving-selector) (16.1. <forgiving-selector-list> and <forgiving-relative-selector-list>; Working Draft, 22 January 2026):

> The <forgiving-selector-list> production instead parses each selector in the list individually, simply ignoring ones that fail to parse, so the remaining selectors can still be used.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule, kept. `:is()` takes a forgiving list, so `:foo` is left out and the selector matches `p`; `margin: 0` applies to every `p`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i is-forgiving.epub -u --advisory` | no findings; VALID | `is-forgiving.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck is-forgiving.epub -u` | no findings; VALID | `is-forgiving.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `:is(p, :foo) { margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
