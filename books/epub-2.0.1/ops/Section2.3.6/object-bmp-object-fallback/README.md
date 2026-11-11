# An `object` of a BMP with a nested JPEG `object` as fallback (valid)

- Book: `object-bmp-object-fallback.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.3.6/object-bmp-object-fallback/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, for the OPS 2.0.1 content document sets
- Issue: [#315](https://github.com/veripublica/epub-test-books/issues/315)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an object element whose data is a BMP image, and inside it a second object element whose data is a JPEG image in the manifest. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. BMP is not a core media type, but the object gives another object, of a core media type, as its fallback.

## Question

`content.xhtml` has an `object` whose `data` is a BMP image, and inside it a second `object` of a JPEG in the manifest. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section2.3.6`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.3.6):

> When adding objects whose data media type is not drawn from the OPS Core Media Type list or which reference an object implementation using the classid attribute, the object element must specify fallback information for the object, such as another object, an img element, or descriptive text.

## Expected result

Valid. BMP is not a core media type, but the object gives another object, of a core media type, as its fallback.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i object-bmp-object-fallback.epub -u --advisory` | no findings; VALID | `object-bmp-object-fallback.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck object-bmp-object-fallback.epub -u` | ERROR RSC-032; INVALID | `object-bmp-object-fallback.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports that the BMP has no fallback (RSC-032), because in an EPUB 2 book it does not count a nested object inside the `object` as one.

- **epubcheck: wrong error.** [w3c/epubcheck#1764](https://github.com/w3c/epubcheck/issues/1764).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/image.bmp` (a generated gray BMP) and `OEBPS/image.jpg` (a generated gray JPEG) are added to the manifest, and `content.xhtml` holds `<object data="image.bmp" type="image/bmp"><object data="image.jpg" type="image/jpeg">A small gray square.</object></object>`.

## History

- 2026-11-11: First version.
