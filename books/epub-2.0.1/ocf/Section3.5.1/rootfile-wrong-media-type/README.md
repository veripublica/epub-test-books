# A rootfile with media type `application/xml`

- Book: `rootfile-wrong-media-type.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.1/rootfile-wrong-media-type/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: [#492](https://github.com/veripublica/epub-test-books/issues/492)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The only rootfile has media-type="application/xml". Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. No rootfile has the media type application/oebps-package+xml.

## Question

The only `rootfile` has `media-type="application/xml"`. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.5.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Container – META-INF/container.xml (Required); Recommended Specification, 4 September 2010):

> The <rootfiles> element MUST contain at least one <rootfile> element that has a media-type of “application/oebps-package+xml”. Only one <rootfile> element with a media-type of “application/oebps-package+xml” SHOULD be included. The file referenced by the first <rootfile> element that has a media-type of “application/oebps-package+xml” will be considered the EPUB rootfile.

## Expected result

Invalid. No `rootfile` has the media type `application/oebps-package+xml`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i rootfile-wrong-media-type.epub -u --advisory` | ERROR RSC-003; INVALID | `rootfile-wrong-media-type.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck rootfile-wrong-media-type.epub -u` | ERROR RSC-003; INVALID | `rootfile-wrong-media-type.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. In `META-INF/container.xml`, the rootfile's `media-type` becomes `application/xml`.

## History

- 2026-11-12: First version.
