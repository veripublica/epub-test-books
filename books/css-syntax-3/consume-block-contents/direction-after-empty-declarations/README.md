# `direction: rtl` after an empty declaration, `;;`

- Book: `direction-after-empty-declarations.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-block-contents/direction-after-empty-declarations/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#349](https://github.com/veripublica/epub-test-books/issues/349)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { color: red;; direction: rtl }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A lone semicolon inside a block is discarded, so direction: rtl is a declaration. The last declaration needs no semicolon.

## Question

`style.css` holds `p { color: red;; direction: rtl }`. Does a validator reject the book?

## Clause

CSS Syntax Level 3, [`consume-block-contents`](https://www.w3.org/TR/css-syntax-3/#consume-block-contents) (5.5.5 Consume a block’s contents; Candidate Recommendation Draft, 1 October 2026):

> <whitespace-token>
>
> <semicolon-token>
>
> Discard a token from input.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. A lone semicolon inside a block is discarded, so `direction: rtl` is a declaration. The last declaration needs no semicolon.

CSS result: One rule with two declarations, `color: red` and `direction: rtl`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i direction-after-empty-declarations.epub -u --advisory` | ERROR CSS-001; INVALID | `direction-after-empty-declarations.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-after-empty-declarations.epub -u` | ERROR CSS-001; INVALID | `direction-after-empty-declarations.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { color: red;; direction: rtl }`, in UTF-8.

## History

- 2026-11-12: First version.
