# A content document with the deprecated `text/x-oeb1-document` type (valid)

- Book: `mime-oeb1-document.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section1.4.1.2/mime-oeb1-document/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: [#295](https://github.com/veripublica/epub-test-books/issues/295)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The manifest gives content.xhtml the media type text/x-oeb1-document, which OPS 2.0.1 keeps but deprecates. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. The type is deprecated but still one of the two allowed. A warning would fit.

## Question

The manifest gives `content.xhtml` the media type `text/x-oeb1-document`, which OPS 2.0.1 keeps but deprecates. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section1.4.1.2`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.4.1.2):

> A conformant XHTML Content Document must meet these conditions:

> it has a MIME media type of either application/xhtml+xml or text/x-oeb1-document (deprecated); and

## Expected result

Valid. The type is deprecated but still one of the two allowed. A warning would fit.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i mime-oeb1-document.epub -u --advisory` | no findings; VALID | `mime-oeb1-document.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck mime-oeb1-document.epub -u` | WARNING OPF-037; VALID | `mime-oeb1-document.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

epubcheck gives WARNING OPF-037 for the deprecated media type; epubveri gives nothing. A warning does not change the verdict, and OPS 2.0.1 does not ask checkers to report deprecated features.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In the manifest, the `content` item's `media-type` is `text/x-oeb1-document`.

## History

- 2026-11-11: First version.
