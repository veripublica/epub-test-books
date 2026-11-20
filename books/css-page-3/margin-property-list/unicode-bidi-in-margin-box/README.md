# `unicode-bidi: bidi-override` inside a page-margin box of `@page`

- Book: `unicode-bidi-in-margin-box.epub`, built from the EPUB 3 template
- Built by: `scripts/css-page-3/margin-property-list/unicode-bidi-in-margin-box/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, after w3c/epub-specs#3115, from styloria's CSSOM cases
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @page { @top-center { content: "x"; unicode-bidi: bidi-override; } }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. unicode-bidi is one of the page-margin properties that CSS Paged Media 3 lists for the margin context, so CSS keeps the declaration. The parsed style sheet therefore holds a unicode-bidi property, which EPUB 3.3 forbids (w3c/epub-specs#3115).

## Question

`style.css` holds `@page { @top-center { content: "x"; unicode-bidi: bidi-override; } }`. Does a validator reject the book?

## Clause

CSS Paged Media Module Level 3, [`margin-property-list`](https://www.w3.org/TR/css-page-3/#margin-property-list) (Appendix A: Applicable CSS2.1 Properties; Working Draft, 14 September 2023), which lists `direction` and `unicode-bidi` under "bidi properties":

> This list defines the page-margin properties. They are further described in § 6 Page Properties.

CSS Paged Media Module Level 3, [`page-properties`](https://www.w3.org/TR/css-page-3/#page-properties) (6. Page Properties):

> The same appendix defines the normative list of CSS 2.1 [CSS2] properties that apply to page-margin boxes. If a conforming user agent supports any of these properties on block boxes, then it must also support that property in the margin context.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. `unicode-bidi` is one of the page-margin properties that CSS Paged Media 3 lists for the margin context, so CSS keeps the declaration. The parsed style sheet holds a `unicode-bidi` property, which EPUB 3.3 forbids.

EPUB 3.3 forbids the property only where the style sheet declares it. The question went to [w3c/epub-specs#3115](https://github.com/w3c/epub-specs/issues/3115). The [answer](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6880091067) there: "It means the property must be declared." For a checker, "if the parsed sheet produces an object that contains a property with the name 'direction', you should report an error." The issue was closed on 2026-11-19 with the requirement's text unchanged ("[the current spec text stands](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6896967498)").

CSS result: One `@page` rule, kept, holding one `@top-center` margin rule with two declarations, `content: "x"` and `unicode-bidi: bidi-override`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.47.0 | `epubveri -i unicode-bidi-in-margin-box.epub -u --advisory` | ERROR CSS-001; INVALID | `unicode-bidi-in-margin-box.epubveri-0.47.0.txt` |
| epubcheck 5.4.0 | `epubcheck unicode-bidi-in-margin-box.epub -u` | ERROR CSS-001; INVALID | `unicode-bidi-in-margin-box.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `@page { @top-center { content: "x"; unicode-bidi: bidi-override; } }`, in UTF-8.

## History

- 2026-11-21: First version.
