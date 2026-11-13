# A custom property whose value holds a `{}` block (valid)

- Book: `custom-property-block.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-declaration/custom-property-block/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#357](https://github.com/veripublica/epub-test-books/issues/357)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { --x: { a: b }; margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `p { --x: { a: b }; margin: 0; }`. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`consume-declaration`](https://www.w3.org/TR/css-syntax-3/#consume-declaration) (5.5.6 Consume a declaration; Candidate Recommendation Draft, 1 October 2026):

> If decl’s name is a custom property name string, then set decl’s original text to the segment of the original source text string corresponding to the tokens of decl’s value.
>
> Otherwise, if decl’s value contains a top-level simple block with an associated token of <{-token>, and also contains any other non-<whitespace-token> value, return nothing. (That is, a top-level {}-block is only allowed as the entire value of a non-custom property.)

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule with two declarations: the custom property `--x`, whose value is the block `{ a: b }`, and `margin: 0`. No parse error.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i custom-property-block.epub -u --advisory` | no findings; VALID | `custom-property-block.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck custom-property-block.epub -u` | ERROR CSS-008, ERROR CSS-008; INVALID | `custom-property-block.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the block in the custom property as errors (CSS-008).

- **epubcheck: wrong error.** [w3c/epubcheck#1768](https://github.com/w3c/epubcheck/issues/1768).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { --x: { a: b }; margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
