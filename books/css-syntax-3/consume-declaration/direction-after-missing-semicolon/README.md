# `direction: rtl` after a declaration with no semicolon (valid)

- Book: `direction-after-missing-semicolon.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-declaration/direction-after-missing-semicolon/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#358](https://github.com/veripublica/epub-test-books/issues/358)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { color: red direction: rtl; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Without a semicolon after red, the color declaration runs to the next semicolon, so direction: rtl is part of its value, not a declaration, and the sheet has no direction property.

## Question

`style.css` holds `p { color: red direction: rtl; }`. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`consume-declaration`](https://www.w3.org/TR/css-syntax-3/#consume-declaration) (5.5.6 Consume a declaration; Candidate Recommendation Draft, 1 October 2026):

> Consume a list of component values from input, with nested, and with <semicolon-token> as the stop token, and set decl’s value to the result.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. Without a semicolon after `red`, the `color` declaration runs to the next semicolon, so `direction: rtl` is part of its value, not a declaration, and the sheet has no `direction` property.

CSS result: One rule with one declaration, `color`, whose value is `red direction: rtl`. That value does not match the grammar of `color`, so the declaration is dropped: re-read as a rule, it reaches its `;`, which is a parse error.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i direction-after-missing-semicolon.epub -u --advisory` | USAGE ADV-024; VALID | `direction-after-missing-semicolon.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-after-missing-semicolon.epub -u` | no findings; VALID | `direction-after-missing-semicolon.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output, except USAGE ADV-024, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { color: red direction: rtl; }`, in UTF-8.

## History

- 2026-11-12: First version.
