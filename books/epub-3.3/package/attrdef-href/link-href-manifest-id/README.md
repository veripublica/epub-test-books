# A `link` pointing to a manifest item's `id`

- Book: `link-href-manifest-id.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/attrdef-href/link-href-manifest-id/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#66](https://github.com/veripublica/epub-test-books/issues/66)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A link element has the href #content, the id of a manifest item. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The URL references a resource through a manifest item.

## Question

A `link` element's `href` is `#content`, the `id` of a manifest item. Does a validator reject it?

## Clause

EPUB 3.3, [`attrdef-href`](https://www.w3.org/TR/epub-33/#attrdef-href):

> The URL string MUST NOT reference resources via elements in the package document (e.g., via a manifest item or spine itemref declaration).

## Expected result

Invalid. The URL references a resource through a manifest item.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i link-href-manifest-id.epub -u --advisory` | ERROR OPF-098; INVALID | `link-href-manifest-id.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck link-href-manifest-id.epub -u` | ERROR OPF-098; INVALID | `link-href-manifest-id.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `<link rel="record" href="#content" media-type="application/xhtml+xml"/>` is added to the metadata.

## History

- 2026-11-09: First version.
