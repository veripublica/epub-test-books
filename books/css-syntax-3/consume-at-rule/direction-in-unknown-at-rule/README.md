# `direction: rtl` inside an unknown at-rule, `@foo { … }` (valid)

- Book: `direction-in-unknown-at-rule.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-at-rule/direction-in-unknown-at-rule/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, after w3c/epub-specs#3115 (held CSS cases)
- Issue: [#667](https://github.com/veripublica/epub-test-books/issues/667)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @foo { p { direction: rtl; } }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. @foo is not a CSS at-rule, so CSS drops it with everything inside it. The parsed style sheet therefore holds no direction property, and EPUB 3.3 forbids only a declared one (w3c/epub-specs#3115).

## Question

`style.css` holds `@foo { p { direction: rtl; } }`. Does a validator accept the book?

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

Valid. `@foo` is not a CSS at-rule, so CSS drops it with everything inside it. The parsed style sheet holds no `direction` property, it holds no `unicode-bidi` either, and it is UTF-8, so EPUB 3.3 asks nothing more of it.

EPUB 3.3 does not say whether "include" means that the property is declared or only that its name is written in the style sheet, so this set waited for the Working Group. The question went to [w3c/epub-specs#3115](https://github.com/w3c/epub-specs/issues/3115). The [answer](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6880091067) there: "It means the property must be declared." For a checker, "if the parsed sheet produces an object that contains a property with the name 'direction', you should report an error." The issue was closed on 2026-11-19 with the requirement's text unchanged ("[the current spec text stands](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6896967498)"); only the note under it was rewritten, in [w3c/epub-specs#3118](https://github.com/w3c/epub-specs/pull/3118).

CSS result: No rule is kept. `@foo` is not valid in a stylesheet, so the at-rule, with the style rule in its block, is dropped, which is a parse error.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i direction-in-unknown-at-rule.epub -u --advisory` | USAGE ADV-020; VALID | `direction-in-unknown-at-rule.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-unknown-at-rule.epub -u` | ERROR CSS-001; INVALID | `direction-in-unknown-at-rule.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the dropped `direction` declaration as an error (CSS-001).

- **epubcheck: wrong error.** [w3c/epubcheck#1781](https://github.com/w3c/epubcheck/issues/1781).

Every epubveri finding here is in its default output, except USAGE ADV-020, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `@foo { p { direction: rtl; } }`, in UTF-8.

## History

- 2026-11-20: First version.
