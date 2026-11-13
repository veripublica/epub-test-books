# An `@namespace` rule after a style rule (valid)

- Book: `namespace-after-rule.epub`, built from the EPUB 3 template
- Built by: `scripts/css-namespaces-3/syntax/namespace-after-rule/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#392](https://github.com/veripublica/epub-test-books/issues/392)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { margin: 0; }, then @namespace epub "http://www.idpf.org/2007/ops";, then [epub|type~="footnote"] { display: none; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `p { margin: 0; }`, then `@namespace epub "http://www.idpf.org/2007/ops";`, then `[epub|type~="footnote"] { display: none; }`. Does a validator accept the book?

## Clause

CSS Namespaces Module Level 3, [`syntax`](https://www.w3.org/TR/css-namespaces-3/#syntax) (3.1 Syntax; Recommendation, 29 September 2011, edited in place 20 March 2014):

> Any @namespace rules must follow all @charset and @import rules and precede all other non-ignored at-rules and style rules in a style sheet.

> A syntactically invalid @namespace rule (whether malformed or misplaced) must be ignored. A CSS style sheet containing an invalid @namespace rule is not a valid style sheet.

Selectors Level 4, [`attrnmsp`](https://www.w3.org/TR/selectors-4/#attrnmsp) (6.4. Attribute selectors and namespaces; Working Draft, 22 January 2026):

> An attribute selector with an attribute name containing a namespace prefix that has not been previously declared is an invalid selector.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule is kept, `p { margin: 0; }`. The `@namespace` rule comes after it, so it is ignored, a parse error, and the `epub` prefix is never declared. The last rule is dropped for its invalid selector, a second parse error. CSS Namespaces calls such a sheet not valid; EPUB 3.3 does not ask for a valid sheet.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i namespace-after-rule.epub -u --advisory` | USAGE ADV-021, USAGE CSS-008; VALID | `namespace-after-rule.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck namespace-after-rule.epub -u` | no findings; VALID | `namespace-after-rule.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output, except USAGE ADV-021, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { margin: 0; }`, then `@namespace epub "http://www.idpf.org/2007/ops";`, then `[epub|type~="footnote"] { display: none; }`, in UTF-8.

## History

- 2026-11-12: First version.
