# An SVG content document whose svg root has no namespace

- Book: `svg-no-namespace.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-svg-req/svg-no-namespace/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubveri: missed
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#586](https://github.com/veripublica/epub-test-books/issues/586)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/picture.svg has an svg root element with no xmlns, so it is not in the SVG namespace. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. An svg element outside the SVG namespace is not SVG's svg element, so the file is not a conforming SVG stand-alone file.

## Question

`picture.svg`, in the spine, has an `svg` root with no namespace. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-svg-req`](https://www.w3.org/TR/epub-33/#sec-svg-req):

> An SVG content document MUST be a conforming SVG stand-alone file [svg] and conform to all content conformance constraints expressed in 6.2.3 Restrictions on SVG.

SVG 2, [`ConformingSVGStandAloneFiles`](https://www.w3.org/TR/SVG2/conform.html#ConformingSVGStandAloneFiles) (2.4.5 Conforming SVG Stand-Alone Files; Candidate Recommendation):

> A document is a conforming SVG stand-alone file if: it is a well-formed XML document, its root element is an ‘svg’ element, the SVG document fragment rooted at the document element is a conforming XML-compatible SVG markup fragment, and any other SVG document fragments within the document (such as those within a ‘foreignObject’) form a conforming XML-compatible SVG markup fragment.

## Expected result

Invalid. An svg element outside the SVG namespace is not SVG's svg element, so the file is not a conforming SVG stand-alone file.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i svg-no-namespace.epub -u --advisory` | no findings; VALID | `svg-no-namespace.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-no-namespace.epub -u` | ERROR RSC-005; INVALID | `svg-no-namespace.epubcheck-5.4.0.txt` |

epubcheck agrees with the expected result. epubveri does not: it gives no finding.

- **epubveri: missed.** epubveri issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/picture.svg` is in the manifest as `image/svg+xml` and last in the spine. It holds the same picture as `svg-document`, without `xmlns` on `svg`.

## History

- 2026-11-13: First version.
