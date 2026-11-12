# Empty `dc:language`

- Book: `language-empty.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-metadata-values/language-empty/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#56](https://github.com/veripublica/epub-test-books/issues/56)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The dc:language element is empty. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The element has no value.

## Question

The `dc:language` element is empty. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-metadata-values`](https://www.w3.org/TR/epub-33/#sec-metadata-values):

> These elements MUST have non-empty values after leading and trailing ASCII whitespace [infra] is stripped (i.e., they must consist of at least one non-whitespace character).

## Expected result

Invalid. The element has no value.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i language-empty.epub -u --advisory` | ERROR RSC-005; INVALID | `language-empty.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck language-empty.epub -u` | ERROR RSC-005; INVALID | `language-empty.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the value of `dc:language` is removed.

## History

- 2026-11-09: First version.
