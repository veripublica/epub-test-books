# `direction: rtl` inside an `@supports` rule with an invalid condition, `@supports foo` (valid)

- Book: `direction-in-supports-invalid.epub`, built from the EPUB 3 template
- Built by: `scripts/css-conditional-3/at-supports/direction-in-supports-invalid/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, after w3c/epub-specs#3115, from styloria's CSSOM cases
- Issue: [#682](https://github.com/veripublica/epub-test-books/issues/682)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @supports foo { p { direction: rtl; } }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. foo is not in parentheses, so it does not match the @supports grammar, not even <general-enclosed>. The rule is invalid, and CSS ignores it with everything inside it. The parsed style sheet therefore holds no direction property, and EPUB 3.3 forbids only a declared one (w3c/epub-specs#3115).

## Question

`style.css` holds `@supports foo { p { direction: rtl; } }`. Does a validator accept the book?

## Clause

CSS Conditional Rules Module Level 3, [`at-supports`](https://www.w3.org/TR/css-conditional-3/#at-supports) (6. Feature queries: the @supports rule; Candidate Recommendation Draft, 15 August 2024):

> <supports-in-parens> = ( <supports-condition> ) | <supports-feature> | <general-enclosed>

> Any @supports rule that does not parse according to the grammar above (that is, a rule that does not match this loose grammar which includes the <general-enclosed> production) is invalid. Style sheets must not use such a rule and processors must ignore such a rule (including all of its contents).

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. `foo` is not in parentheses, so it does not match the `@supports` grammar, not even `<general-enclosed>`. The rule is invalid, and CSS ignores it with everything inside it. The parsed style sheet holds no `direction` property, it holds no `unicode-bidi` either, and it is UTF-8, so EPUB 3.3 asks nothing more of it.

EPUB 3.3 forbids the property only where the style sheet declares it. The question went to [w3c/epub-specs#3115](https://github.com/w3c/epub-specs/issues/3115). The [answer](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6880091067) there: "It means the property must be declared." For a checker, "if the parsed sheet produces an object that contains a property with the name 'direction', you should report an error." The issue was closed on 2026-11-19 with the requirement's text unchanged ("[the current spec text stands](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6896967498)").

CSS result: No rule is kept. The prelude `foo` does not match `<supports-condition>`, so the `@supports` rule, with the style rule in its block, is ignored.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.48.0 | `epubveri -i direction-in-supports-invalid.epub -u --advisory` | no findings; VALID | `direction-in-supports-invalid.epubveri-0.48.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-supports-invalid.epub -u` | ERROR CSS-001; INVALID | `direction-in-supports-invalid.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the `direction` declaration in the ignored `@supports` rule as an error (CSS-001).

- **epubcheck: wrong error.** [w3c/epubcheck#1781](https://github.com/w3c/epubcheck/issues/1781).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `@supports foo { p { direction: rtl; } }`, in UTF-8.

## History

- 2026-11-21: First version.
