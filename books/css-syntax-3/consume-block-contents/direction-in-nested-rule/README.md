# `direction: rtl` in a nested style rule

- Book: `direction-in-nested-rule.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-block-contents/direction-in-nested-rule/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed, wrong error
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#350](https://github.com/veripublica/epub-test-books/issues/350)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { span { direction: rtl; } }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The nested rule span { … } is parsed as a rule, and direction: rtl is one of its declarations.

## Question

`style.css` holds `p { span { direction: rtl; } }`. Does a validator reject the book?

## Clause

CSS Syntax Level 3, [`consume-block-contents`](https://www.w3.org/TR/css-syntax-3/#consume-block-contents) (5.5.5 Consume a block’s contents; Candidate Recommendation Draft, 1 October 2026):

> Mark input.
>
> Consume a declaration from input, with nested set to true. If a declaration was returned, append it to decls, and discard a mark from input.
>
> Otherwise, restore a mark from input, then consume a qualified rule from input, with nested set to true, and <semicolon-token> as the stop token.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. The nested rule `span { … }` is parsed as a rule, and `direction: rtl` is one of its declarations.

CSS result: One rule, `p`, with one nested style rule, `span`, which declares `direction: rtl`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i direction-in-nested-rule.epub -u --advisory` | ERROR CSS-001; INVALID | `direction-in-nested-rule.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-nested-rule.epub -u` | ERROR CSS-008, ERROR CSS-008, ERROR CSS-008; INVALID | `direction-in-nested-rule.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it does not report `direction` (no CSS-001), and reports the nested rule as errors (CSS-008).

- **epubcheck: missed, wrong error.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { span { direction: rtl; } }`, in UTF-8.

## History

- 2026-11-12: First version.
