# A scrolled document in a paginated book (valid)

- Book: `flow-override-scrolled-doc.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/flow-overrides/flow-override-scrolled-doc/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the reflowable layouts section
- Issue: [#286](https://github.com/veripublica/epub-test-books/issues/286)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package sets rendition:flow to paginated, and the about document's itemref has rendition:flow-scrolled-doc. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The override sets the flow for that one spine item. The specification's own example does the same for a table of contents.

## Question

The package sets `rendition:flow` to `paginated`, and the about document's `itemref` has `rendition:flow-scrolled-doc`. Does a validator accept it?

## Clause

EPUB 3.3, [`flow-overrides`](https://www.w3.org/TR/epub-33/#flow-overrides):

> EPUB creators MAY specify the following properties locally on spine itemref elements to override the global value for the given spine item:

## Expected result

Valid. The override sets the flow for that one spine item. The specification's own example does the same for a table of contents.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i flow-override-scrolled-doc.epub -u --advisory` | USAGE OBS-001, USAGE OBS-001; VALID | `flow-override-scrolled-doc.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck flow-override-scrolled-doc.epub -u` | USAGE OBS-001, USAGE OBS-001; VALID | `flow-override-scrolled-doc.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OBS-001 says the `rendition:flow` property is outdated. EPUB 3.3 does not deprecate it, but the EPUB 3.4 draft lists it as outdated (change log, 18 December 2025); the message is at usage level, so it does not change the verdict. A second USAGE OBS-001 says the same of the `rendition:flow-scrolled-doc` override.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

In the EPUB 3 template, `<meta property="rendition:flow">paginated</meta>` is added, and the about document's `itemref` gets `properties="rendition:flow-scrolled-doc"`.

## History

- 2026-11-11: First version.
