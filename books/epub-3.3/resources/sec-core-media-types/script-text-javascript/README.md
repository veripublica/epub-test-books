# A script file listed as text/javascript (valid)

- Book: `script-text-javascript.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-core-media-types/script-text-javascript/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: [#546](https://github.com/veripublica/epub-test-books/issues/546)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml loads OEBPS/script.js, which is in the manifest as text/javascript. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. text/javascript is one of the three media types the core media types table gives for scripts.

## Question

`script.js` is in the manifest as `text/javascript`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-core-media-types`](https://www.w3.org/TR/epub-33/#sec-core-media-types), the core media types table, row for scripts:

> | application/javascript, application/ecmascript, text/javascript | [rfc4329] | Scripts. |

## Expected result

Valid. text/javascript is one of the three media types the core media types table gives for scripts.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i script-text-javascript.epub -u --advisory` | USAGE OPF-090; VALID | `script-text-javascript.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck script-text-javascript.epub -u` | USAGE OPF-090; VALID | `script-text-javascript.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-090 does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The same as `external-script`, with `media-type="text/javascript"` on `script.js`.

## History

- 2026-11-13: First version.
