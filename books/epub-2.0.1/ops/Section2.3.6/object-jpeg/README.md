# An `object` of a JPEG (valid)

- Book: `object-jpeg.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.3.6/object-jpeg/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: [#307](https://github.com/veripublica/epub-test-books/issues/307)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an object element whose data is a JPEG image in the manifest. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. JPEG is a core media type, so no fallback is needed.

## Question

`content.xhtml` has an `object` whose `data` is a JPEG in the manifest. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section2.3.6`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.3.6):

> When adding objects whose data media type is not drawn from the OPS Core Media Type list or which reference an object implementation using the classid attribute, the object element must specify fallback information for the object, such as another object, an img element, or descriptive text.

## Expected result

Valid. JPEG is a core media type, so no fallback is needed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i object-jpeg.epub -u --advisory` | no findings; VALID | `object-jpeg.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck object-jpeg.epub -u` | no findings; VALID | `object-jpeg.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/image.jpg` is added to the manifest, and `content.xhtml` holds `<object data="image.jpg" type="image/jpeg">A small gray square.</object>`.

## History

- 2026-11-11: First version.
