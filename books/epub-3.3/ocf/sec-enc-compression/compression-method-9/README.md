# A Compression property with Method 9

- Book: `compression-method-9.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-enc-compression/compression-method-9/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#530](https://github.com/veripublica/epub-test-books/issues/530)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

As in aes-compressed-first, OEBPS/content.xhtml is compressed with Deflate, then encrypted, but the Compression element in META-INF/encryption.xml gives Method 9. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The Compression element's Method must be 0 or 8.

## Question

The Compression property in `META-INF/encryption.xml` gives `Method="9"`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-enc-compression`](https://www.w3.org/TR/epub-33/#sec-enc-compression):

> When stored in an OCF ZIP container, EPUB creators SHOULD compress streams of data with non-codec content types before encrypting them.
>
> EPUB creators MUST use Deflate compression.

EPUB 3.3, [`sec-enc-compression`](https://www.w3.org/TR/epub-33/#sec-enc-compression), the `Method` attribute of `Compression`:

> Value is either "0" (no compression) or "8" (Deflate algorithm).

## Expected result

Invalid. The Compression element's Method must be 0 or 8.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i compression-method-9.epub -u --advisory` | ERROR RSC-005, INFO RSC-004; INVALID | `compression-method-9.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck compression-method-9.epub -u` | ERROR RSC-005, INFO RSC-004; INVALID | `compression-method-9.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Both report the `Method` value against the encryption.xml schema (RSC-005), and INFO RSC-004 for the encrypted document.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The same build as `aes-compressed-first`, with `Method="9"` on the `Compression` element.

## History

- 2026-11-13: First version.
