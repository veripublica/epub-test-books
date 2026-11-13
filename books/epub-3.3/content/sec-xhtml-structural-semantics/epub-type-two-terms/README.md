# epub:type with two terms (valid)

- Book: `epub-type-two-terms.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-structural-semantics/epub-type-two-terms/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#560](https://github.com/veripublica/epub-test-books/issues/560)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a p element with epub:type="chapter bodymatter". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The value is a whitespace-separated list of terms, and both are in the default vocabulary.

## Question

`content.xhtml` has `epub:type="chapter bodymatter"`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-epub-type-attribute`](https://www.w3.org/TR/epub-33/#sec-epub-type-attribute):

> Its value is one or more whitespace-separated terms stemming from external vocabularies associated with the document instance.

## Expected result

Valid. The value is a whitespace-separated list of terms, and both are in the default vocabulary.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i epub-type-two-terms.epub -u --advisory` | no findings; VALID | `epub-type-two-terms.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck epub-type-two-terms.epub -u` | no findings; VALID | `epub-type-two-terms.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<p epub:type="chapter bodymatter">Content.</p>`.

## History

- 2026-11-13: First version.
