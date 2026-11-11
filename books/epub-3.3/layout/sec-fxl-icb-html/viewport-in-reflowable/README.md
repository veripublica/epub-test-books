# A viewport in a reflowable document (valid)

- Book: `viewport-in-reflowable.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/sec-fxl-icb-html/viewport-in-reflowable/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#273](https://github.com/veripublica/epub-test-books/issues/273)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

In a reflowable book, content.xhtml has a viewport meta tag of width=1200, height=600. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The viewport rules are for fixed-layout documents; nothing forbids the tag in a reflowable one.

## Question

In a reflowable book, `content.xhtml` has a viewport meta tag of `width=1200, height=600`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-fxl-icb-html`](https://www.w3.org/TR/epub-33/#sec-fxl-icb-html):

> For XHTML fixed-layout documents, the initial containing block [css2] is obtained from the REQUIRED height and width definitions in a viewport meta tag, where: the height property MUST have as its value a positive number [css2] or the keyword device-height; and the width property MUST have as its value a positive number [css2] or the keyword device-width.

## Expected result

Valid. The viewport rules are for fixed-layout documents; nothing forbids the tag in a reflowable one.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i viewport-in-reflowable.epub -u --advisory` | USAGE HTM_060b; VALID | `viewport-in-reflowable.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck viewport-in-reflowable.epub -u` | USAGE HTM_060b; VALID | `viewport-in-reflowable.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE HTM_060b says the viewport is not checked, because the document is reflowable. It is at usage level and does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

In the EPUB 3 template, `content.xhtml` gets `<meta name="viewport" content="width=1200, height=600"/>`.

## History

- 2026-11-11: First version.
