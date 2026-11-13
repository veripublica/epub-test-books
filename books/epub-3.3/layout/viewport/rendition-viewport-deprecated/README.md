# The deprecated `rendition:viewport` property

- Book: `rendition-viewport-deprecated.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/viewport/rendition-viewport-deprecated/build.py`
- Origin: built here
- Expected: valid, with a warning for the deprecated property
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#260](https://github.com/veripublica/epub-test-books/issues/260)
- Other clauses: `deprecated`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package also declares rendition:viewport with width=1200, height=600. The property is deprecated. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid, because using a deprecated feature is a SHOULD NOT, not a MUST NOT. A validator should warn about it.

## Question

The fixed-layout package also declares `rendition:viewport` with `width=1200, height=600`. The property is deprecated. What does a validator report?

## Clause

EPUB 3.3, [`viewport`](https://www.w3.org/TR/epub-33/#viewport):

> The rendition:viewport property allows EPUB creators to express the CSS initial containing block (ICB) [css2] for XHTML and SVG content documents whose rendition:layout property has been set to pre-paginated. Use of the property is deprecated.

EPUB 3.3, [`deprecated`](https://www.w3.org/TR/epub-33/#deprecated):

> If this specification designates a feature as deprecated, EPUB creators SHOULD NOT use the feature in their EPUB publications.

## Expected result

Valid, because using a deprecated feature is a SHOULD NOT, not a MUST NOT. A validator should warn about it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i rendition-viewport-deprecated.epub -u --advisory` | WARNING OPF-086; VALID | `rendition-viewport-deprecated.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck rendition-viewport-deprecated.epub -u` | WARNING OPF-086; VALID | `rendition-viewport-deprecated.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

WARNING OPF-086 is the alert for the deprecated property.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and `<meta property="rendition:viewport">width=1200, height=600</meta>`.

## History

- 2026-11-11: First version.
