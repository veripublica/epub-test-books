# Two orientation overrides on one spine item

- Book: `orientation-two-overrides.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/orientation-overrides/orientation-two-overrides/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document's itemref has both rendition:orientation-landscape and rendition:orientation-portrait. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. Only one orientation override is allowed on a spine item.

## Question

The content document's `itemref` has both `rendition:orientation-landscape` and `rendition:orientation-portrait`. Does a validator reject it?

## Clause

EPUB 3.3, [`orientation-overrides`](https://www.w3.org/TR/epub-33/#orientation-overrides):

> EPUB creators MUST NOT use more than one of these overrides on any given spine item.

## Expected result

Invalid. Only one orientation override is allowed on a spine item.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i orientation-two-overrides.epub -u --advisory` | ERROR RSC-005, USAGE OBS-001, USAGE OBS-001; INVALID | `orientation-two-overrides.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck orientation-two-overrides.epub -u` | USAGE OBS-001, USAGE OBS-001, ERROR RSC-005; INVALID | `orientation-two-overrides.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OBS-001 (once for each property) says the orientation overrides are outdated. EPUB 3.3 does not deprecate them; the message is at usage level, so it does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and the content document's `itemref` gets `properties="rendition:orientation-landscape rendition:orientation-portrait"`.

## History

- 2026-11-11: First version.
