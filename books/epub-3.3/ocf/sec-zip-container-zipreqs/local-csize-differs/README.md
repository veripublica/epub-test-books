# Local compressed size 7 bytes larger than the central one (valid)

- Book: `local-csize-differs.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-zipreqs/local-csize-differs/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: epubveri; parked on 2026-11-08 until the ZIP rule was read, shipped as valid on 2026-11-15
- Issue: [#626](https://github.com/veripublica/epub-test-books/issues/626)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The compressed size in the local header of OEBPS/content.xhtml is 7 bytes larger than in its central directory header. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The ZIP application note has no rule that the fields of a local header and its central directory header must match.

## Question

The compressed size in the local header of `OEBPS/content.xhtml` is 7 bytes larger than the one in its central directory header, which is right. Does a validator accept the container?

## Clause

EPUB 3.3, [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs):

> An OCF ZIP container uses the ZIP format as specified by [zip], but with the following constraints and clarifications

[ZIP application note 6.3.10](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT), 4.3.2:

> Each file placed into a ZIP file MUST be preceded by a "local file header" record for that file. Each "local file header" MUST be accompanied by a corresponding "central directory header" record within the central directory section of the ZIP file.

## Expected result

Valid. The local header is there and has its central directory header, which is what 4.3.2 asks. The application note asks for a "corresponding" record, not for equal fields, and no other rule in it says the two compressed sizes must be the same. When bit 3 is set, 4.4.8 even has the local size be zero while the central one is not. EPUB 3.3 adds no rule of its own here.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.50.0 | `epubveri -i local-csize-differs.epub -u --advisory` | no findings; VALID | `local-csize-differs.epubveri-0.50.0.txt` |
| epubcheck 5.4.0 | `epubcheck local-csize-differs.epub -u` | no findings; VALID | `local-csize-differs.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Other readers

- `unzip -t` (Info-ZIP 6.00): no errors.
- Python `zipfile` (3.14): reads every file.

## Build

The EPUB 3 template is built for this set, then 7 is added to the compressed size in the local header of `OEBPS/content.xhtml`. The script checks first that the local and central sizes are equal.

## History

- 2026-11-08: First version, parked.
- 2026-11-15: Measured on epubveri 0.43.0 and added to the library as valid: no rule in the application note asks the two headers to match.
