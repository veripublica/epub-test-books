# A rule whose block is never closed (valid)

- Book: `unclosed-block.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-block-contents/unclosed-block/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#353](https://github.com/veripublica/epub-test-books/issues/353)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { margin: 0, and the file ends there. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `p { margin: 0`, and the file ends there. Does a validator accept the book?

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

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule, `p { margin: 0; }`: the block and the declaration are closed at EOF. No parse error is defined for this.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i unclosed-block.epub -u --advisory` | USAGE CSS-008; VALID | `unclosed-block.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck unclosed-block.epub -u` | ERROR CSS-008; INVALID | `unclosed-block.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the unclosed block as an error (CSS-008).

- **epubcheck: wrong error.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { margin: 0`, and the file ends there, in UTF-8.

## History

- 2026-11-12: First version.
