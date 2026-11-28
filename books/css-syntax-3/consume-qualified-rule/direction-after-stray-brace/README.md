# `direction: rtl` in a rule after a stray `}`, `} p { … }` (valid)

- Book: `direction-after-stray-brace.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-qualified-rule/direction-after-stray-brace/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, after w3c/epub-specs#3115 (held CSS cases)
- Issue: [#668](https://github.com/veripublica/epub-test-books/issues/668)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds } p { direction: rtl; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The stray } becomes part of the selector, } p, which is invalid, so CSS drops the rule. The parsed style sheet therefore holds no direction property, and EPUB 3.3 forbids only a declared one (w3c/epub-specs#3115).

## Question

`style.css` holds `} p { direction: rtl; }`. Does a validator accept the book?

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

Valid. The stray `}` becomes part of the selector, `} p`, which is invalid, so CSS drops the rule. The parsed style sheet holds no `direction` property, it holds no `unicode-bidi` either, and it is UTF-8, so EPUB 3.3 asks nothing more of it.

EPUB 3.3 does not say whether "include" means that the property is declared or only that its name is written in the style sheet, so this set waited for the Working Group. The question went to [w3c/epub-specs#3115](https://github.com/w3c/epub-specs/issues/3115). The [answer](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6880091067) there: "It means the property must be declared." For a checker, "if the parsed sheet produces an object that contains a property with the name 'direction', you should report an error." The issue was closed on 2026-11-19 with the requirement's text unchanged ("[the current spec text stands](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6896967498)"); only the note under it was rewritten, in [w3c/epub-specs#3118](https://github.com/w3c/epub-specs/pull/3118).

CSS result: The `}` is a parse error and becomes part of a qualified rule's prelude, `} p`, which is not a valid selector, so the rule is dropped, a second parse error. No rule is kept.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i direction-after-stray-brace.epub -u --advisory` | USAGE CSS-008; VALID | `direction-after-stray-brace.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-after-stray-brace.epub -u` | ERROR CSS-008; INVALID | `direction-after-stray-brace.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the parse error as an error (CSS-008).

- **epubcheck: wrong error.** [w3c/epubcheck#1768](https://github.com/w3c/epubcheck/issues/1768).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `} p { direction: rtl; }`, in UTF-8.

## History

- 2026-11-20: First version.
