# A file whose 'version needed to extract' is 63

- Book: `version-needed-63.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section4/version-needed-63/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer; parked on 2026-11-12 while both verifiers missed it, shipped after epubveri 0.42.0 reports it
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The ZIP headers of OEBPS/content.xhtml give 63 as the version needed to extract. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The version needed to extract must be 10, 20 or 45.

## Question

The ZIP headers of `OEBPS/content.xhtml` give 63 as the version needed to extract. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 4](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (ZIP Container; Recommended Specification, 4 September 2010):

> In the local file header table, Conforming OCF ZIP Containers MUST set the ‘version needed to extract’ fields to the values 10, 20 or 45 in order to match the maximum version level needed by the given file (e.g., 20 if Deflate is needed, 45 if ZIP64 is needed).

## Expected result

Invalid. The version needed to extract must be 10, 20 or 45.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i version-needed-63.epub -u --advisory` | ERROR SPEC-004; INVALID | `version-needed-63.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck version-needed-63.epub -u` | no findings; VALID | `version-needed-63.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. The content document's entry gives version needed 63 in its local and central headers; it is still deflated.

## History

- 2026-11-13: First version.
