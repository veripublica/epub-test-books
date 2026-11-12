# A stylesheet in UTF-16 (valid)

- Book: `css-utf-16.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-css-req/css-utf-16/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#172](https://github.com/veripublica/epub-test-books/issues/172)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A stylesheet is encoded in UTF-16 with a byte order mark. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. UTF-16 is allowed, although UTF-8 is recommended, so a warning would fit.

## Question

A stylesheet is encoded in UTF-16 with a byte order mark. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. UTF-16 is allowed, although UTF-8 is recommended, so a warning would fit.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i css-utf-16.epub -u --advisory` | WARNING CSS-003; VALID | `css-utf-16.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck css-utf-16.epub -u` | WARNING CSS-003; VALID | `css-utf-16.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

WARNING CSS-003 is the recommendation to use UTF-8. It does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/style.css` is written in UTF-16 with a byte order mark, and `content.xhtml` links to it.

## History

- 2026-11-09: First version.
