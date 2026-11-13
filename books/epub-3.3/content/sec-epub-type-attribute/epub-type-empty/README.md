# An empty epub:type

- Book: `epub-type-empty.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-epub-type-attribute/epub-type-empty/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubveri: missed
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#561](https://github.com/veripublica/epub-test-books/issues/561)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a p element with epub:type="". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The value must be one or more terms, and an empty value has none.

## Question

`content.xhtml` has `epub:type=""`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-epub-type-attribute`](https://www.w3.org/TR/epub-33/#sec-epub-type-attribute):

> Its value is one or more whitespace-separated terms stemming from external vocabularies associated with the document instance.

## Expected result

Invalid. The value must be one or more terms, and an empty value has none.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i epub-type-empty.epub -u --advisory` | no findings; VALID | `epub-type-empty.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck epub-type-empty.epub -u` | ERROR RSC-005; INVALID | `epub-type-empty.epubcheck-5.4.0.txt` |

epubcheck agrees with the expected result. epubveri does not: it gives no finding.

- **epubveri: missed.** epubveri issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<p epub:type="">Content.</p>`.

## History

- 2026-11-13: First version.
