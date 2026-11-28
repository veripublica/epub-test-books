# pageBreakSource none, with a page list (valid)

- Book: `page-break-source.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.4/package/sec-pageBreakSource/page-break-source/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, from the EPUB 3.4 pageBreakSource property (w3c/epub-specs#2714)
- Issue: [#711](https://github.com/veripublica/epub-test-books/issues/711)
- Other clauses: EPUB 3.3 `sec-nav-pagelist`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The navigation document has a page list with one entry. The package has one meta with the property pageBreakSource and the value none. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. EPUB 3.4 asks for exactly one pageBreakSource when the publication has a page list, and none when the page break markers belong to this publication only.

## Question

The navigation document has a page list, and the package has one `pageBreakSource` meta with the value `none`. Does a validator accept the book?

## Clause

EPUB 3.4, [`sec-pageBreakSource`](https://www.w3.org/TR/epub-34/#sec-pageBreakSource) (D.2.9 pageBreakSource; Candidate Recommendation Draft, 25 November 2026):

> If the page break markers are unique to the EPUB publication (e.g., for a digital-only edition), the value "none" MUST be specified.

> Cardinality: Exactly one when the publication includes a page list and/or page break markers, otherwise 0.

## Expected result

Valid. The book has a page list, so it needs exactly one `pageBreakSource`. Its page list is not drawn from another edition, so the value is `none`.

In EPUB 3.3 `pageBreakSource` is not a term of the meta properties vocabulary.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i page-break-source.epub -u --advisory` | no findings; VALID | `page-break-source.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck page-break-source.epub -u` | no findings; VALID | `page-break-source.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with a `page-list` nav of one entry (`content.xhtml#content`) in `nav.xhtml` (`scripts/lib/navvariants.py`), and `<meta property="pageBreakSource">none</meta>` in the package metadata.

## History

- 2026-11-28: First version.
