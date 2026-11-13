# A manifest href starting with /

- Book: `item-href-path-absolute.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-elem/item-href-path-absolute/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the package document section
- Issue: [#48](https://github.com/veripublica/epub-test-books/issues/48)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The manifest item for the content document has the href /OEBPS/content.xhtml, which starts with a slash. It still resolves to the right file. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A value starting with `/` is a path-absolute-URL string in the URL Standard, which is neither of the two allowed forms.

## Question

A manifest item's `href` is `/OEBPS/content.xhtml`, which still resolves to the right file. Does a validator reject the form of the URL?

## Clause

EPUB 3.3, [`sec-item-elem`](https://www.w3.org/TR/epub-33/#sec-item-elem):

> The value MUST be an absolute- or path-relative-scheme-less-URL string [url].

## Expected result

Invalid. A value starting with `/` is a path-absolute-URL string in the URL Standard, which is neither of the two allowed forms.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i item-href-path-absolute.epub -u --advisory` | ERROR RSC-026; INVALID | `item-href-path-absolute.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck item-href-path-absolute.epub -u` | ERROR RSC-026; INVALID | `item-href-path-absolute.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

epubcheck says the URL leaks outside the container, and epubveri says it is path-absolute or escapes the container root. The note in `sec-container-iri` says such a string does not leak after parsing and is disallowed anyway, so the clause above is the accurate reason. The verdict is the same.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the content item's `href` becomes `/OEBPS/content.xhtml`.

## History

- 2026-11-09: First version.
