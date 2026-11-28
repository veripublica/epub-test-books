# `direction: rtl` inside a keyframe of `@keyframes`

- Book: `direction-in-keyframe.epub`, built from the EPUB 3 template
- Built by: `scripts/css-animations-1/keyframes/direction-in-keyframe/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, after w3c/epub-specs#3115, from styloria's CSSOM cases
- Issue: [#684](https://github.com/veripublica/epub-test-books/issues/684)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @keyframes k { from { direction: rtl; } }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A keyframe accepts any CSS property except the animation properties, so CSS keeps the declaration, even though direction is not animated. The parsed style sheet therefore holds a direction property, which EPUB 3.3 forbids (w3c/epub-specs#3115).

## Question

`style.css` holds `@keyframes k { from { direction: rtl; } }`. Does a validator reject the book?

## Clause

CSS Animations Level 1, [`keyframes`](https://www.w3.org/TR/css-animations-1/#keyframes) (3. Keyframes; Working Draft, 2 March 2023):

> The <declaration-list> inside of <keyframe-block> accepts any CSS property except those defined in this specification, but does accept the animation-timing-function property and interprets it specially.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. A keyframe accepts any CSS property except the animation properties, so CSS keeps the declaration, even though `direction` is not animated. The parsed style sheet holds a `direction` property, which EPUB 3.3 forbids.

EPUB 3.3 forbids the property only where the style sheet declares it. The question went to [w3c/epub-specs#3115](https://github.com/w3c/epub-specs/issues/3115). The [answer](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6880091067) there: "It means the property must be declared." For a checker, "if the parsed sheet produces an object that contains a property with the name 'direction', you should report an error." The issue was closed on 2026-11-19 with the requirement's text unchanged ("[the current spec text stands](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6896967498)").

CSS result: One `@keyframes k` rule, kept, holding one keyframe, `from`, with one declaration, `direction: rtl`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.50.0 | `epubveri -i direction-in-keyframe.epub -u --advisory` | ERROR CSS-001; INVALID | `direction-in-keyframe.epubveri-0.50.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-keyframe.epub -u` | ERROR CSS-001; INVALID | `direction-in-keyframe.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `@keyframes k { from { direction: rtl; } }`, in UTF-8.

## History

- 2026-11-21: First version.
