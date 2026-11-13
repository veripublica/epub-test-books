# A bad url whose remnants end at the first `)`, before `direction: rtl`

- Book: `direction-in-bad-url.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-url-token/direction-in-bad-url/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#375](https://github.com/veripublica/epub-test-books/issues/375)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { background: url(a(b); direction: rtl; ); }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The ( inside an unquoted url( makes a bad url, and its remnants end at the first ), the one right after b. So the bad url is url(a(b), the ; after it ends the background declaration, and direction: rtl is a declaration of its own.

## Question

`style.css` holds `p { background: url(a(b); direction: rtl; ); }`. Does a validator reject the book?

## Clause

CSS Syntax Level 3, [`consume-url-token`](https://www.w3.org/TR/css-syntax-3/#consume-url-token) (4.3.6 Consume a url token; Candidate Recommendation Draft, 1 October 2026):

> U+0022 QUOTATION MARK (")
>
> U+0027 APOSTROPHE (')
>
> U+0028 LEFT PARENTHESIS (()
>
> non-printable code point
>
> This is a parse error. Consume the remnants of a bad url, create a <bad-url-token>, and return it.

CSS Syntax Level 3, [`consume-remnants-of-bad-url`](https://www.w3.org/TR/css-syntax-3/#consume-remnants-of-bad-url) (4.3.15 Consume the remnants of a bad url; Candidate Recommendation Draft, 1 October 2026):

> Repeatedly consume the next input code point from the stream:
>
> U+0029 RIGHT PARENTHESIS ())
>
> EOF
>
> Return.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. The `(` inside an unquoted `url(` makes a bad url, and its remnants end at the first `)`, the one right after `b`. So the bad url is `url(a(b)`, the `;` after it ends the `background` declaration, and `direction: rtl` is a declaration of its own.

CSS result: One rule. The `(` makes a bad-url token, `url(a(b)` (a parse error). The `background` declaration that holds it is dropped: re-read as a rule, it reaches its `;`, a second parse error. `direction: rtl` is kept. The lone `)` after it is not a declaration, and re-read as a rule it reaches the last `;`: a third parse error.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i direction-in-bad-url.epub -u --advisory` | ERROR CSS-001, USAGE ADV-015, USAGE CSS-008; INVALID | `direction-in-bad-url.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-bad-url.epub -u` | ERROR CSS-001, ERROR CSS-008, ERROR RSC-007; INVALID | `direction-in-bad-url.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Besides CSS-001, epubcheck reports CSS-008, RSC-007. This does not change the verdict: the book is invalid for its `direction` declaration.

Every epubveri finding here is in its default output, except USAGE ADV-015, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { background: url(a(b); direction: rtl; ); }`, in UTF-8.

## History

- 2026-11-12: First version.
- 2026-11-13: Expected result changed from valid to invalid. The remnants of the bad url end at the first `)`, after `b`, not after `direction: rtl;`, so `direction` is declared. epubveri and styloria pointed it out (§4.3.15); the set first meant is now `direction-in-bad-url-quote`.
