# `direction: rtl` inside a comment that is never closed (valid)

- Book: `direction-in-unclosed-comment.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-comment/direction-in-unclosed-comment/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#355](https://github.com/veripublica/epub-test-books/issues/355)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { margin: 0; }, then /* direction: rtl; with no */ before the end of the file. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. A comment runs to EOF when it is not closed, so direction: rtl; is inside it, and the sheet has no direction property.

## Question

`style.css` holds `p { margin: 0; }`, then `/* direction: rtl;` with no `*/` before the end of the file. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`consume-comment`](https://www.w3.org/TR/css-syntax-3/#consume-comment) (4.3.2 Consume comments; Candidate Recommendation Draft, 1 October 2026):

> If the next two input code point are U+002F SOLIDUS (/) followed by a U+002A ASTERISK (*), consume them and all following code points up to and including the first U+002A ASTERISK (*) followed by a U+002F SOLIDUS (/), or up to an EOF code point.

> If the preceding paragraph ended by consuming an EOF code point, this is a parse error.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. A comment runs to EOF when it is not closed, so `direction: rtl;` is inside it, and the sheet has no `direction` property.

CSS result: One rule, `p { margin: 0; }`. The unclosed comment is a parse error and produces no token.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i direction-in-unclosed-comment.epub -u --advisory` | USAGE CSS-008; VALID | `direction-in-unclosed-comment.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-unclosed-comment.epub -u` | ERROR CSS-008; INVALID | `direction-in-unclosed-comment.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the unclosed comment as an error (CSS-008).

- **epubcheck: wrong error.** [w3c/epubcheck#1768](https://github.com/w3c/epubcheck/issues/1768).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { margin: 0; }`, then `/* direction: rtl;` with no `*/` before the end of the file, in UTF-8.

## History

- 2026-11-12: First version.
