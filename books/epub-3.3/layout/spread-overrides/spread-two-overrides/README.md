# Two spread overrides on one spine item

- Book: `spread-two-overrides.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/spread-overrides/spread-two-overrides/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#252](https://github.com/veripublica/epub-test-books/issues/252)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document's itemref has both rendition:spread-none and rendition:spread-both. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. Only one spread override is allowed on a spine item.

## Question

The content document's `itemref` has both `rendition:spread-none` and `rendition:spread-both`. Does a validator reject it?

## Clause

EPUB 3.3, [`spread-overrides`](https://www.w3.org/TR/epub-33/#spread-overrides):

> EPUB creators MUST NOT use more than one of these overrides on any given spine item.

## Expected result

Invalid. Only one spread override is allowed on a spine item.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i spread-two-overrides.epub -u --advisory` | ERROR RSC-005, USAGE OBS-001, USAGE OBS-001; INVALID | `spread-two-overrides.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck spread-two-overrides.epub -u` | USAGE OBS-001, USAGE OBS-001, ERROR RSC-005; INVALID | `spread-two-overrides.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OBS-001 (once for each property) says the spread overrides are outdated. EPUB 3.3 deprecates only `rendition:spread-portrait`, but the EPUB 3.4 draft lists the spread overrides as outdated (change log, 18 December 2025); the message is at usage level, so it does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and the content document's `itemref` gets `properties="rendition:spread-none rendition:spread-both"`.

## History

- 2026-11-11: First version.
