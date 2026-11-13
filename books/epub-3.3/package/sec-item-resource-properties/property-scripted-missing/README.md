# A script without the `scripted` property

- Book: `property-scripted-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-resource-properties/property-scripted-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#75](https://github.com/veripublica/epub-test-books/issues/75)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document has a script element, and its manifest item has no scripted property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. `scripted` is one of the listed properties, and this document contains a script.

## Question

The content document has a `script` element, and its manifest item has no `scripted` property. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> EPUB creators MUST set the following properties whenever a resource referenced by an item element matches their respective definitions:

## Expected result

Invalid. `scripted` is one of the listed properties, and this document contains a script.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i property-scripted-missing.epub -u --advisory` | ERROR OPF-014; INVALID | `property-scripted-missing.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck property-scripted-missing.epub -u` | ERROR OPF-014; INVALID | `property-scripted-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A `script` element is added to `content.xhtml`. The manifest is not changed.

## History

- 2026-11-09: First version.
