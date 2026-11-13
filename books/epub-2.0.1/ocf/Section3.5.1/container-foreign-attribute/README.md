# An attribute from another namespace in `container.xml` (valid)

- Book: `container-foreign-attribute.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.1/container-foreign-attribute/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: [#489](https://github.com/veripublica/epub-test-books/issues/489)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The rootfiles element of container.xml has an ext:note attribute in its own namespace. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. Attributes from other namespaces are removed before the schema check, and what is left is the template's container.xml.

## Question

The `rootfiles` element of `container.xml` has an `ext:note` attribute in its own namespace. Does a validator accept the book?

## Clause

OCF 2.0.1, [section 3.5.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Container – META-INF/container.xml (Required); Recommended Specification, 4 September 2010):

> Conforming container.xml files MUST be valid according to the RELAX NG OCF schema with the <container> element as the root element after removing all elements (and child nodes of these elements) and attributes from other namespaces.

## Expected result

Valid. Attributes from other namespaces are removed before the schema check, and what is left is the template's `container.xml`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i container-foreign-attribute.epub -u --advisory` | no findings; VALID | `container-foreign-attribute.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck container-foreign-attribute.epub -u` | ERROR RSC-005; INVALID | `container-foreign-attribute.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the foreign attribute as a schema error (RSC-005).

- **epubcheck: wrong error.** [w3c/epubcheck#1754](https://github.com/w3c/epubcheck/issues/1754), opened for EPUB 3; the same happens at EPUB 2.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. In `META-INF/container.xml`, `rootfiles` gets `ext:note`, with `xmlns:ext="https://example.org/epub-test-books/ns"`.

## History

- 2026-11-12: First version.
