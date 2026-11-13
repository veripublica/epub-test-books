# An element with no namespace in `container.xml`

- Book: `container-unqualified-element.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.1/container-unqualified-element/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: [#490](https://github.com/veripublica/epub-test-books/issues/490)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

container.xml has a <foo/> element after rootfiles. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. foo is in the container namespace, so it is not removed, and the schema does not allow it. The specification gives this case as non-conformant.

## Question

`container.xml` has a `<foo/>` element after `rootfiles`. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.5.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Container – META-INF/container.xml (Required); Recommended Specification, 4 September 2010):

> Conforming container.xml files MUST be valid according to the RELAX NG OCF schema with the <container> element as the root element after removing all elements (and child nodes of these elements) and attributes from other namespaces.

OCF 2.0.1, [section 3.5.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Container – META-INF/container.xml (Required); Recommended Specification, 4 September 2010):

> is non-conformant due to the non-namespace-qualified use of the <foo> element.

## Expected result

Invalid. `foo` is in the container namespace, so it is not removed, and the schema does not allow it. The specification gives this case as non-conformant.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i container-unqualified-element.epub -u --advisory` | ERROR RSC-005; INVALID | `container-unqualified-element.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck container-unqualified-element.epub -u` | ERROR RSC-005; INVALID | `container-unqualified-element.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. In `META-INF/container.xml`, `<foo/>` follows `rootfiles`.

## History

- 2026-11-12: First version.
