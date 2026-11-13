# `dc:language` with an underscore

- Book: `language-malformed.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.2.12/language-malformed/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets; parked on 2026-11-09 until #27's comments had their time, built on 2026-11-13 for the release after 15 November
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The dc:language value is en_US. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. RFC 3066 separates subtags with hyphens.

## Question

The `dc:language` value is `en_US`. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.2.12`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.2.12):

> The content of this element must comply with RFC 3066

## Expected result

Invalid. RFC 3066 separates subtags with hyphens.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i language-malformed.epub -u --advisory` | ERROR OPF-092; INVALID | `language-malformed.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck language-malformed.epub -u` | no findings; VALID | `language-malformed.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it gives no finding.

- **epubcheck: missed.** [w3c/epubcheck#1761](https://github.com/w3c/epubcheck/issues/1761).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `dc:language` becomes `en_US`.

## History

- 2026-11-09: First version, parked.
- 2026-11-13: Measured on epubveri 0.42.0 and added to the library.
