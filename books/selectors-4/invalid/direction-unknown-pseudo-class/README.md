# `direction: rtl` in a rule with an unknown pseudo-class, `p:foo` (valid)

- Book: `direction-unknown-pseudo-class.epub`, built from the EPUB 3 template
- Built by: `scripts/selectors-4/invalid/direction-unknown-pseudo-class/build.py`
- Origin: built here
- Expected: valid
- Marks: epubveri: wrong error; epubcheck: wrong error
- Asked for by: the maintainer, after w3c/epub-specs#3115 (held CSS cases)
- Issue: [#676](https://github.com/veripublica/epub-test-books/issues/676)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p:foo { direction: rtl; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. :foo is not a pseudo-class, so the selector is invalid and CSS drops the rule. The parsed style sheet therefore holds no direction property, and EPUB 3.3 forbids only a declared one (w3c/epub-specs#3115).

## Question

`style.css` holds `p:foo { direction: rtl; }`. Does a validator accept the book?

## Clause

Selectors Level 4, [`invalid`](https://www.w3.org/TR/selectors-4/#invalid) (3.9. Invalid Selectors and Error Handling; Working Draft, 22 January 2026):

> a parsing error in a selector, e.g. an unrecognized token or a token which is not allowed at the current parsing point (see overall § 16 Grammar and per-selector syntax definitions), causes that selector to be invalid.

Selectors Level 4, [`invalid`](https://www.w3.org/TR/selectors-4/#invalid) (3.9. Invalid Selectors and Error Handling; Working Draft, 22 January 2026), a note, which is not normative:

> Note: Consistent with CSS’s forwards-compatible parsing principle, UAs must treat as invalid any pseudo-classes, pseudo-elements, combinators, or other syntactic constructs for which they have no usable level of support.

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

Valid. `:foo` is not a pseudo-class, so the selector is invalid and CSS drops the rule. The parsed style sheet holds no `direction` property, it holds no `unicode-bidi` either, and it is UTF-8, so EPUB 3.3 asks nothing more of it.

EPUB 3.3 does not say whether "include" means that the property is declared or only that its name is written in the style sheet, so this set waited for the Working Group. The question went to [w3c/epub-specs#3115](https://github.com/w3c/epub-specs/issues/3115). The [answer](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6880091067) there: "It means the property must be declared." For a checker, "if the parsed sheet produces an object that contains a property with the name 'direction', you should report an error." The issue was closed on 2026-11-19 with the requirement's text unchanged ("[the current spec text stands](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6896967498)"); only the note under it was rewritten, in [w3c/epub-specs#3118](https://github.com/w3c/epub-specs/pull/3118).

CSS result: No rule is kept. `:foo` is not a pseudo-class, so the selector is invalid and the rule is dropped, which is a parse error.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.47.0 | `epubveri -i direction-unknown-pseudo-class.epub -u --advisory` | ERROR CSS-001, USAGE ADV-019; INVALID | `direction-unknown-pseudo-class.epubveri-0.47.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-unknown-pseudo-class.epub -u` | ERROR CSS-001; INVALID | `direction-unknown-pseudo-class.epubcheck-5.4.0.txt` |

Neither agrees with the expected result. epubveri: it reports the dropped `direction` declaration as an error (CSS-001). epubcheck: it reports the dropped `direction` declaration as an error (CSS-001).

- **epubveri: wrong error.** [veripublica/epubveri#144](https://github.com/veripublica/epubveri/issues/144).
- **epubcheck: wrong error.** [w3c/epubcheck#1781](https://github.com/w3c/epubcheck/issues/1781).

Every epubveri finding here is in its default output, except USAGE ADV-019, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p:foo { direction: rtl; }`, in UTF-8.

## History

- 2026-11-20: First version.
