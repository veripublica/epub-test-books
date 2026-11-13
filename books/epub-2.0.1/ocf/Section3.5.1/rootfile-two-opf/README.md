# Two rootfiles of type `application/oebps-package+xml` (valid)

- Book: `rootfile-two-opf.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.1/rootfile-two-opf/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: [#496](https://github.com/veripublica/epub-test-books/issues/496)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

container.xml lists OEBPS/package.opf, then OEBPS/second.opf, a copy of it; both have the media type application/oebps-package+xml. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. Only one such rootfile SHOULD be included, which is a recommendation, and the first one is the EPUB rootfile.

## Question

`container.xml` lists `OEBPS/package.opf`, then `OEBPS/second.opf`, a copy of it; both have the media type `application/oebps-package+xml`. Does a validator accept the book?

## Clause

OCF 2.0.1, [section 3.5.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Container – META-INF/container.xml (Required); Recommended Specification, 4 September 2010):

> The <rootfiles> element MUST contain at least one <rootfile> element that has a media-type of “application/oebps-package+xml”. Only one <rootfile> element with a media-type of “application/oebps-package+xml” SHOULD be included. The file referenced by the first <rootfile> element that has a media-type of “application/oebps-package+xml” will be considered the EPUB rootfile.

## Expected result

Valid. Only one such rootfile SHOULD be included, which is a recommendation, and the first one is the EPUB rootfile.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i rootfile-two-opf.epub -u --advisory` | WARNING PKG-013; VALID | `rootfile-two-opf.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck rootfile-two-opf.epub -u` | ERROR PKG-013; INVALID | `rootfile-two-opf.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the second rootfile as an error (PKG-013).

epubveri reports the second rootfile as a warning (PKG-013): the rule is a SHOULD, and a warning does not change the verdict. Up to 0.40.1 it was an error.

- **epubcheck: wrong error.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. In `META-INF/container.xml`, a second rootfile for `OEBPS/second.opf`; that file is a copy of `OEBPS/package.opf`.

## History

- 2026-11-12: First version.
