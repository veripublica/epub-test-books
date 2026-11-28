# An `object` whose `type` differs from the manifest

- Book: `object-type-mismatch.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.3.6/object-type-mismatch/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, for the OPS 2.0.1 content document sets; parked on 2026-11-11 while both verifiers missed it, shipped after epubveri reports it
- Issue: [#612](https://github.com/veripublica/epub-test-books/issues/612)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an object element of a JPEG image whose type attribute says image/png. The manifest gives image/jpeg. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The type of an object must match the media type in the manifest, and image/png does not match image/jpeg.

## Question

In `content.xhtml`, an `object` points to `image.jpg` with `type="image/png"`; the manifest gives `image/jpeg`. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section2.3.6`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.3.6):

> The MIME media type values for the codetype and type attributes must match those specified in the Publication's Manifest.

## Expected result

Invalid. The `type` of an `object` must match the media type in the manifest, and `image/png` does not match `image/jpeg`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i object-type-mismatch.epub -u --advisory` | ERROR OPF-013; INVALID | `object-type-mismatch.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck object-type-mismatch.epub -u` | no findings; VALID | `object-type-mismatch.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1780](https://github.com/w3c/epubcheck/issues/1780).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/image.jpg` is added to the manifest as `image/jpeg`, and `content.xhtml` holds `<object data="image.jpg" type="image/png">A small gray square.</object>` in a `div`.

## History

- 2026-11-11: First version, parked.
- 2026-11-15: Measured on epubveri 0.43.0 and added to the library.
