# An `img` of a JPEG in the manifest (valid)

- Book: `img-jpeg.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.3.4/img-jpeg/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: [#305](https://github.com/veripublica/epub-test-books/issues/305)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an img whose src is a JPEG image listed in the manifest. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. JPEG is a core media type and the image is in the manifest.

## Question

`content.xhtml` has an `img` whose `src` is a JPEG listed in the manifest. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section2.3.4`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.3.4):

> The required URI attribute, src, is used to reference the image resource, which must be listed in the Manifest.

## Expected result

Valid. JPEG is a core media type and the image is in the manifest.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i img-jpeg.epub -u --advisory` | no findings; VALID | `img-jpeg.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck img-jpeg.epub -u` | no findings; VALID | `img-jpeg.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/image.jpg` (a generated 8×8 gray JPEG) is added to the manifest, and `content.xhtml` holds `<img src="image.jpg" alt="A small gray square."/>`.

## History

- 2026-11-11: First version.
