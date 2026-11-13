# A stylesheet that starts with `}` (valid)

- Book: `stray-close-brace.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-qualified-rule/stray-close-brace/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#365](https://github.com/veripublica/epub-test-books/issues/365)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds } p { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `} p { margin: 0; }`. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`consume-qualified-rule`](https://www.w3.org/TR/css-syntax-3/#consume-qualified-rule) (5.5.3 Consume a qualified rule; Candidate Recommendation Draft, 1 October 2026):

> <}-token>
>
> This is a parse error. If nested is true, return nothing. Otherwise, consume a token and append the result to rule’s prelude.

> If rule is valid in the current context, return it; otherwise return an invalid rule error.

CSS Syntax Level 3, [`css-stylesheets`](https://www.w3.org/TR/css-syntax-3/#css-stylesheets) (8. CSS stylesheets; Candidate Recommendation Draft, 1 October 2026):

> If any style rule is invalid, or any at-rule is not recognized or is invalid according to its grammar or context, it’s a parse error. Discard that rule.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: The `}` is a parse error and becomes part of a qualified rule's prelude, `} p`, which is not a valid selector, so the rule is dropped, a second parse error. No rule is kept.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i stray-close-brace.epub -u --advisory` | USAGE CSS-008; VALID | `stray-close-brace.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck stray-close-brace.epub -u` | ERROR CSS-008; INVALID | `stray-close-brace.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the parse error as an error (CSS-008).

- **epubcheck: wrong error.** [w3c/epubcheck#1768](https://github.com/w3c/epubcheck/issues/1768).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `} p { margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
