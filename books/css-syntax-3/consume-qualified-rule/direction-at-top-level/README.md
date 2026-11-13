# `direction: rtl;` outside any rule (valid)

- Book: `direction-at-top-level.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-qualified-rule/direction-at-top-level/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#363](https://github.com/veripublica/epub-test-books/issues/363)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { margin: 0; }, then a line direction: rtl; outside any rule, and nothing after it. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. At the top level, direction: rtl; starts a qualified rule. A semicolon does not end it, and the file ends before any {, so it is dropped: no declaration is made, and the sheet has no direction property.

## Question

`style.css` holds `p { margin: 0; }`, then a line `direction: rtl;` outside any rule, and nothing after it. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`consume-qualified-rule`](https://www.w3.org/TR/css-syntax-3/#consume-qualified-rule) (5.5.3 Consume a qualified rule; Candidate Recommendation Draft, 1 October 2026):

> <EOF-token>
>
> stop token (if passed)
>
> This is a parse error. Return nothing.

CSS Syntax Level 3, [`error-handling`](https://www.w3.org/TR/css-syntax-3/#error-handling) (2.2 Error Handling; Candidate Recommendation Draft, 1 October 2026), a section that is not normative:

> Qualified rules work similarly, except that semicolons don’t end them; instead, they are just taken in as part of the rule’s prelude.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. At the top level, `direction: rtl;` starts a qualified rule. A semicolon does not end it, and the file ends before any `{`, so it is dropped: no declaration is made, and the sheet has no `direction` property.

CSS result: One rule, `p { margin: 0; }`. The second qualified rule reaches EOF with no block: a parse error, and nothing is added.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i direction-at-top-level.epub -u --advisory` | USAGE CSS-008; VALID | `direction-at-top-level.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-at-top-level.epub -u` | ERROR CSS-008, ERROR CSS-008; INVALID | `direction-at-top-level.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the parse error as errors (CSS-008).

- **epubcheck: wrong error.** [w3c/epubcheck#1768](https://github.com/w3c/epubcheck/issues/1768).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { margin: 0; }`, then a line `direction: rtl;` outside any rule, and nothing after it, in UTF-8.

## History

- 2026-11-12: First version.
