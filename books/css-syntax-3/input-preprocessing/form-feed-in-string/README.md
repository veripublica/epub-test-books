# A U+000C FORM FEED inside a string (valid)

- Book: `form-feed-in-string.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/input-preprocessing/form-feed-in-string/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#377](https://github.com/veripublica/epub-test-books/issues/377)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { content: "a, a U+000C FORM FEED, then b"; margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `p { content: "a`, a U+000C FORM FEED, then `b"; margin: 0; }`. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`input-preprocessing`](https://www.w3.org/TR/css-syntax-3/#input-preprocessing) (3.3 Preprocessing the input stream; Candidate Recommendation Draft, 1 October 2026):

> Replace any U+000D CARRIAGE RETURN (CR) code points, U+000C FORM FEED (FF) code points, or pairs of U+000D CARRIAGE RETURN (CR) followed by U+000A LINE FEED (LF) in input by a single U+000A LINE FEED (LF) code point.

CSS Syntax Level 3, [`consume-string-token`](https://www.w3.org/TR/css-syntax-3/#consume-string-token) (4.3.5 Consume a string token; Candidate Recommendation Draft, 1 October 2026):

> newline
>
> This is a parse error. Reconsume the current input code point, create a <bad-string-token>, and return it.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: Preprocessing turns the form feed into a newline, so the string ends there as a bad string (a parse error). `b` follows, and its `"` opens a second string, which takes in `; margin: 0; }` and is broken by the newline at the end of the line: a second bad string. The rule is closed at EOF. Its one declaration, `content`, is dropped: re-read as a rule, it reaches EOF, a third parse error. `margin: 0` is never declared.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i form-feed-in-string.epub -u --advisory` | USAGE CSS-008, USAGE CSS-008, USAGE CSS-008; VALID | `form-feed-in-string.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck form-feed-in-string.epub -u` | ERROR CSS-008; INVALID | `form-feed-in-string.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the broken string as an error (CSS-008).

- **epubcheck: wrong error.** [w3c/epubcheck#1768](https://github.com/w3c/epubcheck/issues/1768).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { content: "a`, a U+000C FORM FEED, then `b"; margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
