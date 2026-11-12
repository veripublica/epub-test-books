# Two flow overrides on one spine item

- Book: `flow-two-overrides.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/flow-overrides/flow-two-overrides/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the reflowable layouts section
- Issue: [#287](https://github.com/veripublica/epub-test-books/issues/287)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document's itemref has both rendition:flow-paginated and rendition:flow-scrolled-doc. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Only one flow override is allowed on a spine item.

## Question

The content document's `itemref` has both `rendition:flow-paginated` and `rendition:flow-scrolled-doc`. Does a validator reject it?

## Clause

EPUB 3.3, [`flow-overrides`](https://www.w3.org/TR/epub-33/#flow-overrides):

> EPUB creators MUST NOT use more than one of these overrides on any given spine item.

## Expected result

Invalid. Only one flow override is allowed on a spine item.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i flow-two-overrides.epub -u --advisory` | ERROR RSC-005, USAGE OBS-001, USAGE OBS-001; INVALID | `flow-two-overrides.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck flow-two-overrides.epub -u` | USAGE OBS-001, USAGE OBS-001, ERROR RSC-005; INVALID | `flow-two-overrides.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OBS-001 (once for each property) says the flow overrides it names are outdated. EPUB 3.3 does not deprecate them, but the EPUB 3.4 draft lists them as outdated (change log, 18 December 2025); the message is at usage level, so it does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

In the EPUB 3 template, the content document's `itemref` gets `properties="rendition:flow-paginated rendition:flow-scrolled-doc"`.

## History

- 2026-11-11: First version.
