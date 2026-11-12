# A custom attribute (valid)

- Book: `custom-attribute.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-custom-attributes/custom-attribute/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#155](https://github.com/veripublica/epub-test-books/issues/155)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A p element has a prefixed attribute from a namespace at example.org. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. This is a custom attribute as the clause defines one.

## Question

A `p` element has a prefixed attribute from a namespace at example.org. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-xhtml-custom-attributes`](https://www.w3.org/TR/epub-33/#sec-xhtml-custom-attributes):

> XHTML content documents MAY contain custom attributes, which are prefixed [xml-names] attributes whose namespace URL does not include either of the following strings in its domain [url]: w3.org idpf.org

## Expected result

Valid. This is a custom attribute as the clause defines one.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i custom-attribute.epub -u --advisory` | no findings; VALID | `custom-attribute.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck custom-attribute.epub -u` | no findings; VALID | `custom-attribute.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a `p` with a prefixed attribute is added.

## History

- 2026-11-09: First version.
