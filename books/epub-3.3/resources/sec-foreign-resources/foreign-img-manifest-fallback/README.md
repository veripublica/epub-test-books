# A BMP in `img` with a manifest fallback (valid)

- Book: `foreign-img-manifest-fallback.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-foreign-resources/foreign-img-manifest-fallback/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#125](https://github.com/veripublica/epub-test-books/issues/125)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An img element shows a BMP image, and its manifest fallback is a JPEG. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The manifest fallback is defined.

## Question

An `img` element shows a BMP image, and its manifest fallback is a JPEG. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-fallbacks-img`](https://www.w3.org/TR/epub-33/#sec-fallbacks-img):

> Otherwise, it MAY reference foreign resources in its src and srcset attributes provided EPUB creators define a manifest fallback.

## Expected result

Valid. The manifest fallback is defined.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i foreign-img-manifest-fallback.epub -u --advisory` | USAGE OBS-001, USAGE OPF-097; VALID | `foreign-img-manifest-fallback.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck foreign-img-manifest-fallback.epub -u` | USAGE OPF-097, USAGE OBS-001; VALID | `foreign-img-manifest-fallback.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect. USAGE OBS-001 says a manifest content fallback is outdated. That is the feature this book uses, not a defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated BMP and JPEG are added to the manifest, the BMP's `fallback` names the JPEG, and `content.xhtml` shows the BMP.

## History

- 2026-11-09: First version.
