# A `script` with no `type`

- Book: `script-no-type.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.3.7/script-no-type/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: [#309](https://github.com/veripublica/epub-test-books/issues/309)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The head of content.xhtml has a script element with no type attribute. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The `type` attribute is required.

## Question

The `head` of `content.xhtml` has a `script` element with no `type` attribute. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section2.3.7`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.3.7):

> The attribute type, which specifies the scripting language for script, is required.

## Expected result

Invalid. The `type` attribute is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i script-no-type.epub -u --advisory` | ERROR RSC-005; INVALID | `script-no-type.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck script-no-type.epub -u` | ERROR RSC-005; INVALID | `script-no-type.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, `<script>var a = 1;</script>` is added to `head`.

## History

- 2026-11-11: First version.
