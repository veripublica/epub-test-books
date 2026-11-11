# `rendition:layout` declared twice

- Book: `layout-twice.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/layout/layout-twice/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#234](https://github.com/veripublica/epub-test-books/issues/234)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package declares rendition:layout twice, both times pre-paginated. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. The property is declared more than once, even though both values are the same.

## Question

The package declares `rendition:layout` twice, both times `pre-paginated`. Does a validator reject it?

## Clause

EPUB 3.3, [`layout`](https://www.w3.org/TR/epub-33/#layout):

> EPUB creators MUST NOT declare the rendition:layout property more than once. They also MUST NOT declare the property using the refines attribute.

## Expected result

Invalid. The property is declared more than once, even though both values are the same.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i layout-twice.epub -u --advisory` | ERROR RSC-005; INVALID | `layout-twice.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck layout-twice.epub -u` | ERROR RSC-005; INVALID | `layout-twice.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with a second `<meta property="rendition:layout">pre-paginated</meta>`.

## History

- 2026-11-11: First version.
