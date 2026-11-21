# The data-descriptor flag with no data descriptor

- Book: `descriptor-flag-no-footer.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-zipreqs/descriptor-flag-no-footer/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: epubveri; parked on 2026-11-08 while both verifiers missed it, shipped after epubveri 0.43.0 reports it
- Issue: [#624](https://github.com/veripublica/epub-test-books/issues/624)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Bit 3 of the general purpose flag is set for OEBPS/content.xhtml, but no data descriptor follows its data. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. When bit 3 is set, a data descriptor must follow the file's data.

## Question

Bit 3 of the general purpose bit flag is set in the local and the central header of `OEBPS/content.xhtml`, but no data descriptor follows its data. Does a validator reject the container?

## Clause

EPUB 3.3, [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs):

> An OCF ZIP container uses the ZIP format as specified by [zip], but with the following constraints and clarifications

[ZIP application note 6.3.10](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT), 3.1 and 4.3.9.1:

> Use of the term MUST or SHALL indicates a required element.

> This descriptor MUST exist if bit 3 of the general purpose bit flag is set (see below). It is byte aligned and immediately follows the last byte of compressed data.

## Expected result

Invalid. Bit 3 is set, so a data descriptor must follow the compressed data, and none does: the next local header starts right after it.

The local header also keeps its CRC-32 and sizes, where 4.4.7 to 4.4.9 say they "are set to zero" when bit 3 is set. That is not stated as a MUST, and the verdict does not rest on it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.48.0 | `epubveri -i descriptor-flag-no-footer.epub -u --advisory` | ERROR SPEC-007; INVALID | `descriptor-flag-no-footer.epubveri-0.48.0.txt` |
| epubcheck 5.4.0 | `epubcheck descriptor-flag-no-footer.epub -u` | no findings; VALID | `descriptor-flag-no-footer.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1779](https://github.com/w3c/epubcheck/issues/1779).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Other readers

- `unzip -t` (Info-ZIP 6.00): no errors.
- Python `zipfile` (3.14): reads every file.

## Build

The EPUB 3 template is built for this set, then bit 3 is set in the general purpose flag of `OEBPS/content.xhtml`, in its local and its central header. Nothing is added after its data. The script checks first that bit 3 is clear in both headers.

## History

- 2026-11-08: First version, parked.
- 2026-11-15: Measured on epubveri 0.43.0 and added to the library.
