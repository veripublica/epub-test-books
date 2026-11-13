# `direction: rtl` in a string continued over a line with a backslash (valid)

- Book: `direction-in-continued-string.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-string-token/direction-in-continued-string/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#369](https://github.com/veripublica/epub-test-books/issues/369)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { content: "a\, a newline, then direction: rtl;"; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. A backslash before a newline continues the string, so direction: rtl; is part of the string's value, and the sheet has no direction property.

## Question

`style.css` holds `p { content: "a\`, a newline, then `direction: rtl;"; }`. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`consume-string-token`](https://www.w3.org/TR/css-syntax-3/#consume-string-token) (4.3.5 Consume a string token; Candidate Recommendation Draft, 1 October 2026):

> U+005C REVERSE SOLIDUS (\)
>
> If the next input code point is EOF, do nothing.
>
> Otherwise, if the next input code point is a newline, consume it.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. A backslash before a newline continues the string, so `direction: rtl;` is part of the string's value, and the sheet has no `direction` property.

CSS result: One rule with one declaration, `content`, whose value is the string `adirection: rtl;` (the escaped newline is dropped).

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i direction-in-continued-string.epub -u --advisory` | no findings; VALID | `direction-in-continued-string.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-continued-string.epub -u` | no findings; VALID | `direction-in-continued-string.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { content: "a\`, a newline, then `direction: rtl;"; }`, in UTF-8.

## History

- 2026-11-12: First version.
