# Two `landmarks` of one type, different targets (valid)

- Book: `landmarks-same-type-different-resources.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-landmarks/landmarks-same-type-different-resources/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#118](https://github.com/veripublica/epub-test-books/issues/118)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Two entries in the landmarks nav share an epub:type and have different targets. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The clause forbids repeating a type only for the same resource.

## Question

Two entries in the `landmarks` nav share an `epub:type` and have different targets. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-nav-landmarks`](https://www.w3.org/TR/epub-33/#sec-nav-landmarks):

> The landmarks nav MUST NOT include multiple entries with the same epub:type value that reference the same resource, or fragment thereof.

## Expected result

Valid. The clause forbids repeating a type only for the same resource.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i landmarks-same-type-different-resources.epub -u --advisory` | no findings; VALID | `landmarks-same-type-different-resources.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck landmarks-same-type-different-resources.epub -u` | no findings; VALID | `landmarks-same-type-different-resources.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, a `landmarks` nav with two `chapter` entries is added.

## History

- 2026-11-09: First version.
