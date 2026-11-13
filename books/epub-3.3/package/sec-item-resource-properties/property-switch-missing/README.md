# An epub:switch without the switch property

- Book: `property-switch-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-resource-properties/property-switch-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#580](https://github.com/veripublica/epub-test-books/issues/580)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an epub:switch, and its manifest item has the mathml property but not switch. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. switch is one of the properties that must be set when they apply, and this document has a switch element.

## Question

`content.xhtml` has an `epub:switch`, and its manifest item has no `switch` property. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> EPUB creators MUST set the following properties whenever a resource referenced by an item element matches their respective definitions:

EPUB 3.3, [`switch`](https://www.w3.org/TR/epub-33/#switch):

> The switch property indicates that the described publication resource contains one or more instances of the deprecated epub:switch element.

## Expected result

Invalid. switch is one of the properties that must be set when they apply, and this document has a switch element.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i property-switch-missing.epub -u --advisory` | ERROR OPF-014, WARNING RSC-017, USAGE ACC-009; INVALID | `property-switch-missing.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck property-switch-missing.epub -u` | USAGE ACC-009, ERROR OPF-014, WARNING RSC-017; INVALID | `property-switch-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE ACC-009, WARNING RSC-017 do not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The same `content.xhtml` as `switch-element`, with `properties="mathml"` only.

## History

- 2026-11-13: First version.
