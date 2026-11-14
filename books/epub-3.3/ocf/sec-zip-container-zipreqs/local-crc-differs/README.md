# A wrong CRC-32 in the local header only (valid)

- Book: `local-crc-differs.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-zipreqs/local-crc-differs/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: epubveri; parked on 2026-11-08 until the ZIP rule was read, shipped as valid on 2026-11-15
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The CRC-32 in the local header of OEBPS/content.xhtml is wrong. Its central directory header has the right one. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The ZIP application note has no rule that the fields of a local header and its central directory header must match, and the right CRC-32 is still there to check the file.

## Question

The CRC-32 in the local header of `OEBPS/content.xhtml` is `0xDEADBEEF`. The one in its central directory header is the right one for the data. Does a validator accept the container?

## Clause

EPUB 3.3, [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs):

> An OCF ZIP container uses the ZIP format as specified by [zip], but with the following constraints and clarifications

[ZIP application note 6.3.10](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT), 4.1.5 and 4.3.2:

> Data integrity MUST be provided for each file using CRC32.

> Each file placed into a ZIP file MUST be preceded by a "local file header" record for that file. Each "local file header" MUST be accompanied by a corresponding "central directory header" record within the central directory section of the ZIP file.

## Expected result

Valid. The local header is there and has its central directory header, which is what 4.3.2 asks. The application note asks for a "corresponding" record, not for equal fields, and no other rule in it says the two CRC-32 values must be the same. When bit 3 is set, 4.4.7 even has the local value be zero while the central one is not. The CRC-32 in the central header is right, so the file's integrity can still be checked, as 4.1.5 asks. EPUB 3.3 adds no rule of its own here.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.43.0 | `epubveri -i local-crc-differs.epub -u --advisory` | no findings; VALID | `local-crc-differs.epubveri-0.43.0.txt` |
| epubcheck 5.4.0 | `epubcheck local-crc-differs.epub -u` | no findings; VALID | `local-crc-differs.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Other readers

- `unzip -t` (Info-ZIP 6.00): compares the data with the local CRC-32 and reports a bad CRC for `OEBPS/content.xhtml`.
- Python `zipfile` (3.14): checks the central CRC-32 and reads every file.

## Build

The EPUB 3 template is built for this set, then the CRC-32 in the local header of `OEBPS/content.xhtml` is set to `0xDEADBEEF`. The script checks first that the local and central values are equal.

## History

- 2026-11-08: First version, parked.
- 2026-11-15: Measured on epubveri 0.43.0 and added to the library as valid: no rule in the application note asks the two headers to match.
