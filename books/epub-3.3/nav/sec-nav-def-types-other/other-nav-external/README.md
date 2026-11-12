# A typed `nav` linking outside the container (valid)

- Book: `other-nav-external.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-types-other/other-nav-external/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#120](https://github.com/veripublica/epub-test-books/issues/120)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A nav with epub:type="lot" has a link to a web address. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Navs other than `toc`, `landmarks` and `page-list` may link outside the container.

## Question

A `nav` with `epub:type="lot"` has an `https` link. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> MAY, for all other nav types, also reference content outside the EPUB container (e.g., web-hosted resources).

## Expected result

Valid. Navs other than `toc`, `landmarks` and `page-list` may link outside the container.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i other-nav-external.epub -u --advisory` | no findings; VALID | `other-nav-external.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck other-nav-external.epub -u` | no findings; VALID | `other-nav-external.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, a `nav` with `epub:type="lot"` and an `https` link is added.

## History

- 2026-11-09: First version.
