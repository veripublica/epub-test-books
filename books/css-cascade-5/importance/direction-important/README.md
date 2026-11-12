# `direction: rtl !important`

- Book: `direction-important.epub`, built from the EPUB 3 template
- Built by: `scripts/css-cascade-5/importance/direction-important/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { direction: rtl !important; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. !important marks the declaration as important; it is still a direction declaration.

## Question

`style.css` holds `p { direction: rtl !important; }`. Does a validator reject the book?

## Clause

CSS Cascading and Inheritance Level 5, [`importance`](https://www.w3.org/TR/css-cascade-5/#importance) (6.3. Important Declarations: the !important annotation; Candidate Recommendation Snapshot, 13 January 2022):

> A declaration is important if it has a !important annotation as defined by [css-syntax-3], i.e. if the last two (non-whitespace, non-comment) tokens in its value are the delimiter token ! followed by the identifier token important.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. `!important` marks the declaration as important; it is still a `direction` declaration.

CSS result: One rule with one important declaration, `direction: rtl`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i direction-important.epub -u --advisory` | ERROR CSS-001; INVALID | `direction-important.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck direction-important.epub -u` | ERROR CSS-001; INVALID | `direction-important.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { direction: rtl !important; }`, in UTF-8.

## History

- 2026-11-12: First version.
