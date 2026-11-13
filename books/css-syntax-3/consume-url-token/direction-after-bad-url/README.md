# `direction: rtl` after a bad url

- Book: `direction-after-bad-url.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-url-token/direction-after-bad-url/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#374](https://github.com/veripublica/epub-test-books/issues/374)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { background: url(a b); direction: rtl; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The space inside the unquoted url( makes a bad url, whose remnants end at ). The ; ends the background declaration, and direction: rtl is a declaration of its own.

## Question

`style.css` holds `p { background: url(a b); direction: rtl; }`. Does a validator reject the book?

## Clause

CSS Syntax Level 3, [`consume-url-token`](https://www.w3.org/TR/css-syntax-3/#consume-url-token) (4.3.6 Consume a url token; Candidate Recommendation Draft, 1 October 2026):

> whitespace
>
> Consume as much whitespace as possible. If the next input code point is U+0029 RIGHT PARENTHESIS ()) or EOF, consume it and return the <url-token> (if EOF was encountered, this is a parse error); otherwise, consume the remnants of a bad url, create a <bad-url-token>, and return it.

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

Invalid. The space inside the unquoted `url(` makes a bad url, whose remnants end at `)`. The `;` ends the `background` declaration, and `direction: rtl` is a declaration of its own.

CSS result: One rule. The `background` declaration holds a bad-url token (a parse error), so its grammar fails and it is dropped: re-read as a rule, it reaches its `;`, a second parse error. `direction: rtl` is kept.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i direction-after-bad-url.epub -u --advisory` | ERROR CSS-001, USAGE ADV-015; INVALID | `direction-after-bad-url.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-after-bad-url.epub -u` | ERROR RSC-020, ERROR CSS-001, ERROR RSC-007; INVALID | `direction-after-bad-url.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Besides CSS-001, epubcheck reports RSC-007, RSC-020. This does not change the verdict: the book is invalid for its `direction` declaration.

Every epubveri finding here is in its default output, except USAGE ADV-015, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { background: url(a b); direction: rtl; }`, in UTF-8.

## History

- 2026-11-12: First version.
