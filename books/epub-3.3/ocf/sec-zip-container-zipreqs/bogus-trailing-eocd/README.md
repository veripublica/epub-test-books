# A bogus end-of-central-directory record after the real one

- Book: `bogus-trailing-eocd.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-zipreqs/bogus-trailing-eocd/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: epubveri
- Issue: [#2](https://github.com/veripublica/epub-test-books/issues/2)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The question: a second end-of-central-directory record follows the real one at the end of the file, and it describes a central directory that cannot exist. Does a validator reject the container?

Everything before those last 22 bytes is the EPUB 3 template, which raises no finding.

Expected result: invalid. A ZIP file must have only one end-of-central-directory record, and the one a reader finds by searching from the end points to a central directory that is not there, so the container cannot be opened.

## Question

A ZIP file ends with two end-of-central-directory (EOCD) records. The second
says the central directory is 999 bytes long at offset 99999, which does not
fit before it. Does a validator reject the container?

## Clause

EPUB 3.3, [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs):

> An OCF ZIP container uses the ZIP format as specified by [zip], but with the
> following constraints and clarifications

[ZIP application note 6.3.10](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT), 4.3.1:

> A ZIP file MUST have only one "end of central directory record".

## Expected result

Invalid, at the level that stops the check: the container cannot be read.
The file has two EOCD records, which the ZIP format forbids. A reader that
looks for the EOCD from the end of the file, as ZIP readers do, finds the
bogus one, and its central directory does not exist.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i bogus-trailing-eocd.epub -u --advisory` | FATAL PKG-008, INVALID | `bogus-trailing-eocd.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck bogus-trailing-eocd.epub -u` | FATAL PKG-008 | `bogus-trailing-eocd.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. Both
reject the record because the central directory it describes does not fit
in the file. epubcheck reports it where it opens the container
(`OCFChecker`); epubveri makes the same check. Neither verifier checks the
one-record rule on its own: they reject this file because of what the
second record points to.

## Other readers

- `unzip -t` (Info-ZIP 6.00): refuses the file.
- Python `zipfile`: refuses the file ("Bad magic number for central
  directory").

## Build

The EPUB 3 template is built for this set, then 22 bytes are appended:
`PK\x05\x06`, then the little-endian fields disk 0, disk with the central
directory 0, entries here 9, entries 9, central directory size 999, offset
99999, comment length 0. The script checks first that the file ends with the
template's own EOCD and no comment.

## History

- 2026-11-08: First version.
