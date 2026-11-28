# A rendition:layout-reflowable override in a roll (invalid)

- Book: `roll-override-reflowable.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.4/layout/sec-layout-reflowable/roll-override-reflowable/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, from the EPUB 3.4 roll layouts (w3c/epub-specs#2791)
- Issue: pending
- Other clauses: EPUB 3.4 `sec-roll`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package sets rendition:layout to roll, and the spine itemref of content.xhtml has the property rendition:layout-reflowable. Both spine documents have a viewport meta tag. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. EPUB 3.4 says rendition:layout-reflowable must not be specified with roll layouts.

## Question

The package sets `rendition:layout` to `roll`, and the itemref of `content.xhtml` has `rendition:layout-reflowable`. Does a validator reject the book?

## Clause

EPUB 3.4, [`sec-layout-reflowable`](https://www.w3.org/TR/epub-34/#sec-layout-reflowable) (D.4.1.2.2 rendition:layout-reflowable, Application; Candidate Recommendation Draft, 25 November 2026):

> MAY be specified only for spine itemref elements. MUST NOT be paired with another layout override property in the same properties attribute. MUST NOT be specified with roll layouts.

EPUB 3.4, [`sec-roll`](https://www.w3.org/TR/epub-34/#sec-roll) (6.3.2 Roll; Candidate Recommendation Draft, 25 November 2026):

> The roll layout style applies globally (i.e., for all spine items) and cannot be overridden.

## Expected result

Invalid. `rendition:layout-reflowable` is on a spine itemref of a roll publication, and EPUB 3.4 says it "MUST NOT be specified with roll layouts".

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i roll-override-reflowable.epub -u --advisory` | ERROR RSC-005, USAGE HTM_060b; INVALID | `roll-override-reflowable.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck roll-override-reflowable.epub -u` | ERROR RSC-005; INVALID | `roll-override-reflowable.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

USAGE HTM_060b does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book from `layout/sec-roll/roll`, with `properties="rendition:layout-reflowable"` on the itemref of `content.xhtml`.

## History

- 2026-11-28: First version.
