# An `object` of a BMP with no fallback

- Book: `object-bmp-no-fallback.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.3.6/object-bmp-no-fallback/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: [#308](https://github.com/veripublica/epub-test-books/issues/308)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an empty object element whose data is a BMP image, with no nested fallback and no text. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. BMP is not a core media type, and the object gives no fallback.

## Question

`content.xhtml` has an empty `object` whose `data` is a BMP image, with no nested fallback and no text. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section2.3.6`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.3.6):

> When adding objects whose data media type is not drawn from the OPS Core Media Type list or which reference an object implementation using the classid attribute, the object element must specify fallback information for the object, such as another object, an img element, or descriptive text.

## Expected result

Invalid. BMP is not a core media type, and the object gives no fallback.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i object-bmp-no-fallback.epub -u --advisory` | ERROR RSC-032; INVALID | `object-bmp-no-fallback.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck object-bmp-no-fallback.epub -u` | ERROR RSC-032; INVALID | `object-bmp-no-fallback.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/image.bmp` (a generated gray BMP) is added to the manifest, and `content.xhtml` holds `<object data="image.bmp" type="image/bmp"></object>`.

## History

- 2026-11-11: First version.
