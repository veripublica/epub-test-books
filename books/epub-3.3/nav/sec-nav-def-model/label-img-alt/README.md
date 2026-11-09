# A navigation image with `alt` (valid)

- Book: `label-img-alt.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/label-img-alt/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#114](https://github.com/veripublica/epub-test-books/issues/114)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

One link in the toc nav holds only an image, with alternative text. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The `alt` text is the label.

## Question

An `a` element in the `toc` nav holds only an image with alternative text. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> When determining compliance with this requirement, the concatenated label MUST include text content contained in title or alt attributes for non-textual descendant elements.

## Expected result

Valid. The `alt` text is the label.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i label-img-alt.epub -u --advisory` | no findings; VALID | `label-img-alt.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck label-img-alt.epub -u` | no findings; VALID | `label-img-alt.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated JPEG is added, and the content document's link in `OEBPS/nav.xhtml` holds only that image, with `alt="Content"`. The accessibility metadata says the book has an image.

## History

- 2026-11-09: First version.
