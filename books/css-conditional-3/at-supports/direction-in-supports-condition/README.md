# `direction: rtl` as an `@supports` condition (valid)

- Book: `direction-in-supports-condition.epub`, built from the EPUB 3 template
- Built by: `scripts/css-conditional-3/at-supports/direction-in-supports-condition/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, after w3c/epub-specs#3115 (held CSS cases)
- Issue: [#666](https://github.com/veripublica/epub-test-books/issues/666)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @supports (direction: rtl) { p { margin: 0; } }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. (direction: rtl) is the condition of the @supports rule: a test of whether the reading system supports that declaration, not a declaration of the style sheet. The parsed style sheet therefore holds no direction property, and EPUB 3.3 forbids only a declared one (w3c/epub-specs#3115).

## Question

`style.css` holds `@supports (direction: rtl) { p { margin: 0; } }`. Does a validator accept the book?

## Clause

CSS Conditional Rules Module Level 3, [`at-supports`](https://www.w3.org/TR/css-conditional-3/#at-supports) (6. Feature queries: the @supports rule; Candidate Recommendation Draft, 15 August 2024):

> The @supports rule is a conditional group rule whose condition tests whether the user agent supports CSS property:value pairs.

> The result is true if the UA supports the declaration within the parentheses.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. `(direction: rtl)` is the condition of the `@supports` rule: a test of whether the reading system supports that declaration, not a declaration of the style sheet. The parsed style sheet holds no `direction` property, it holds no `unicode-bidi` either, and it is UTF-8, so EPUB 3.3 asks nothing more of it.

EPUB 3.3 does not say whether "include" means that the property is declared or only that its name is written in the style sheet, so this set waited for the Working Group. The question went to [w3c/epub-specs#3115](https://github.com/w3c/epub-specs/issues/3115). The [answer](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6880091067) there: "It means the property must be declared." For a checker, "if the parsed sheet produces an object that contains a property with the name 'direction', you should report an error." The issue was closed on 2026-11-19 with the requirement's text unchanged ("[the current spec text stands](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6896967498)"); only the note under it was rewritten, in [w3c/epub-specs#3118](https://github.com/w3c/epub-specs/pull/3118).

CSS result: One `@supports` rule, kept, holding one rule, `p { margin: 0; }`. Its condition, `(direction: rtl)`, is true in any reading system that supports `direction`; it sets nothing.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.50.0 | `epubveri -i direction-in-supports-condition.epub -u --advisory` | no findings; VALID | `direction-in-supports-condition.epubveri-0.50.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-supports-condition.epub -u` | no findings; VALID | `direction-in-supports-condition.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `@supports (direction: rtl) { p { margin: 0; } }`, in UTF-8.

## History

- 2026-11-20: First version.
