# A PDF rendition after the OPF rootfile (valid)

- Book: `rootfile-pdf-alternate.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.1/rootfile-pdf-alternate/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: [#497](https://github.com/veripublica/epub-test-books/issues/497)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

container.xml lists OEBPS/package.opf, then PDF/book.pdf as application/pdf, and the PDF is in the container. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. Alternate renditions are allowed, and the OPF rootfile is the first of its type.

## Question

`container.xml` lists `OEBPS/package.opf`, then `PDF/book.pdf` as `application/pdf`, and the PDF is in the container. Does a validator accept the book?

## Clause

OCF 2.0.1, [section 3.5.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Container – META-INF/container.xml (Required); Recommended Specification, 4 September 2010):

> The container.xml file MUST identify the MIME type of, and path to, the rootfile for the OPF/OPS version of the publication and any OPTIONAL alternate renditions included within the container.

OCF 2.0.1, [section 3.5.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Container – META-INF/container.xml (Required); Recommended Specification, 4 September 2010):

> The <rootfiles> element MUST contain at least one <rootfile> element that has a media-type of “application/oebps-package+xml”. Only one <rootfile> element with a media-type of “application/oebps-package+xml” SHOULD be included. The file referenced by the first <rootfile> element that has a media-type of “application/oebps-package+xml” will be considered the EPUB rootfile.

## Expected result

Valid. Alternate renditions are allowed, and the OPF rootfile is the first of its type.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i rootfile-pdf-alternate.epub -u --advisory` | no findings; VALID | `rootfile-pdf-alternate.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck rootfile-pdf-alternate.epub -u` | no findings; VALID | `rootfile-pdf-alternate.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. In `META-INF/container.xml`, a second rootfile `PDF/book.pdf` (`application/pdf`), and a small PDF at that path.

## History

- 2026-11-12: First version.
