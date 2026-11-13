# An unknown at-rule, `@foo` (valid)

- Book: `unknown-at-rule.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-at-rule/unknown-at-rule/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#348](https://github.com/veripublica/epub-test-books/issues/348)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @foo bar { baz }, then p { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `@foo bar { baz }`, then `p { margin: 0; }`. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`consume-at-rule`](https://www.w3.org/TR/css-syntax-3/#consume-at-rule) (5.5.2 Consume an at-rule; Candidate Recommendation Draft, 1 October 2026):

> <{-token>
>
> Consume a block from input, and assign the result to rule’s child rules.

> If rule is valid in the current context, return it. Otherwise, return nothing.

CSS Syntax Level 3, [`css-stylesheets`](https://www.w3.org/TR/css-syntax-3/#css-stylesheets) (8. CSS stylesheets; Candidate Recommendation Draft, 1 October 2026):

> If any style rule is invalid, or any at-rule is not recognized or is invalid according to its grammar or context, it’s a parse error. Discard that rule.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: Inside the block, `baz` is not a declaration, and re-read as a rule it reaches the `}`: a parse error. `@foo` is not valid in a stylesheet, so the at-rule, with its block, is dropped, a second parse error. One rule is kept, `p { margin: 0; }`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i unknown-at-rule.epub -u --advisory` | USAGE ADV-020, USAGE CSS-008; VALID | `unknown-at-rule.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck unknown-at-rule.epub -u` | ERROR CSS-008; INVALID | `unknown-at-rule.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the unknown at-rule as an error (CSS-008).

- **epubcheck: wrong error.** [w3c/epubcheck#1768](https://github.com/w3c/epubcheck/issues/1768).

Every epubveri finding here is in its default output, except USAGE ADV-020, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `@foo bar { baz }`, then `p { margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
