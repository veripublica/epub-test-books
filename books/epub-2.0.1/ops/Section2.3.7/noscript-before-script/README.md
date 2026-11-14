# A `noscript` before its `script`

- Book: `noscript-before-script.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.3.7/noscript-before-script/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, for the OPS 2.0.1 content document sets; parked on 2026-11-11 while both verifiers missed it, shipped after epubveri reports it
- Issue: [#613](https://github.com/veripublica/epub-test-books/issues/613)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a noscript element and then a script element, in that order. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. A noscript must come after the script it belongs to, and here it comes before it.

## Question

In `content.xhtml`, a `noscript` element comes right before the only `script` element. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section2.3.7`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.3.7):

> If noscript is included, whose purpose is to display some message if the Reading System chooses not to execute the script, it must appear after the closing tag of the script it is associated with.

## Expected result

Invalid. A `noscript` must come after the `script` it belongs to, and here it comes before it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.43.0 | `epubveri -i noscript-before-script.epub -u --advisory` | ERROR RSC-005; INVALID | `noscript-before-script.epubveri-0.43.0.txt` |
| epubcheck 5.4.0 | `epubcheck noscript-before-script.epub -u` | no findings; VALID | `noscript-before-script.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds `<noscript><p>No script.</p></noscript>` and then `<script type="text/javascript">var a = 1;</script>`.

## History

- 2026-11-11: First version, parked.
- 2026-11-15: Measured on epubveri 0.43.0 and added to the library.
