# A page-spread property on a reflowable document (valid)

- Book: `page-spread-reflowable.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/page-spread/page-spread-reflowable/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#259](https://github.com/veripublica/epub-test-books/issues/259)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

In a reflowable book, the content document's itemref has rendition:page-spread-right. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The placement properties apply to reflowable content as well as pre-paginated content.

## Question

In a reflowable book, the content document's `itemref` has `rendition:page-spread-right`. Does a validator accept it?

## Clause

EPUB 3.3, [`page-spread`](https://www.w3.org/TR/epub-33/#page-spread):

> The rendition:page-spread-center, rendition:page-spread-left, and rendition:page-spread-right properties apply to both pre-paginated and reflowable content. They only apply when the reading system is creating synthetic spreads.

## Expected result

Valid. The placement properties apply to reflowable content as well as pre-paginated content.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i page-spread-reflowable.epub -u --advisory` | USAGE OPF-100; VALID | `page-spread-reflowable.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck page-spread-reflowable.epub -u` | USAGE OPF-100; VALID | `page-spread-reflowable.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-100 says the property only applies to pre-paginated content. The clause says the opposite: the properties "apply to both pre-paginated and reflowable content". The message is at usage level, so it does not change the verdict, and the verdict is what this set checks.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

In the EPUB 3 template, the content document's `itemref` gets `properties="rendition:page-spread-right"`.

## History

- 2026-11-11: First version.
