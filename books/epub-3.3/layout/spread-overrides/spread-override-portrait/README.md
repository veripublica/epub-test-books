# The deprecated `rendition:spread-portrait` override

- Book: `spread-override-portrait.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/spread-overrides/spread-override-portrait/build.py`
- Origin: built here
- Expected: valid, with a warning for the deprecated property
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#253](https://github.com/veripublica/epub-test-books/issues/253)
- Other clauses: `deprecated`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document's itemref has rendition:spread-portrait, a deprecated override. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid, because using a deprecated feature is a SHOULD NOT, not a MUST NOT. A validator should warn about it.

## Question

The content document's `itemref` has `rendition:spread-portrait`, a deprecated override. What does a validator report?

## Clause

EPUB 3.3, [`spread-overrides`](https://www.w3.org/TR/epub-33/#spread-overrides):

> The rendition:spread-portrait property is deprecated.

EPUB 3.3, [`deprecated`](https://www.w3.org/TR/epub-33/#deprecated):

> If this specification designates a feature as deprecated, EPUB creators SHOULD NOT use the feature in their EPUB publications.

## Expected result

Valid, because using a deprecated feature is a SHOULD NOT, not a MUST NOT. A validator should warn about it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i spread-override-portrait.epub -u --advisory` | WARNING OPF-086; VALID | `spread-override-portrait.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck spread-override-portrait.epub -u` | WARNING OPF-086; VALID | `spread-override-portrait.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

WARNING OPF-086 is the alert for the deprecated property.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and the content document's `itemref` gets `properties="rendition:spread-portrait"`.

## History

- 2026-11-11: First version.
