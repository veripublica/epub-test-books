# An `object` of a BMP with descriptive text as fallback (valid)

- Book: `object-bmp-text-fallback.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.3.6/object-bmp-text-fallback/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, for the OPS 2.0.1 content document sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an object element whose data is a BMP image, with descriptive text inside it as its only fallback. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. BMP is not a core media type, but the object gives descriptive text as its fallback.

## Question

`content.xhtml` has an `object` whose `data` is a BMP image, with descriptive text inside it as its only fallback. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section2.3.6`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.3.6):

> When adding objects whose data media type is not drawn from the OPS Core Media Type list or which reference an object implementation using the classid attribute, the object element must specify fallback information for the object, such as another object, an img element, or descriptive text.

## Expected result

Valid. BMP is not a core media type, but the object gives descriptive text as its fallback.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i object-bmp-text-fallback.epub -u --advisory` | no findings; VALID | `object-bmp-text-fallback.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck object-bmp-text-fallback.epub -u` | ERROR RSC-032; INVALID | `object-bmp-text-fallback.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports that the BMP has no fallback (RSC-032), because in an EPUB 2 book it does not count descriptive text inside the `object` as one.

- **epubcheck: wrong error.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/image.bmp` (a generated gray BMP) is added to the manifest, and `content.xhtml` holds `<object data="image.bmp" type="image/bmp">A small gray square.</object>`.

## History

- 2026-11-11: First version.
