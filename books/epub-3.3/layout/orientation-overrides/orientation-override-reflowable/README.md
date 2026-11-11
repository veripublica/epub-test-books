# An orientation override on a reflowable document (valid)

- Book: `orientation-override-reflowable.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/orientation-overrides/orientation-override-reflowable/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

In a reflowable book, the content document's itemref has rendition:orientation-landscape. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The override may be set on any spine item; the clause does not limit it to pre-paginated documents.

## Question

In a reflowable book, the content document's `itemref` has `rendition:orientation-landscape`. Does a validator accept it?

## Clause

EPUB 3.3, [`orientation-overrides`](https://www.w3.org/TR/epub-33/#orientation-overrides):

> EPUB creators MAY specify the following properties locally on spine itemref elements to override the global value for the given spine item:

## Expected result

Valid. The override may be set on any spine item; the clause does not limit it to pre-paginated documents.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i orientation-override-reflowable.epub -u --advisory` | USAGE OBS-001; VALID | `orientation-override-reflowable.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck orientation-override-reflowable.epub -u` | USAGE OBS-001; VALID | `orientation-override-reflowable.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OBS-001 says the `rendition:orientation-landscape` override is outdated. EPUB 3.3 does not deprecate it; the message is at usage level, so it does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

In the EPUB 3 template, the content document's `itemref` gets `properties="rendition:orientation-landscape"`.

## History

- 2026-11-11: First version.
