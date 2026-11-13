# A `META-INF/manifest.xml` that is not an ODF manifest

- Book: `manifest-xml-wrong-root.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.2/manifest-xml-wrong-root/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer; parked on 2026-11-12 while both verifiers missed it, shipped after epubveri 0.42.0 reports it
- Issue: [#595](https://github.com/veripublica/epub-test-books/issues/595)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container also holds META-INF/manifest.xml, an empty files element in no namespace. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. If present, manifest.xml must follow the ODF 1.0 manifest schema, whose root is manifest:manifest.

## Question

The container also holds `META-INF/manifest.xml`, an empty `files` element in no namespace. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.5.2](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Manifest – META-INF/manifest.xml (Optional); Recommended Specification, 4 September 2010):

> If present, the file’s content MUST be as defined in the ODF 1.0 manifest schema

## Expected result

Invalid. If present, `manifest.xml` must follow the ODF 1.0 manifest schema, whose root is `manifest:manifest`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i manifest-xml-wrong-root.epub -u --advisory` | ERROR RSC-005; INVALID | `manifest-xml-wrong-root.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck manifest-xml-wrong-root.epub -u` | no findings; VALID | `manifest-xml-wrong-root.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1777](https://github.com/w3c/epubcheck/issues/1777).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. An entry `META-INF/manifest.xml`: an empty `<files/>`.

## History

- 2026-11-13: First version.
