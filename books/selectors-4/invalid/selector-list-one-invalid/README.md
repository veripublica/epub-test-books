# A selector list with one invalid selector, `p, :foo` (valid)

- Book: `selector-list-one-invalid.epub`, built from the EPUB 3 template
- Built by: `scripts/selectors-4/invalid/selector-list-one-invalid/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p, :foo { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `p, :foo { margin: 0; }`. Does a validator accept the book?

## Clause

Selectors Level 4, [`invalid`](https://www.w3.org/TR/selectors-4/#invalid) (3.9. Invalid Selectors and Error Handling; Working Draft, 22 January 2026):

> a parsing error in a selector, e.g. an unrecognized token or a token which is not allowed at the current parsing point (see overall § 16 Grammar and per-selector syntax definitions), causes that selector to be invalid.

> a selector list containing an invalid selector is invalid.

CSS Syntax Level 3, [`style-rules`](https://www.w3.org/TR/css-syntax-3/#style-rules) (8.1. Style rules; Candidate Recommendation Draft, 1 October 2026):

> The prelude of the qualified rule is parsed as a <selector-list>. If this returns failure, the entire style rule is invalid.

CSS Syntax Level 3, [`css-stylesheets`](https://www.w3.org/TR/css-syntax-3/#css-stylesheets) (8. CSS stylesheets; Candidate Recommendation Draft, 1 October 2026):

> If any style rule is invalid, or any at-rule is not recognized or is invalid according to its grammar or context, it’s a parse error. Discard that rule.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: No rule is kept. `:foo` is invalid, so the whole list `p, :foo` is invalid and the rule is dropped (a parse error); `p` gets nothing.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i selector-list-one-invalid.epub -u --advisory` | USAGE ADV-019; VALID | `selector-list-one-invalid.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck selector-list-one-invalid.epub -u` | no findings; VALID | `selector-list-one-invalid.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output, except USAGE ADV-019, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p, :foo { margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
