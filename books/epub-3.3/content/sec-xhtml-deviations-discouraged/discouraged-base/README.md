# The `base` element (valid)

- Book: `discouraged-base.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-deviations-discouraged/discouraged-base/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#179](https://github.com/veripublica/epub-test-books/issues/179)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document has a base element. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The section is non-normative and only discourages the element, so a usage note would fit.

## Question

The content document has a `base` element. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-xhtml-deviations-discouraged`](https://www.w3.org/TR/epub-33/#sec-xhtml-deviations-discouraged):

> EPUB creators should not use the base element.

## Expected result

Valid. The section is non-normative and only discourages the element, so a usage note would fit.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i discouraged-base.epub -u --advisory` | USAGE HTM_055; VALID | `discouraged-base.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck discouraged-base.epub -u` | USAGE HTM_055; VALID | `discouraged-base.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE HTM_055 says the element is discouraged, which is what this book shows. It does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, `<base href="content.xhtml"/>` is added to `head`.

## History

- 2026-11-09: First version.
