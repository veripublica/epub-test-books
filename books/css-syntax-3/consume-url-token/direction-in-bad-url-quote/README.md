# `direction: rtl` inside the remnants of a bad url (valid)

- Book: `direction-in-bad-url-quote.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-url-token/direction-in-bad-url-quote/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: styloria, after its review of the tokenizer sets
- Issue: [#376](https://github.com/veripublica/epub-test-books/issues/376)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { background: url(a"b; direction: rtl; ); }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The " inside an unquoted url( makes a bad url, and its remnants run to the first ), after direction: rtl;. So direction: rtl is part of that token, not a declaration, and the sheet has no direction property. A bad url is not a URL, so it refers to no resource.

## Question

`style.css` holds `p { background: url(a"b; direction: rtl; ); }`. Does a validator accept the book?

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

Valid. The `"` inside an unquoted `url(` makes a bad url, and its remnants run to the first `)`, after `direction: rtl;`. So `direction: rtl` is part of that token, not a declaration, and the sheet has no `direction` property. A bad url is not a URL, so it refers to no resource.

CSS result: One rule. The `background` declaration holds the bad-url token (a parse error), so its grammar fails and it is dropped: re-read as a rule, it reaches its `;`, a second parse error. Nothing else is declared.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i direction-in-bad-url-quote.epub -u --advisory` | USAGE ADV-015; VALID | `direction-in-bad-url-quote.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-bad-url-quote.epub -u` | ERROR RSC-020, ERROR RSC-007; INVALID | `direction-in-bad-url-quote.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reads the bad url as a reference, and reports it as not valid (RSC-020) and missing (RSC-007).

- **epubcheck: wrong error.** [w3c/epubcheck#1768](https://github.com/w3c/epubcheck/issues/1768).

Every epubveri finding here is in its default output, except USAGE ADV-015, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { background: url(a"b; direction: rtl; ); }`, in UTF-8.

## History

- 2026-11-13: First version.
