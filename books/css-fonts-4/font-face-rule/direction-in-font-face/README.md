# `direction: rtl` inside an `@font-face` rule (valid)

- Book: `direction-in-font-face.epub`, built from the EPUB 3 template
- Built by: `scripts/css-fonts-4/font-face-rule/direction-in-font-face/build.py`
- Origin: built here
- Expected: valid
- Marks: epubveri: wrong error; epubcheck: wrong error
- Asked for by: the maintainer, after w3c/epub-specs#3115, from styloria's CSSOM cases
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @font-face { font-family: x; direction: rtl; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. @font-face holds descriptors, not properties, and it has no direction descriptor, so CSS ignores the declaration. The parsed style sheet therefore holds no direction property, and EPUB 3.3 forbids only a declared one (w3c/epub-specs#3115).

## Question

`style.css` holds `@font-face { font-family: x; direction: rtl; }`. Does a validator accept the book?

## Clause

CSS Fonts Module Level 4, [`font-face-rule`](https://www.w3.org/TR/css-fonts-4/#font-face-rule) (4.1. The @font-face rule; Working Draft, 12 November 2026):

> This at-rule follows the forward-compatible parsing rules of CSS. Like properties in a declaration block, declarations of any descriptors that are not supported by the user agent must be ignored.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. `@font-face` holds descriptors, not properties, and it has no `direction` descriptor, so CSS ignores the declaration. The parsed style sheet holds no `direction` property, it holds no `unicode-bidi` either, and it is UTF-8, so EPUB 3.3 asks nothing more of it.

EPUB 3.3 forbids the property only where the style sheet declares it. The question went to [w3c/epub-specs#3115](https://github.com/w3c/epub-specs/issues/3115). The [answer](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6880091067) there: "It means the property must be declared." For a checker, "if the parsed sheet produces an object that contains a property with the name 'direction', you should report an error." The issue was closed on 2026-11-19 with the requirement's text unchanged ("[the current spec text stands](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6896967498)").

CSS result: One `@font-face` rule, kept, with one descriptor, `font-family: x`. `direction` is not an `@font-face` descriptor, so its declaration is ignored.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.47.0 | `epubveri -i direction-in-font-face.epub -u --advisory` | ERROR CSS-001, USAGE CSS-028, USAGE ADV-002; INVALID | `direction-in-font-face.epubveri-0.47.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-font-face.epub -u` | USAGE CSS-028, ERROR CSS-001, USAGE CSS-028; INVALID | `direction-in-font-face.epubcheck-5.4.0.txt` |

Neither agrees with the expected result. epubveri: it reports the ignored `direction` declaration in `@font-face` as an error (CSS-001), although its own USAGE ADV-002 says that `direction` is not an `@font-face` descriptor. epubcheck: it reports the ignored `direction` declaration in `@font-face` as an error (CSS-001).

- **epubveri: wrong error.** [veripublica/epubveri#144](https://github.com/veripublica/epubveri/issues/144).
- **epubcheck: wrong error.** [w3c/epubcheck#1781](https://github.com/w3c/epubcheck/issues/1781).

Every epubveri finding here is in its default output, except USAGE ADV-002, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `@font-face { font-family: x; direction: rtl; }`, in UTF-8.

## History

- 2026-11-21: First version.
