# A navigation link holding SVG with no `title`

- Book: `label-svg-no-title.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/label-svg-no-title/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#96](https://github.com/veripublica/epub-test-books/issues/96)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

One link in the toc nav holds only inline SVG and has no title attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. SVG with no text inside it gives no text alternative, so the `a` needs a `title`.

## Question

An `a` element in the `toc` nav holds only inline SVG, and has no `title` attribute. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> If an a or span element contains instances of HTML embedded content [html] that do not provide intrinsic text alternatives, the element MUST also contain a title attribute with an alternate text rendering of the link label.

## Expected result

Invalid. SVG with no text inside it gives no text alternative, so the `a` needs a `title`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i label-svg-no-title.epub -u --advisory` | ERROR RSC-005; INVALID | `label-svg-no-title.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck label-svg-no-title.epub -u` | ERROR RSC-005; INVALID | `label-svg-no-title.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, the content document's link holds only an inline `svg`, and the nav item in the manifest gets the `svg` property. The accessibility metadata says the book has an image.

## History

- 2026-11-09: First version.
