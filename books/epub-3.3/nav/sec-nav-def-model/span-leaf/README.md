# A `span` with no list after it

- Book: `span-leaf.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/span-leaf/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#100](https://github.com/veripublica/epub-test-books/issues/100)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A list item in the toc nav holds a span and no ol. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. An `ol` must follow a `span`.

## Question

A list item in the `toc` nav holds a `span` and no `ol`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> An ol (ordered list) element MUST follow a span element (span elements cannot occur in "leaf" li elements).

## Expected result

Invalid. An `ol` must follow a `span`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i span-leaf.epub -u --advisory` | ERROR RSC-005; INVALID | `span-leaf.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck span-leaf.epub -u` | ERROR RSC-005; INVALID | `span-leaf.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, `<li><span>A group</span></li>` is added.

## History

- 2026-11-09: First version.
