# `rendition:spread` declared twice

- Book: `spread-twice.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/spread/spread-twice/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package declares rendition:spread twice, as none and as both. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. The property is declared more than once.

## Question

The package declares `rendition:spread` twice, as `none` and as `both`. Does a validator reject it?

## Clause

EPUB 3.3, [`spread`](https://www.w3.org/TR/epub-33/#spread):

> EPUB creators MUST NOT declare the rendition:spread property more than once. They also MUST NOT declare the property using the refines attribute.

## Expected result

Invalid. The property is declared more than once.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i spread-twice.epub -u --advisory` | ERROR RSC-005, USAGE OBS-001, USAGE OBS-001; INVALID | `spread-twice.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck spread-twice.epub -u` | USAGE OBS-001, USAGE OBS-001, ERROR RSC-005; INVALID | `spread-twice.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OBS-001 (once for each element) says the `rendition:spread` property is outdated. EPUB 3.3 deprecates only its `portrait` value, but the EPUB 3.4 draft lists the property as outdated (change log, 18 December 2025); the message is at usage level, so it does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and two `rendition:spread` meta elements, `none` and `both`.

## History

- 2026-11-11: First version.
