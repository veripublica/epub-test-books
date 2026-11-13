# A script file listed as application/x-javascript (valid)

- Book: `script-foreign-media-type.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-core-media-types/script-foreign-media-type/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: [#548](https://github.com/veripublica/epub-test-books/issues/548)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml loads OEBPS/script.js, which is in the manifest as application/x-javascript, a type that is not a core media type. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The script is then a foreign resource. A foreign resource needs a fallback only when it is in the spine or used where a core media type is required, and neither applies to a script loaded by a script element.

## Question

`script.js` is in the manifest as `application/x-javascript`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-core-media-types`](https://www.w3.org/TR/epub-33/#sec-core-media-types), the core media types table, row for scripts:

> | application/javascript, application/ecmascript, text/javascript | [rfc4329] | Scripts. |

## Expected result

Valid. The script is then a foreign resource. A foreign resource needs a fallback only when it is in the spine or used where a core media type is required, and neither applies to a script loaded by a script element.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i script-foreign-media-type.epub -u --advisory` | USAGE RSC-035; VALID | `script-foreign-media-type.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck script-foreign-media-type.epub -u` | USAGE RSC-035; VALID | `script-foreign-media-type.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE RSC-035 does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The same as `external-script`, with `media-type="application/x-javascript"` on `script.js`.

## History

- 2026-11-13: First version.
