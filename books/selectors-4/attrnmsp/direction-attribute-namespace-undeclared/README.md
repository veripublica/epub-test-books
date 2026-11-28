# `direction: rtl` in a rule with an undeclared namespace prefix, `[epub|type~="footnote"]` (valid)

- Book: `direction-attribute-namespace-undeclared.epub`, built from the EPUB 3 template
- Built by: `scripts/selectors-4/attrnmsp/direction-attribute-namespace-undeclared/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, after w3c/epub-specs#3115 (held CSS cases)
- Issue: [#674](https://github.com/veripublica/epub-test-books/issues/674)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds [epub|type~="footnote"] { direction: rtl; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The epub prefix is not declared, so the selector is invalid and CSS drops the rule. The parsed style sheet therefore holds no direction property, and EPUB 3.3 forbids only a declared one (w3c/epub-specs#3115).

## Question

`style.css` holds `[epub|type~="footnote"] { direction: rtl; }`. Does a validator accept the book?

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

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The `epub` prefix is not declared, so the selector is invalid and CSS drops the rule. The parsed style sheet holds no `direction` property, it holds no `unicode-bidi` either, and it is UTF-8, so EPUB 3.3 asks nothing more of it.

EPUB 3.3 does not say whether "include" means that the property is declared or only that its name is written in the style sheet, so this set waited for the Working Group. The question went to [w3c/epub-specs#3115](https://github.com/w3c/epub-specs/issues/3115). The [answer](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6880091067) there: "It means the property must be declared." For a checker, "if the parsed sheet produces an object that contains a property with the name 'direction', you should report an error." The issue was closed on 2026-11-19 with the requirement's text unchanged ("[the current spec text stands](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6896967498)"); only the note under it was rewritten, in [w3c/epub-specs#3118](https://github.com/w3c/epub-specs/pull/3118).

CSS result: No rule is kept. The `epub` prefix is not declared, so the selector is invalid and the rule is dropped, which is a parse error.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.50.0 | `epubveri -i direction-attribute-namespace-undeclared.epub -u --advisory` | USAGE CSS-008; VALID | `direction-attribute-namespace-undeclared.epubveri-0.50.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-attribute-namespace-undeclared.epub -u` | ERROR CSS-001; INVALID | `direction-attribute-namespace-undeclared.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the dropped `direction` declaration as an error (CSS-001).

- **epubcheck: wrong error.** [w3c/epubcheck#1781](https://github.com/w3c/epubcheck/issues/1781).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `[epub|type~="footnote"] { direction: rtl; }`, in UTF-8.

## History

- 2026-11-20: First version.
