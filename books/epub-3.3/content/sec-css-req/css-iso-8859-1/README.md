# A stylesheet in ISO-8859-1

- Book: `css-iso-8859-1.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-css-req/css-iso-8859-1/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#171](https://github.com/veripublica/epub-test-books/issues/171)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A stylesheet is encoded in ISO-8859-1 and says so with @charset. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Only UTF-8 and UTF-16 are allowed.

## Question

A stylesheet is encoded in ISO-8859-1 and says so with `@charset`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. Only UTF-8 and UTF-16 are allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i css-iso-8859-1.epub -u --advisory` | ERROR CSS-004; INVALID | `css-iso-8859-1.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck css-iso-8859-1.epub -u` | ERROR CSS-004; INVALID | `css-iso-8859-1.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/style.css` is written in ISO-8859-1 with a matching `@charset` and one non-ASCII character, and `content.xhtml` links to it.

## History

- 2026-11-09: First version.
