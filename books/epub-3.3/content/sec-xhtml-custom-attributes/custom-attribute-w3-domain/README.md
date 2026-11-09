# A prefixed attribute from w3.org

- Book: `custom-attribute-w3-domain.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-custom-attributes/custom-attribute-w3-domain/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#156](https://github.com/veripublica/epub-test-books/issues/156)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A p element has a prefixed attribute from a namespace at w3.org that HTML does not define. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A namespace at w3.org does not make a custom attribute, and HTML does not define this attribute.

## Question

A `p` element has a prefixed attribute from a namespace at w3.org that HTML does not define. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-custom-attributes`](https://www.w3.org/TR/epub-33/#sec-xhtml-custom-attributes):

> XHTML content documents MAY contain custom attributes, which are prefixed [xml-names] attributes whose namespace URL does not include either of the following strings in its domain [url]: w3.org idpf.org

## Expected result

Invalid. A namespace at w3.org does not make a custom attribute, and HTML does not define this attribute.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i custom-attribute-w3-domain.epub -u --advisory` | ERROR HTM_054; INVALID | `custom-attribute-w3-domain.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck custom-attribute-w3-domain.epub -u` | ERROR HTM_054; INVALID | `custom-attribute-w3-domain.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a `p` with a prefixed attribute from a w3.org namespace is added.

## History

- 2026-11-09: First version.
