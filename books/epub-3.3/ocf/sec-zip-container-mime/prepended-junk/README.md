# Junk before the first local header

- Book: `prepended-junk.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-mime/prepended-junk/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: epubveri
- Issue: [#3](https://github.com/veripublica/epub-test-books/issues/3)
- Also touches: [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The question: 16 bytes of junk come before the first entry of the ZIP file, and no offset inside the file is adjusted for them. Does a validator reject the container?

Everything after those first 16 bytes is the EPUB 3 template, which raises no finding.

Expected result: invalid. The mimetype file must be the first file in the container, and an EPUB file is identified by its first bytes, which here are not a ZIP local header.

## Question

The file starts with `JUNKJUNKJUNKJUNK`, then the template's ZIP bytes,
unchanged. Every offset in the central directory is now 16 bytes short of
the header it points to. Does a validator reject the container?

## Clause

EPUB 3.3, [`sec-zip-container-mime`](https://www.w3.org/TR/epub-33/#sec-zip-container-mime):

> EPUB creators MUST include the mimetype file as the first file in the OCF
> ZIP container.

EPUB 3.3, [I.2 The application/epub+zip media type](https://www.w3.org/TR/epub-33/#app-media-type),
magic numbers:

> 0: PK 0x03 0x04, 30: mimetype, 38: application/epub+zip

[ZIP application note 6.3.10](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT),
4.4.16, relative offset of local header:

> This is the offset from the start of the first disk on which this file
> appears, to where the local header SHOULD be found.

## Expected result

Invalid, at the level that stops the check. The file does not begin with a
local header, so it does not carry the magic numbers that identify an EPUB,
and the mimetype file is not at the start. The offsets in the central
directory do not point to the local headers.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i prepended-junk.epub -u --advisory` | FATAL PKG-004, INVALID | `prepended-junk.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck prepended-junk.epub -u` | FATAL PKG-004 | `prepended-junk.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. Before any
ZIP parsing, both read the first bytes of the file as a local header, find
no `PK`, and stop (epubcheck: `OCFZipChecker`).

## Other readers

This is the set where validators and ZIP readers part ways. ZIP readers
treat the 16 bytes as a prefix, as they do for self-extracting archives, and
read every entry:

- `unzip -t` (Info-ZIP 6.00): warns about 16 extra bytes at the beginning,
  then tests every entry without error (exit 1, a warning).
- Python `zipfile`: reads every entry.

So a tool that repairs or converts books may open this file without
complaint and write a valid book from it, while a validator rejects the
original.

## Build

The EPUB 3 template is built for this set, then `JUNKJUNKJUNKJUNK` is put in
front of it. No offset is changed. The script checks first that the template
starts with a local header.

## History

- 2026-11-08: First version.
