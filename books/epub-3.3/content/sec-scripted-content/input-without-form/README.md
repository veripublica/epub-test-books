# An input element outside any form, without the scripted property (valid)

- Book: `input-without-form.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-scripted-content/input-without-form/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has one text input element, with no form element around it, and its manifest item has no scripted property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Only the HTML form element makes a document scripted (EPUB 3.3 links "form" to that element), and there is none here.

## Question

`content.xhtml` has an `input` element but no `form` element, and no `scripted` property. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-scripted-content`](https://www.w3.org/TR/epub-33/#sec-scripted-content):

> When an EPUB content document contains scripting, this specification refers to it as a scripted content document. This label also applies to XHTML content documents that contain [html] form elements.

## Expected result

Valid. Only the HTML form element makes a document scripted (EPUB 3.3 links "form" to that element), and there is none here.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i input-without-form.epub -u --advisory` | no findings; VALID | `input-without-form.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck input-without-form.epub -u` | no findings; VALID | `input-without-form.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<p><input type="text" name="q" aria-label="Query"/></p>`. The manifest is not changed.

## History

- 2026-11-13: First version.
