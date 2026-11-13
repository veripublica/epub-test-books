# A content fallback chain with no core media type

- Book: `content-fallback-no-core.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-manifest-fallbacks/content-fallback-no-core/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#133](https://github.com/veripublica/epub-test-books/issues/133)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An img shows a BMP whose manifest fallback is another foreign image. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The chain must hold a core media type resource.

## Question

An `img` shows a BMP whose manifest fallback is another foreign image. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-manifest-fallbacks`](https://www.w3.org/TR/epub-33/#sec-manifest-fallbacks):

> EPUB creators MUST provide a content fallback for foreign resources when the elements that reference them do not have intrinsic fallback capabilities. In this case, the fallback chain MUST contain at least one core media type resource.

## Expected result

Invalid. The chain must hold a core media type resource.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i content-fallback-no-core.epub -u --advisory` | ERROR RSC-032, USAGE OBS-001, USAGE OPF-097; INVALID | `content-fallback-no-core.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck content-fallback-no-core.epub -u` | USAGE OPF-097, USAGE OBS-001, ERROR RSC-032; INVALID | `content-fallback-no-core.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect. USAGE OBS-001 says a manifest content fallback is outdated. That is the feature this book uses, not a defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated BMP and XBM are added, the BMP's `fallback` names the XBM, and `content.xhtml` shows the BMP.

## History

- 2026-11-09: First version.
