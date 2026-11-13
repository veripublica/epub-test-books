# `direction: rtl` in a block that is never closed

- Book: `direction-in-unclosed-block.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-block-contents/direction-in-unclosed-block/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed, wrong error
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#351](https://github.com/veripublica/epub-test-books/issues/351)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { direction: rtl, and the file ends there. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The block and the declaration are closed at EOF, so direction: rtl is a declaration.

## Question

`style.css` holds `p { direction: rtl`, and the file ends there. Does a validator reject the book?

## Clause

CSS Syntax Level 3, [`consume-block-contents`](https://www.w3.org/TR/css-syntax-3/#consume-block-contents) (5.5.5 Consume a block’s contents; Candidate Recommendation Draft, 1 October 2026):

> <EOF-token>
>
> <}-token>
>
> Return rules.

CSS Syntax Level 3, [`error-handling`](https://www.w3.org/TR/css-syntax-3/#error-handling) (2.2 Error Handling; Candidate Recommendation Draft, 1 October 2026), a section that is not normative:

> If the stylesheet ends while any rule, declaration, function, string, etc. are still open, everything is automatically closed.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. The block and the declaration are closed at EOF, so `direction: rtl` is a declaration.

CSS result: One rule, `p`, with one declaration, `direction: rtl`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i direction-in-unclosed-block.epub -u --advisory` | ERROR CSS-001, USAGE CSS-008; INVALID | `direction-in-unclosed-block.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-unclosed-block.epub -u` | ERROR CSS-008; INVALID | `direction-in-unclosed-block.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it does not report `direction` (no CSS-001), and reports the unclosed block as an error (CSS-008).

- **epubcheck: missed, wrong error.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { direction: rtl`, and the file ends there, in UTF-8.

## History

- 2026-11-12: First version.
