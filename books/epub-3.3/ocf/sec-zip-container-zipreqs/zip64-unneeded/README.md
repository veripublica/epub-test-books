# ZIP64 sizes on an entry that does not need them (valid)

- Book: `zip64-unneeded.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-zipreqs/zip64-unneeded/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml, a file of a few hundred bytes, is written with ZIP64 sizes in both of its ZIP headers. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. ZIP64 is allowed. Using it where the content does not need it breaks only a SHOULD, and the version needed to extract is 45, as ZIP64 asks. A warning would fit.

## Question

`OEBPS/content.xhtml`, a small file, is written with ZIP64 sizes in both headers. Does a validator accept the container?

## Clause

EPUB 3.3, [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs):

> OCF ZIP containers MAY use the ZIP64 extensions defined as "Version 1" in section V, subsection G of the application note [zip] and SHOULD use only those extensions when the content requires them.

EPUB 3.3, [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs):

> In the local file header table, EPUB creators MUST set the version needed to extract fields to the values 10, 20 or 45 to match the maximum version level needed by the given file (e.g., 20 for Deflate, 45 for ZIP64).

## Expected result

Valid. ZIP64 is allowed. Using it where the content does not need it breaks only a SHOULD, and the version needed to extract is 45, as ZIP64 asks. A warning would fit.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i zip64-unneeded.epub -u --advisory` | no findings; VALID | `zip64-unneeded.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck zip64-unneeded.epub -u` | no findings; VALID | `zip64-unneeded.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Neither warns about the ZIP64 fields, so the broken SHOULD goes unreported. That does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/content.xhtml` is written with ZIP64 sizes, as some ZIP writers do for every entry: its local and central headers set the 32-bit compressed and uncompressed sizes to 0xFFFFFFFF, and each carries a ZIP64 extended information extra field (header ID 0x0001, 16 bytes) with the real sizes. The version needed to extract is 45, and the central header's version made by is 4.5. The entry's offset stays in the 32-bit field. Everything else, `mimetype` included, is written as usual. Written by `scripts/lib/rawzip.py` (`zip64=True`). `unzip -t` and Python's `zipfile` read every entry.

## History

- 2026-11-13: First version.
