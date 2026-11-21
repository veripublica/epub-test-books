# A block open at EOF whose last `}` is escaped, `p { ; \}` (valid)

- Book: `eof-escaped-brace.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-block-contents/eof-escaped-brace/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: styloria, for its 0.21 release (note 2026-11-18)
- Issue: [#657](https://github.com/veripublica/epub-test-books/issues/657)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { ; \} and nothing after it: the last byte of the file is the }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `p { ; \}` and nothing after it: the last byte of the file is the `}`. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`starts-with-a-valid-escape`](https://www.w3.org/TR/css-syntax-3/#starts-with-a-valid-escape) (4.3.8. Check if two code points are a valid escape; Candidate Recommendation Draft, 1 October 2026):

> If the first code point is not U+005C REVERSE SOLIDUS (\), return false.
>
> Otherwise, if the second code point is a newline, return false.
>
> Otherwise, return true.

CSS Syntax Level 3, [`consume-block-contents`](https://www.w3.org/TR/css-syntax-3/#consume-block-contents) (5.5.5. Consume a block’s contents; Candidate Recommendation Draft, 1 October 2026):

> <EOF-token>
>
> <}-token>
>
> Return rules.

> Mark input.
>
> Consume a declaration from input, with nested set to true. If a declaration was returned, append it to decls, and discard a mark from input.
>
> Otherwise, restore a mark from input, then consume a qualified rule from input, with nested set to true, and <semicolon-token> as the stop token.

CSS Syntax Level 3, [`consume-declaration`](https://www.w3.org/TR/css-syntax-3/#consume-declaration) (5.5.6. Consume a declaration; Candidate Recommendation Draft, 1 October 2026):

> If the next token is an <ident-token>, consume a token from input and set decl's name to the token’s value.
>
> Otherwise, consume the remnants of a bad declaration from input, with nested, and return nothing.

CSS Syntax Level 3, [`consume-qualified-rule`](https://www.w3.org/TR/css-syntax-3/#consume-qualified-rule) (5.5.3. Consume a qualified rule; Candidate Recommendation Draft, 1 October 2026):

> <EOF-token>
>
> stop token (if passed)
>
> This is a parse error. Return nothing.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule, `p`, with no declarations. `\}` is a valid escape, so it starts an ident whose value is `}`. The ident is not followed by a colon, so it is not a declaration; re-read as a rule it reaches EOF, a parse error, and nothing is added. The block is never closed; it ends at EOF.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.48.0 | `epubveri -i eof-escaped-brace.epub -u --advisory` | USAGE CSS-008, USAGE CSS-008; VALID | `eof-escaped-brace.epubveri-0.48.0.txt` |
| epubcheck 5.4.0 | `epubcheck eof-escaped-brace.epub -u` | ERROR CSS-008; INVALID | `eof-escaped-brace.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the parse errors as errors (CSS-008).

- **epubcheck: wrong error.** [w3c/epubcheck#1768](https://github.com/w3c/epubcheck/issues/1768).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { ; \}` and nothing after it: the last byte of the file is the `}`, in UTF-8.

## History

- 2026-11-18: First version.
