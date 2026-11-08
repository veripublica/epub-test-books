# An element from another namespace in container.xml

- Book: `container-foreign-element.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-metainf-container.xml/container-foreign-element/build.py`
- Origin: built here
- Expected: valid
- Marks: epubveri: wrong error; epubcheck: wrong error
- Asked for by: the maintainer, to complete the OCF section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

META-INF/container.xml has one extra element, ext:note, in the namespace https://example.org/epub-test-books/ns. It comes after rootfiles. Without it, the file is the EPUB 3 template's container.xml, which raises no finding.

Expected result: Valid. Elements and attributes from other namespaces are removed before the file is checked, and what is left is the template's valid container.xml.

## Question

`META-INF/container.xml` has an element from another namespace after `rootfiles`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-container-metainf-container.xml`](https://www.w3.org/TR/epub-33/#sec-container-metainf-container.xml):

> All [xml] elements defined in this section are in the urn:oasis:names:tc:opendocument:xmlns:container namespace [xml-names] unless specified otherwise. The contents of this file MUST be valid to the definition in this section after removing all elements and attributes from other namespaces (including all attributes and contents of such elements).

## Expected result

Valid. Elements and attributes from other namespaces are removed before the file is checked, and what is left is the template's valid container.xml.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.37.1 | `epubveri -i container-foreign-element.epub -u --advisory` | ERROR RSC-005; INVALID | `container-foreign-element.epubveri-0.37.1.txt` |
| epubcheck 5.4.0 | `epubcheck container-foreign-element.epub -u` | ERROR RSC-005; INVALID | `container-foreign-element.epubcheck-5.4.0.txt` |

Both disagree with the expected result. Each reports the extension element as not allowed (RSC-005). That is right for the bare schema, but the specification says to remove elements from other namespaces before validating.

- **epubveri: wrong error.** Reported to epubveri by note (2026-11-08); no public issue yet.
- **epubcheck: wrong error.** The issue on `w3c/epubcheck` is not filed yet. I found no existing issue on it.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `META-INF/container.xml`, `<ext:note xmlns:ext="https://example.org/epub-test-books/ns">An element from another namespace.</ext:note>` is added after `</rootfiles>`.

## History

- 2026-11-08: First version.
