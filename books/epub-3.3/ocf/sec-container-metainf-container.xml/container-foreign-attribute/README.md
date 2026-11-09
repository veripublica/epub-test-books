# An attribute from another namespace in container.xml

- Book: `container-foreign-attribute.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-metainf-container.xml/container-foreign-attribute/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#33](https://github.com/veripublica/epub-test-books/issues/33)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The rootfiles element in META-INF/container.xml has one extra attribute, ext:note, in the namespace https://example.org/epub-test-books/ns. Without it, the file is the EPUB 3 template's container.xml, which raises no finding.

Expected result: Valid. Elements and attributes from other namespaces are removed before the file is checked, and what is left is the template's valid container.xml.

## Question

The `rootfiles` element in `META-INF/container.xml` has an attribute from another namespace. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-container-metainf-container.xml`](https://www.w3.org/TR/epub-33/#sec-container-metainf-container.xml):

> All [xml] elements defined in this section are in the urn:oasis:names:tc:opendocument:xmlns:container namespace [xml-names] unless specified otherwise. The contents of this file MUST be valid to the definition in this section after removing all elements and attributes from other namespaces (including all attributes and contents of such elements).

## Expected result

Valid. Elements and attributes from other namespaces are removed before the file is checked, and what is left is the template's valid container.xml.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i container-foreign-attribute.epub -u --advisory` | VALID | `container-foreign-attribute.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck container-foreign-attribute.epub -u` | ERROR RSC-005; INVALID | `container-foreign-attribute.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the extension attribute as not allowed (RSC-005). That is right for the bare schema, but the specification says to remove attributes from other namespaces before validating.

- **epubcheck: wrong error.** [w3c/epubcheck#1754](https://github.com/w3c/epubcheck/issues/1754).

epubveri gives no finding here. Since 0.38.0 it validates container.xml against the schema, but it removes other namespaces first.

## Build

`<rootfiles>` becomes `<rootfiles xmlns:ext="https://example.org/epub-test-books/ns" ext:note="An attribute from another namespace.">`.

## History

- 2026-11-08: First version.
