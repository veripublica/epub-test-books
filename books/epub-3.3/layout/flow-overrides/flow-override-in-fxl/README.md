# A flow override on a fixed-layout document (valid)

- Book: `flow-override-in-fxl.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/flow-overrides/flow-override-in-fxl/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the reflowable layouts section
- Issue: [#288](https://github.com/veripublica/epub-test-books/issues/288)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

In a fixed-layout book, the content document's itemref has rendition:flow-scrolled-doc. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid. The clause lets any spine item carry a flow override; nothing forbids one on a pre-paginated document, though a reading system has no overflow to handle there.

## Question

In a fixed-layout book, the content document's `itemref` has `rendition:flow-scrolled-doc`. Does a validator accept it?

## Clause

EPUB 3.3, [`flow-overrides`](https://www.w3.org/TR/epub-33/#flow-overrides):

> EPUB creators MAY specify the following properties locally on spine itemref elements to override the global value for the given spine item:

## Expected result

Valid. The clause lets any spine item carry a flow override; nothing forbids one on a pre-paginated document, though a reading system has no overflow to handle there.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i flow-override-in-fxl.epub -u --advisory` | USAGE OBS-001; VALID | `flow-override-in-fxl.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck flow-override-in-fxl.epub -u` | USAGE OBS-001; VALID | `flow-override-in-fxl.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OBS-001 says the flow overrides it names are outdated. EPUB 3.3 does not deprecate them, but the EPUB 3.4 draft lists them as outdated (change log, 18 December 2025); the message is at usage level, so it does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and the content document's `itemref` gets `properties="rendition:flow-scrolled-doc"`.

## History

- 2026-11-11: First version.
