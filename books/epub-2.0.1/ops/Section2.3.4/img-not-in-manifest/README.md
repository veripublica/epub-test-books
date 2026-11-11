# An `img` of a file that is not in the manifest

- Book: `img-not-in-manifest.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.3.4/img-not-in-manifest/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an img whose JPEG is in the container but not listed in the manifest. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The image must be listed in the manifest.

## Question

`content.xhtml` has an `img` whose JPEG is in the container but not listed in the manifest. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section2.3.4`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.3.4):

> The required URI attribute, src, is used to reference the image resource, which must be listed in the Manifest.

## Expected result

Invalid. The image must be listed in the manifest.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i img-not-in-manifest.epub -u --advisory` | ERROR RSC-008, USAGE OPF-003; INVALID | `img-not-in-manifest.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck img-not-in-manifest.epub -u` | ERROR RSC-008, USAGE OPF-003; INVALID | `img-not-in-manifest.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-003 says the container holds a file that the manifest does not list. That is the same defect seen from the container, not a second one.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

`OEBPS/image.jpg` is put in the container without a manifest item, and `content.xhtml` holds `<img src="image.jpg" alt="A small gray square."/>`.

## History

- 2026-11-11: First version.
