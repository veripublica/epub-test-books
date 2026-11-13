# A form element without the scripted property

- Book: `property-scripted-form-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-resource-properties/property-scripted-form-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a form element with one text input, and its manifest item has no scripted property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A document with a form element is a scripted content document, so its manifest item must have the scripted property.

## Question

`content.xhtml` has a `form` element and no `scripted` property. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> EPUB creators MUST set the following properties whenever a resource referenced by an item element matches their respective definitions:

EPUB 3.3, [`scripted`](https://www.w3.org/TR/epub-33/#scripted):

> The scripted property indicates that the described publication resource is a scripted content document (i.e., contains scripting and/or [html] form elements).

## Expected result

Invalid. A document with a form element is a scripted content document, so its manifest item must have the scripted property.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i property-scripted-form-missing.epub -u --advisory` | ERROR OPF-014; INVALID | `property-scripted-form-missing.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck property-scripted-form-missing.epub -u` | ERROR OPF-014; INVALID | `property-scripted-form-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets the same `form` as `form-element`. The manifest is not changed.

## History

- 2026-11-13: First version.
