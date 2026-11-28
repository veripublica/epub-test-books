# Local header says stored, central header says deflated (valid)

- Book: `local-method-differs.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-zipreqs/local-method-differs/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: epubveri; parked on 2026-11-08 until the ZIP rule was read, shipped as valid on 2026-11-15
- Issue: [#627](https://github.com/veripublica/epub-test-books/issues/627)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The local header of OEBPS/content.xhtml says stored, while its central directory header says deflated. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The ZIP application note has no rule that the fields of a local header and its central directory header must match.

## Question

The local header of `OEBPS/content.xhtml` gives compression method 0 (stored). Its central directory header keeps method 8 (deflated), and the data is deflated. Does a validator accept the container?

## Clause

EPUB 3.3, [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs):

> An OCF ZIP container uses the ZIP format as specified by [zip], but with the following constraints and clarifications

[ZIP application note 6.3.10](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT), 4.3.2:

> Each file placed into a ZIP file MUST be preceded by a "local file header" record for that file. Each "local file header" MUST be accompanied by a corresponding "central directory header" record within the central directory section of the ZIP file.

## Expected result

Valid. The local header is there and has its central directory header, which is what 4.3.2 asks. The application note asks for a "corresponding" record, not for equal fields, and no other rule in it says the two compression methods must be the same. When bit 3 is set, 4.4.7 to 4.4.9 even have the two headers differ on purpose. EPUB 3.3 adds no rule of its own here.

A reader that trusts the local header gets the deflated bytes as they are, so the book may still fail in some readers. That is a question for those readers, not a rule the container breaks.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i local-method-differs.epub -u --advisory` | no findings; VALID | `local-method-differs.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck local-method-differs.epub -u` | no findings; VALID | `local-method-differs.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Other readers

- `unzip -t` (Info-ZIP 6.00): follows the local header, takes the deflated bytes as stored, and reports a bad CRC for `OEBPS/content.xhtml`.
- Python `zipfile` (3.14): follows the central header and reads every file.

## Build

The EPUB 3 template is built for this set, then the compression method in the local header of `OEBPS/content.xhtml` is changed from 8 to 0. The script checks first that both headers say 8.

## History

- 2026-11-08: First version, parked.
- 2026-11-15: Measured on epubveri 0.43.0 and added to the library as valid: no rule in the application note asks the two headers to match.
