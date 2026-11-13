# `[epub|type~="footnote"]` with no `@namespace` rule (valid)

- Book: `attribute-namespace-undeclared.epub`, built from the EPUB 3 template
- Built by: `scripts/selectors-4/attrnmsp/attribute-namespace-undeclared/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#395](https://github.com/veripublica/epub-test-books/issues/395)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds [epub|type~="footnote"] { display: none; } and no @namespace rule. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `[epub|type~="footnote"] { display: none; }` and no `@namespace` rule. Does a validator accept the book?

## Clause

Selectors Level 4, [`attrnmsp`](https://www.w3.org/TR/selectors-4/#attrnmsp) (6.4. Attribute selectors and namespaces; Working Draft, 22 January 2026):

> An attribute selector with an attribute name containing a namespace prefix that has not been previously declared is an invalid selector.

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

CSS result: No rule is kept. The `epub` prefix is not declared, so the selector is invalid and the rule is dropped, which is a parse error.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i attribute-namespace-undeclared.epub -u --advisory` | USAGE CSS-008; VALID | `attribute-namespace-undeclared.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck attribute-namespace-undeclared.epub -u` | no findings; VALID | `attribute-namespace-undeclared.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `[epub|type~="footnote"] { display: none; }` and no `@namespace` rule, in UTF-8.

## History

- 2026-11-12: First version.
