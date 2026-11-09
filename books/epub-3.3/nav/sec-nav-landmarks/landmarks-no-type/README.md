# A `landmarks` link without `epub:type`

- Book: `landmarks-no-type.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-landmarks/landmarks-no-type/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#109](https://github.com/veripublica/epub-test-books/issues/109)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A link in the landmarks nav has no epub:type attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The attribute is required.

## Question

An `a` element in the `landmarks` nav has no `epub:type`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-landmarks`](https://www.w3.org/TR/epub-33/#sec-nav-landmarks):

> The epub:type attribute is REQUIRED on a element descendants of the landmarks nav element.

## Expected result

Invalid. The attribute is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i landmarks-no-type.epub -u --advisory` | ERROR RSC-005; INVALID | `landmarks-no-type.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck landmarks-no-type.epub -u` | ERROR RSC-005; INVALID | `landmarks-no-type.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, a `landmarks` nav is added whose `a` has no `epub:type`.

## History

- 2026-11-09: First version.
