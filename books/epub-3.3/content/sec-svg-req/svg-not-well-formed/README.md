# An SVG content document that is not well-formed

- Book: `svg-not-well-formed.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-svg-req/svg-not-well-formed/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#588](https://github.com/veripublica/epub-test-books/issues/588)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/picture.svg never closes its svg root element. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A conforming SVG stand-alone file must be well-formed XML.

## Question

`picture.svg`, in the spine, never closes its `svg` element. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-svg-req`](https://www.w3.org/TR/epub-33/#sec-svg-req):

> An SVG content document MUST be a conforming SVG stand-alone file [svg] and conform to all content conformance constraints expressed in 6.2.3 Restrictions on SVG.

SVG 2, [`ConformingSVGStandAloneFiles`](https://www.w3.org/TR/SVG2/conform.html#ConformingSVGStandAloneFiles) (2.4.5 Conforming SVG Stand-Alone Files; Candidate Recommendation):

> A document is a conforming SVG stand-alone file if: it is a well-formed XML document, its root element is an ‘svg’ element, the SVG document fragment rooted at the document element is a conforming XML-compatible SVG markup fragment, and any other SVG document fragments within the document (such as those within a ‘foreignObject’) form a conforming XML-compatible SVG markup fragment.

## Expected result

Invalid. A conforming SVG stand-alone file must be well-formed XML.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i svg-not-well-formed.epub -u --advisory` | FATAL RSC-016; INVALID | `svg-not-well-formed.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-not-well-formed.epub -u` | FATAL RSC-016; INVALID | `svg-not-well-formed.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/picture.svg` is in the manifest as `image/svg+xml` and last in the spine. It holds the same picture as `svg-document`, without the closing `</svg>`.

## History

- 2026-11-13: First version.
