# An unquoted `url()` with a space inside (valid)

- Book: `bad-url.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-url-token/bad-url/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#373](https://github.com/veripublica/epub-test-books/issues/373)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { background: url(a b); margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements. A bad url is not a URL, so it refers to no resource.

## Question

`style.css` holds `p { background: url(a b); margin: 0; }`. Does a validator accept the book?

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

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements. A bad url is not a URL, so it refers to no resource.

CSS result: One rule. The `background` declaration holds a bad-url token (a parse error), so its grammar fails and it is dropped: re-read as a rule, it reaches its `;`, a second parse error. `margin: 0` is kept.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i bad-url.epub -u --advisory` | USAGE ADV-015; VALID | `bad-url.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck bad-url.epub -u` | ERROR RSC-020, ERROR RSC-007; INVALID | `bad-url.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reads the bad url as a reference, and reports it as missing (RSC-007) and not valid (RSC-020).

- **epubcheck: wrong error.** [w3c/epubcheck#1768](https://github.com/w3c/epubcheck/issues/1768).

Every epubveri finding here is in its default output, except USAGE ADV-015, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { background: url(a b); margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
