# A stylesheet wrapped in `<!--` and `-->` (valid)

- Book: `cdo-cdc.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-stylesheet-contents/cdo-cdc/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#371](https://github.com/veripublica/epub-test-books/issues/371)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds <!-- p { margin: 0; } -->. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `<!-- p { margin: 0; } -->`. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`consume-stylesheet-contents`](https://www.w3.org/TR/css-syntax-3/#consume-stylesheet-contents) (5.5.1 Consume a stylesheet’s contents; Candidate Recommendation Draft, 1 October 2026):

> <CDO-token>
>
> <CDC-token>
>
> Discard a token from input.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule, `p { margin: 0; }`. No parse error.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i cdo-cdc.epub -u --advisory` | no findings; VALID | `cdo-cdc.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck cdo-cdc.epub -u` | no findings; VALID | `cdo-cdc.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `<!-- p { margin: 0; } -->`, in UTF-8.

## History

- 2026-11-12: First version.
