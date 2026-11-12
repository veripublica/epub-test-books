# An image outside the container

- Book: `remote-image.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-resource-locations/remote-image/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#135](https://github.com/veripublica/epub-test-books/issues/135)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An img element references a JPEG at a web address, listed in the manifest. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Images are not among the types that may be outside the container.

## Question

An `img` element references a JPEG at an `https` URL, listed in the manifest. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-resource-locations`](https://www.w3.org/TR/epub-33/#sec-resource-locations):

> EPUB creators MUST store all other resources within the EPUB container.

## Expected result

Invalid. Images are not among the types that may be outside the container.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i remote-image.epub -u --advisory` | ERROR RSC-006; INVALID | `remote-image.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck remote-image.epub -u` | ERROR RSC-006; INVALID | `remote-image.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, an `img` has an `https` source. In `OEBPS/package.opf`, that URL is a manifest item and the content item has the `remote-resources` property.

## History

- 2026-11-09: First version.
