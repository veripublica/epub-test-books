# A `script` with a `type` (valid)

- Book: `script-with-type.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.3.7/script-with-type/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The head of content.xhtml has a script element with type="text/javascript". The text is readable without it. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. The script has its type, and the document does not depend on it.

## Question

The `head` of `content.xhtml` has `<script type="text/javascript">`. The text is readable without it. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section2.3.7`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.3.7):

> The attribute type, which specifies the scripting language for script, is required.

> The content must be readable without execution of script elements.

## Expected result

Valid. The script has its type, and the document does not depend on it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i script-with-type.epub -u --advisory` | no findings; VALID | `script-with-type.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck script-with-type.epub -u` | no findings; VALID | `script-with-type.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, `<script type="text/javascript">var a = 1;</script>` is added to `head`.

## History

- 2026-11-11: First version.
