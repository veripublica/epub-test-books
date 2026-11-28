# 22 bytes inside the `mimetype` data

- Book: `mimetype-data-shift.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-zipreqs/mimetype-data-shift/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: epubveri; parked on 2026-11-08 while both verifiers missed it, shipped after epubveri 0.43.0 reports it
- Issue: [#628](https://github.com/veripublica/epub-test-books/issues/628)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

22 bytes are inserted inside the stored mimetype data, so every offset after it is 22 bytes off. No header is changed. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A reader that shifts every offset by the same 22 bytes finds every file except mimetype, and the local header of mimetype then has no central directory header.

## Question

22 bytes (an end-of-central-directory signature and 18 zero bytes) are inserted at file offset 40, inside the stored `mimetype` data. No header and no offset is changed, so every offset after that point is 22 bytes off. Does a validator reject the container?

## Clause

EPUB 3.3, [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs):

> An OCF ZIP container uses the ZIP format as specified by [zip], but with the following constraints and clarifications

[ZIP application note 6.3.10](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT), 3.1 and 4.3.2:

> Use of the term MUST or SHALL indicates a required element.

> Each file placed into a ZIP file MUST be preceded by a "local file header" record for that file. Each "local file header" MUST be accompanied by a corresponding "central directory header" record within the central directory section of the ZIP file.

## Expected result

Invalid. The end-of-central-directory record says where the central directory starts, and it is really 22 bytes later. Readers take such a gap as data in front of the archive and move every offset by it. That finds the local header of every file except `mimetype`: its central header says offset 0, which becomes 22, and there is no local header there. The local header at offset 0 is then not accompanied by a central directory header, which 4.3.2 requires.

The shifted reading is what makes the other files readable. Read without the shift, every file but `mimetype` is lost instead, and the container is still not a ZIP file as the application note defines it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.50.0 | `epubveri -i mimetype-data-shift.epub -u --advisory` | ERROR SPEC-008; INVALID | `mimetype-data-shift.epubveri-0.50.0.txt` |
| epubcheck 5.4.0 | `epubcheck mimetype-data-shift.epub -u` | no findings; VALID | `mimetype-data-shift.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1779](https://github.com/w3c/epubcheck/issues/1779).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Other readers

- `unzip -t` (Info-ZIP 6.00): finds the 22-byte gap, says it is "attempting to re-compensate", and reports errors.
- Python `zipfile` (3.14): lists every entry and reads every file except `mimetype` ("Bad magic number for file header").

## Build

The EPUB 3 template is built for this set, then 22 bytes (`PK\x05\x06` and 18 zero bytes) are inserted at file offset 40, two bytes into the stored `mimetype` data. The script checks first that bytes 30 to 37 are the name `mimetype`.

## History

- 2026-11-08: First version, parked.
- 2026-11-15: Measured on epubveri 0.43.0 and added to the library.
