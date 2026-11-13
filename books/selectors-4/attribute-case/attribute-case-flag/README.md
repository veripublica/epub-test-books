# An attribute selector with the `i` flag, `[lang="EN" i]` (valid)

- Book: `attribute-case-flag.epub`, built from the EPUB 3 template
- Built by: `scripts/selectors-4/attribute-case/attribute-case-flag/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#393](https://github.com/veripublica/epub-test-books/issues/393)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds [lang="EN" i] { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `[lang="EN" i] { margin: 0; }`. Does a validator accept the book?

## Clause

Selectors Level 4, [`attribute-case`](https://www.w3.org/TR/selectors-4/#attribute-case) (6.3. Case-sensitivity; Working Draft, 22 January 2026):

> To match attribute values ASCII case-insensitively regardless of document language rules, the attribute selector may include the identifier i before the closing bracket (]). When this flag is present, UAs must match the attribute’s value ASCII case-insensitively (i.e. [a-z] and [A-Z] are considered equivalent).

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule, kept: every element whose `lang` is `en` in any case, which in this book is the `html` element.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i attribute-case-flag.epub -u --advisory` | no findings; VALID | `attribute-case-flag.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck attribute-case-flag.epub -u` | ERROR CSS-008; INVALID | `attribute-case-flag.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the `i` flag as an error (CSS-008).

- **epubcheck: wrong error.** [w3c/epubcheck#1768](https://github.com/w3c/epubcheck/issues/1768).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `[lang="EN" i] { margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
