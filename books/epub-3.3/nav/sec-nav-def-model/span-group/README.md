# A `span` heading with a list (valid)

- Book: `span-group.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/span-group/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#113](https://github.com/veripublica/epub-test-books/issues/113)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A list item in the toc nav holds a span followed by an ol. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. This is the shape the clause requires.

## Question

A list item in the `toc` nav holds a `span` followed by an `ol`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> An ol (ordered list) element MUST follow a span element (span elements cannot occur in "leaf" li elements).

## Expected result

Valid. This is the shape the clause requires.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i span-group.epub -u --advisory` | no findings; VALID | `span-group.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck span-group.epub -u` | no findings; VALID | `span-group.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, the content document's entry is nested under a `span`.

## History

- 2026-11-09: First version.
