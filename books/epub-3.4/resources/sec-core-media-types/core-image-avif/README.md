# An AVIF image with no fallback (valid)

- Book: `core-image-avif.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.4/resources/sec-core-media-types/core-image-avif/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, from the EPUB 3.4 core media types (w3c/epub-specs#2794)
- Issue: [#715](https://github.com/veripublica/epub-test-books/issues/715)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml shows image.avif, a 16 by 16 gray AVIF image, in an img element. Its manifest item is image/avif and has no fallback. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. EPUB 3.4 makes image/avif a core media type, so it needs no fallback.

## Question

`content.xhtml` shows an AVIF image, `image/avif`, with no fallback. Does a validator accept the book?

## Clause

EPUB 3.4, [`sec-core-media-types`](https://www.w3.org/TR/epub-34/#sec-core-media-types) (3.2 Core media types; Candidate Recommendation Draft, 25 November 2026):

> Publication resources that conform to the MIME media type [rfc2046] specifications defined in the following table MAY be included in EPUB publications without fallbacks when they are used in EPUB content documents and foreign content documents.

> | image/avif | [av1-avif] | AVIF images | 3.4 |

## Expected result

Valid. `image/avif` is a core media type in EPUB 3.4, so an `img` may use it without a fallback.

In EPUB 3.3 AVIF is a foreign resource, so the same book needs a fallback there and is invalid without one.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i core-image-avif.epub -u --advisory` | no findings; VALID | `core-image-avif.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck core-image-avif.epub -u` | no findings; VALID | `core-image-avif.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<p><img src="image.avif" alt="A small gray square."/></p>` in `content.xhtml`, and `OEBPS/image.avif` (`image/avif`) in the manifest. The image is a 16 by 16 gray AVIF, kept as bytes in `scripts/lib/encodedmedia.py` with the command that made it.

## History

- 2026-11-28: First version.
