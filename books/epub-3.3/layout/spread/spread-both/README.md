# `rendition:spread` set to `both` (valid)

- Book: `spread-both.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/spread/spread-both/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#247](https://github.com/veripublica/epub-test-books/issues/247)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package sets rendition:spread to both. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid. `both` is one of the values.

## Question

The fixed-layout package sets `rendition:spread` to `both`. Does a validator accept it?

## Clause

EPUB 3.3, [`spread`](https://www.w3.org/TR/epub-33/#spread):

> EPUB creators MUST use one of the following values with the rendition:spread property: none […] landscape […] portrait (deprecated) […] both […] auto […]

## Expected result

Valid. `both` is one of the values.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i spread-both.epub -u --advisory` | USAGE OBS-001; VALID | `spread-both.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck spread-both.epub -u` | USAGE OBS-001; VALID | `spread-both.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OBS-001 says the `rendition:spread` property is outdated. EPUB 3.3 deprecates only its `portrait` value, but the EPUB 3.4 draft lists the property as outdated (change log, 18 December 2025); the message is at usage level, so it does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and `<meta property="rendition:spread">both</meta>`.

## History

- 2026-11-11: First version.
