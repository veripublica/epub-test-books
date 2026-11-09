# A typed `nav` with no heading (valid)

- Book: `other-nav-no-heading.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-types-other/other-nav-no-heading/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#222](https://github.com/veripublica/epub-test-books/issues/222)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A nav with epub:type="lot" has no heading. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The heading is optional: the content model allows zero or one, and no sentence in EPUB 3.3 requires one for this kind of nav.

## Question

A `nav` with `epub:type="lot"` has no heading. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> nav In this order: h1-h6 [0 or 1] ol [exactly 1]

## Expected result

Valid. The heading is optional: the content model allows zero or one, and no sentence in EPUB 3.3 requires one for this kind of nav.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i other-nav-no-heading.epub -u --advisory` | no findings; VALID | `other-nav-no-heading.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck other-nav-no-heading.epub -u` | ERROR RSC-005; INVALID | `other-nav-no-heading.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: epubcheck requires a heading on this kind of `nav`, and EPUB 3.3 does not.

- **epubcheck: wrong error.** [w3c/epubcheck#1758](https://github.com/w3c/epubcheck/issues/1758).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, a `nav` with `epub:type="lot"` and no heading is added.

## History

- 2026-11-09: First version.
