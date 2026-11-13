# ZIP64 sizes on a file that does not need them (valid)

- Book: `zip64-unneeded.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section4/zip64-unneeded/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml, a file of a few hundred bytes, is written with ZIP64 sizes in both of its ZIP headers. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. ZIP64 is allowed. Using it where the content does not need it breaks only a SHOULD, and the version needed to extract is 45, as ZIP64 asks. A warning would fit.

## Question

`OEBPS/content.xhtml`, a small file, is written with ZIP64 sizes in both headers. Does a validator accept the book?

## Clause

OCF 2.0.1, [section 4](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (ZIP Container; Recommended Specification, 4 September 2010):

> Conforming OCF ZIP Containers MAY use the ZIP64 extensions and SHOULD only use those extensions when the content requires them.

OCF 2.0.1, [section 4](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (ZIP Container; Recommended Specification, 4 September 2010):

> In the local file header table, Conforming OCF ZIP Containers MUST set the ‘version needed to extract’ fields to the values 10, 20 or 45 in order to match the maximum version level needed by the given file (e.g., 20 if Deflate is needed, 45 if ZIP64 is needed).

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
