# `direction: rtl` after a string broken by a newline

- Book: `direction-after-bad-string.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-string-token/direction-after-bad-string/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: styloria, after its review of the encoding sets
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { content: "open, a newline, then ; direction: rtl; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The newline ends the string as a bad string. The ; on the next line ends the content declaration, and direction: rtl is a declaration of its own.

## Question

`style.css` holds `p { content: "open`, a newline, then `; direction: rtl; }`. Does a validator reject the book?

## Clause

CSS Syntax Level 3, [`consume-string-token`](https://www.w3.org/TR/css-syntax-3/#consume-string-token) (4.3.5 Consume a string token; Candidate Recommendation Draft, 1 October 2026):

> newline
>
> This is a parse error. Reconsume the current input code point, create a <bad-string-token>, and return it.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. The newline ends the string as a bad string. The `;` on the next line ends the `content` declaration, and `direction: rtl` is a declaration of its own.

CSS result: One rule. The `content` declaration holds a bad-string token (a parse error), so its grammar fails and it is dropped: re-read as a rule, it reaches its `;`, a second parse error. `direction: rtl` is kept.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i direction-after-bad-string.epub -u --advisory` | ERROR CSS-001, USAGE CSS-008; INVALID | `direction-after-bad-string.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-after-bad-string.epub -u` | ERROR CSS-008, ERROR CSS-001; INVALID | `direction-after-bad-string.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Besides CSS-001, epubcheck reports CSS-008. This does not change the verdict: the book is invalid for its `direction` declaration.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { content: "open`, a newline, then `; direction: rtl; }`, in UTF-8.

## History

- 2026-11-12: First version.
