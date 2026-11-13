# The CSS `unicode-bidi` property

- Book: `css-unicode-bidi.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-css-req/css-unicode-bidi/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#170](https://github.com/veripublica/epub-test-books/issues/170)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A stylesheet uses the unicode-bidi property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The property is not allowed.

## Question

A stylesheet uses the `unicode-bidi` property. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

## Expected result

Invalid. The property is not allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i css-unicode-bidi.epub -u --advisory` | ERROR CSS-001; INVALID | `css-unicode-bidi.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck css-unicode-bidi.epub -u` | ERROR CSS-001; INVALID | `css-unicode-bidi.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/style.css` is added with `unicode-bidi: bidi-override`, and `content.xhtml` links to it.

## History

- 2026-11-09: First version.
