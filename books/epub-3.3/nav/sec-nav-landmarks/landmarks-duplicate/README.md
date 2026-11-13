# Two identical `landmarks` entries

- Book: `landmarks-duplicate.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-landmarks/landmarks-duplicate/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#110](https://github.com/veripublica/epub-test-books/issues/110)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The landmarks nav has two entries with the same epub:type and the same target. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The two entries repeat the type and the resource.

## Question

The `landmarks` nav has two entries with the same `epub:type` and the same target. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-landmarks`](https://www.w3.org/TR/epub-33/#sec-nav-landmarks):

> The landmarks nav MUST NOT include multiple entries with the same epub:type value that reference the same resource, or fragment thereof.

## Expected result

Invalid. The two entries repeat the type and the resource.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i landmarks-duplicate.epub -u --advisory` | ERROR RSC-005, ERROR RSC-005; INVALID | `landmarks-duplicate.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck landmarks-duplicate.epub -u` | ERROR RSC-005, ERROR RSC-005; INVALID | `landmarks-duplicate.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, a `landmarks` nav with two identical entries is added.

## History

- 2026-11-09: First version.
