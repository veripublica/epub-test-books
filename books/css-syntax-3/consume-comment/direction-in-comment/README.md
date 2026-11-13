# `direction: rtl` inside a comment (valid)

- Book: `direction-in-comment.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-comment/direction-in-comment/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#354](https://github.com/veripublica/epub-test-books/issues/354)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds /* p { direction: rtl; } */, then p { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The declaration is inside a comment, which the tokenizer consumes and drops, so the sheet has no direction property.

## Question

`style.css` holds `/* p { direction: rtl; } */`, then `p { margin: 0; }`. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`consume-comment`](https://www.w3.org/TR/css-syntax-3/#consume-comment) (4.3.2 Consume comments; Candidate Recommendation Draft, 1 October 2026):

> If the next two input code point are U+002F SOLIDUS (/) followed by a U+002A ASTERISK (*), consume them and all following code points up to and including the first U+002A ASTERISK (*) followed by a U+002F SOLIDUS (/), or up to an EOF code point.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The declaration is inside a comment, which the tokenizer consumes and drops, so the sheet has no `direction` property.

CSS result: One rule, `p { margin: 0; }`. The comment produces no token.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i direction-in-comment.epub -u --advisory` | no findings; VALID | `direction-in-comment.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-comment.epub -u` | no findings; VALID | `direction-in-comment.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `/* p { direction: rtl; } */`, then `p { margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
