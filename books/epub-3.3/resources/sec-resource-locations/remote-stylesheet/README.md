# A stylesheet outside the container

- Book: `remote-stylesheet.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-resource-locations/remote-stylesheet/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#136](https://github.com/veripublica/epub-test-books/issues/136)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document links to a stylesheet at a web address, listed in the manifest. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Stylesheets are not among the types that may be outside the container.

## Question

The content document links to a stylesheet at an `https` URL, listed in the manifest. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-resource-locations`](https://www.w3.org/TR/epub-33/#sec-resource-locations):

> EPUB creators MUST store all other resources within the EPUB container.

## Expected result

Invalid. Stylesheets are not among the types that may be outside the container.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i remote-stylesheet.epub -u --advisory` | ERROR RSC-006; INVALID | `remote-stylesheet.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck remote-stylesheet.epub -u` | ERROR RSC-006; INVALID | `remote-stylesheet.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a `link` has an `https` stylesheet. In `OEBPS/package.opf`, that URL is a manifest item.

## History

- 2026-11-09: First version.
