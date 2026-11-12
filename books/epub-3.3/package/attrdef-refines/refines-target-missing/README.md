# `refines` naming no element

- Book: `refines-target-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/attrdef-refines/refines-target-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#65](https://github.com/veripublica/epub-test-books/issues/65)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

One meta element has a refines attribute that names an id that does not exist. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The fragment references nothing.

## Question

A `meta` element's `refines` attribute names an `id` that does not exist. Does a validator reject it?

## Clause

EPUB 3.3, [`attrdef-refines`](https://www.w3.org/TR/epub-33/#attrdef-refines):

> EPUB creators MUST use as the value a path-relative-scheme-less-URL string, optionally followed by U+0023 (#) and a URL-fragment string that references the resource or element they are describing.

## Expected result

Invalid. The fragment references nothing.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i refines-target-missing.epub -u --advisory` | ERROR RSC-005; INVALID | `refines-target-missing.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck refines-target-missing.epub -u` | ERROR RSC-005; INVALID | `refines-target-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, a `meta` with `refines="#nope"` is added to the metadata.

## History

- 2026-11-09: First version.
