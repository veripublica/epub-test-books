# Central-directory offset 4 bytes short

- Book: `cd-offset-shifted.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-zipreqs/cd-offset-shifted/build.py`
- Origin: built here
- Asked for by: epubveri
- Issue: [#4](https://github.com/veripublica/epub-test-books/issues/4)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The question: the end-of-central-directory record gives the start of the central directory 4 bytes too early. Does a validator reject the container?

Everything except those 4 bytes is the EPUB 3 template, which raises no finding.

Expected result: invalid. The offset field must hold where the central directory starts, and it does not, so no entry can be read where the file says it is.

## Question

The 4-byte "offset of start of central directory" field in the EOCD record
holds a value 4 smaller than the real offset. Nothing else changes. Does a
validator reject the container?

## Clause

EPUB 3.3, [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs):

> An OCF ZIP container uses the ZIP format as specified by [zip], but with the
> following constraints and clarifications

[ZIP application note 6.3.10](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT),
4.4.24, offset of start of central directory:

> Offset of the start of the central directory on the disk on which the
> central directory starts.

## Expected result

Invalid. The field does not hold the offset it is defined to hold. Readers
find the central directory from the EOCD's position and size, take the
4-byte difference as a prefix, and then look for every local header 4 bytes
too far. No entry can be read, `META-INF/container.xml` first among them.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.37.1 | `epubveri -i cd-offset-shifted.epub -u --advisory` | FATAL PKG-008 on `META-INF/container.xml`, ERROR RSC-003, INVALID | `cd-offset-shifted.epubveri-0.37.1.txt` |
| epubcheck 5.4.0 | `epubcheck cd-offset-shifted.epub -u` | FATAL PKG-008 on `META-INF/container.xml`, ERROR RSC-003 | `cd-offset-shifted.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. PKG-008 is
the failed read of `container.xml`; RSC-003 follows from it, because without
that file no package document is declared.

## Other readers

- `unzip -t` (Info-ZIP 6.00): reports errors.
- Python `zipfile`: opens the archive and lists every entry, but can read
  none of them ("Bad magic number for file header").

## Build

The EPUB 3 template is built for this set, then 4 is subtracted from the
central directory offset in the EOCD record. The script checks first that
the field points at the central directory.

## History

- 2026-11-08: First version.
