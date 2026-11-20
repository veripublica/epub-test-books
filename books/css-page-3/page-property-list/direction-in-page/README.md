# `direction: rtl` inside an `@page` rule

- Book: `direction-in-page.epub`, built from the EPUB 3 template
- Built by: `scripts/css-page-3/page-property-list/direction-in-page/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, after w3c/epub-specs#3115, from styloria's CSSOM cases
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @page { direction: rtl; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. direction is one of the page properties that CSS Paged Media 3 lists for the page context, so CSS keeps the declaration. The parsed style sheet therefore holds a direction property, which EPUB 3.3 forbids (w3c/epub-specs#3115).

## Question

`style.css` holds `@page { direction: rtl; }`. Does a validator reject the book?

## Clause

CSS Paged Media Module Level 3, [`page-property-list`](https://www.w3.org/TR/css-page-3/#page-property-list) (Appendix A: Applicable CSS2.1 Properties; Working Draft, 14 September 2023), which lists `direction` under "bidi properties":

> This list defines the page properties. They are further described in § 6 Page Properties.

CSS Paged Media Module Level 3, [`page-properties`](https://www.w3.org/TR/css-page-3/#page-properties) (6. Page Properties):

> Appendix A defines the normative list of CSS 2.1 [CSS2] properties that apply to page boxes. If a conforming user agent supports any of these properties on block boxes, then it must also support that property in the page context.

CSS Paged Media Module Level 3, [`at-page-rule`](https://www.w3.org/TR/css-page-3/#at-page-rule) (4.1. The @page Rule):

> Properties declared within the page context apply to the page box.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. `direction` is one of the page properties that CSS Paged Media 3 lists for the page context, so CSS keeps the declaration. The parsed style sheet holds a `direction` property, which EPUB 3.3 forbids.

EPUB 3.3 forbids the property only where the style sheet declares it. The question went to [w3c/epub-specs#3115](https://github.com/w3c/epub-specs/issues/3115). The [answer](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6880091067) there: "It means the property must be declared." For a checker, "if the parsed sheet produces an object that contains a property with the name 'direction', you should report an error." The issue was closed on 2026-11-19 with the requirement's text unchanged ("[the current spec text stands](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6896967498)"). Firefox 160 leaves the declaration out of its CSSOM (styloria measured this on 2026-11-20). That is a gap in Firefox, not a rule of CSS, so it does not change the verdict.

CSS result: One `@page` rule, kept, with one declaration, `direction: rtl`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.47.0 | `epubveri -i direction-in-page.epub -u --advisory` | ERROR CSS-001; INVALID | `direction-in-page.epubveri-0.47.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-page.epub -u` | ERROR CSS-001; INVALID | `direction-in-page.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `@page { direction: rtl; }`, in UTF-8.

## History

- 2026-11-21: First version.
