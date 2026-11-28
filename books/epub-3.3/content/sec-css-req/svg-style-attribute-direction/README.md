# `direction: rtl` in a `style` attribute of inline SVG

- Book: `svg-style-attribute-direction.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-css-req/svg-style-attribute-direction/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, after w3c/epub-specs#3115 (held CSS cases)
- Issue: [#672](https://github.com/veripublica/epub-test-books/issues/672)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml holds an inline svg whose text element is <text x="0" y="15" style="direction: rtl">abc</text>. Everything else is the EPUB 3 template.

Expected result: Invalid. A style attribute holds style sheet rules, so EPUB 3.3's CSS requirements cover it (w3c/epub-specs#3115).

## Question

`content.xhtml` holds `<text x="0" y="15" style="direction: rtl">abc</text>`. Does a validator reject the book?

## Clause

CSS 2.2, [`specificity`](https://www.w3.org/TR/CSS22/cascade.html#specificity) (6.4.3 Calculating a selector's specificity; First Public Working Draft, 12 April 2016):

> In HTML, values of an element's "style" attribute are style sheet rules.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

## Expected result

Invalid. The `style` attribute holds style sheet rules, and they declare `direction`, which EPUB 3.3 forbids.

EPUB 3.3 speaks of "a CSS style sheet", and a `style` attribute holds declarations, not a whole style sheet, so this set waited for the Working Group. The question went to [w3c/epub-specs#3115](https://github.com/w3c/epub-specs/issues/3115). The [answer](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6879045100) there: CSS 2.2 says that "in HTML, values of an element's 'style' attribute are style sheet rules", so "when we ban a property from 'style sheets' that has to filter down to the same style sheet rules being used in the style attribute." The issue was closed on 2026-11-19 with the requirement's text unchanged ("[the current spec text stands](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6896967498)").

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i svg-style-attribute-direction.epub -u --advisory` | ERROR CSS-001; INVALID | `svg-style-attribute-direction.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-style-attribute-direction.epub -u` | no findings; VALID | `svg-style-attribute-direction.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing; it does not read `style` attributes in inline SVG for CSS-001.

- **epubcheck: missed.** [w3c/epubcheck#1781](https://github.com/w3c/epubcheck/issues/1781).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, the body holds `<text x="0" y="15" style="direction: rtl">abc</text>`, and the manifest item of `content.xhtml` has `properties="svg"`.

## History

- 2026-11-20: First version.
