# A navigation image with empty `alt`

- Book: `label-img-no-alt.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/label-img-no-alt/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#95](https://github.com/veripublica/epub-test-books/issues/95)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

One link in the toc nav holds only an image with an empty alt attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The image supplies no text, so the label has zero length.

## Question

An `a` element in the `toc` nav holds only an image with `alt=""`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> The child a or span element MUST provide a non-zero-length text label after concatenation of all child content and application of whitespace normalization rules.

> When determining compliance with this requirement, the concatenated label MUST include text content contained in title or alt attributes for non-textual descendant elements.

## Expected result

Invalid. The image supplies no text, so the label has zero length.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i label-img-no-alt.epub -u --advisory` | ERROR RSC-005; INVALID | `label-img-no-alt.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck label-img-no-alt.epub -u` | ERROR RSC-005; INVALID | `label-img-no-alt.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated JPEG is added, and the content document's link in `OEBPS/nav.xhtml` holds only that image with `alt=""`. The accessibility metadata says the book has an image.

## History

- 2026-11-09: First version.
