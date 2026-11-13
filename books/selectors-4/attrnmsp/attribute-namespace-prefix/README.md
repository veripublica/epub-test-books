# `[epub|type~="footnote"]` with the `epub` prefix declared (valid)

- Book: `attribute-namespace-prefix.epub`, built from the EPUB 3 template
- Built by: `scripts/selectors-4/attrnmsp/attribute-namespace-prefix/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @namespace epub "http://www.idpf.org/2007/ops";, then [epub|type~="footnote"] { display: none; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `@namespace epub "http://www.idpf.org/2007/ops";`, then `[epub|type~="footnote"] { display: none; }`. Does a validator accept the book?

## Clause

Selectors Level 4, [`attrnmsp`](https://www.w3.org/TR/selectors-4/#attrnmsp) (6.4. Attribute selectors and namespaces; Working Draft, 22 January 2026):

> The attribute name in an attribute selector is given as a CSS qualified name: a namespace prefix that has been previously declared may be prepended to the attribute name separated by the namespace separator "vertical bar" (|).

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One `@namespace` rule and one style rule, kept: every element whose `epub:type` holds `footnote`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i attribute-namespace-prefix.epub -u --advisory` | no findings; VALID | `attribute-namespace-prefix.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck attribute-namespace-prefix.epub -u` | no findings; VALID | `attribute-namespace-prefix.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `@namespace epub "http://www.idpf.org/2007/ops";`, then `[epub|type~="footnote"] { display: none; }`, in UTF-8.

## History

- 2026-11-12: First version.
