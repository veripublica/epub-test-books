# A semicolon in a selector, `p; div` (valid)

- Book: `semicolon-in-selector.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-qualified-rule/semicolon-in-selector/build.py`
- Origin: built here
- Expected: valid
- Marks: epubveri: wrong error; epubcheck: wrong error
- Asked for by: styloria, after its review of the encoding sets
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p; div { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `p; div { margin: 0; }`. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`consume-qualified-rule`](https://www.w3.org/TR/css-syntax-3/#consume-qualified-rule) (5.5.3 Consume a qualified rule; Candidate Recommendation Draft, 1 October 2026):

> If rule is valid in the current context, return it; otherwise return an invalid rule error.

CSS Syntax Level 3, [`error-handling`](https://www.w3.org/TR/css-syntax-3/#error-handling) (2.2 Error Handling; Candidate Recommendation Draft, 1 October 2026), a section that is not normative:

> Qualified rules work similarly, except that semicolons don’t end them; instead, they are just taken in as part of the rule’s prelude.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: At the top level a semicolon does not end a qualified rule, so the prelude is `p; div`, which is not a valid selector, and the rule is dropped. No rule is kept, and there is no parse error.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i semicolon-in-selector.epub -u --advisory` | ERROR CSS-008; INVALID | `semicolon-in-selector.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck semicolon-in-selector.epub -u` | ERROR CSS-008; INVALID | `semicolon-in-selector.epubcheck-5.4.0.txt` |

Neither agrees with the expected result. epubveri reports the invalid selector as an error (CSS-008). epubcheck reports the invalid selector as an error (CSS-008).

- **epubveri: wrong error.** epubveri issue pending.
- **epubcheck: wrong error.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p; div { margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
