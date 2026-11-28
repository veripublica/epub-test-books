# A rendition:layout-pre-paginated override in a roll (invalid)

- Book: `roll-override-pre-paginated.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.4/layout/sec-layout-pre-paginated/roll-override-pre-paginated/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, from the EPUB 3.4 roll layouts (w3c/epub-specs#2791)
- Issue: [#706](https://github.com/veripublica/epub-test-books/issues/706)
- Other clauses: EPUB 3.4 `sec-roll`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package sets rendition:layout to roll, and the spine itemref of content.xhtml has the property rendition:layout-pre-paginated. Both spine documents have a viewport meta tag. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. EPUB 3.4 says rendition:layout-pre-paginated must not be specified with roll layouts.

## Question

The package sets `rendition:layout` to `roll`, and the itemref of `content.xhtml` has `rendition:layout-pre-paginated`. Does a validator reject the book?

## Clause

EPUB 3.4, [`sec-layout-pre-paginated`](https://www.w3.org/TR/epub-34/#sec-layout-pre-paginated) (D.4.1.2.1 rendition:layout-pre-paginated, Application; Candidate Recommendation Draft, 25 November 2026):

> MAY be specified only for spine itemref elements. MUST NOT be paired with another layout override property in the same properties attribute. MUST NOT be specified with roll layouts.

EPUB 3.4, [`sec-roll`](https://www.w3.org/TR/epub-34/#sec-roll) (6.3.2 Roll; Candidate Recommendation Draft, 25 November 2026):

> The roll layout style applies globally (i.e., for all spine items) and cannot be overridden.

## Expected result

Invalid. `rendition:layout-pre-paginated` is on a spine itemref of a roll publication, and EPUB 3.4 says it "MUST NOT be specified with roll layouts".

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i roll-override-pre-paginated.epub -u --advisory` | ERROR RSC-005; INVALID | `roll-override-pre-paginated.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck roll-override-pre-paginated.epub -u` | ERROR RSC-005; INVALID | `roll-override-pre-paginated.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book from `layout/sec-roll/roll`, with `properties="rendition:layout-pre-paginated"` on the itemref of `content.xhtml`.

## History

- 2026-11-28: First version.
