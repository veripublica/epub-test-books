# A scripted document in an iframe, without the scripted property

- Book: `property-scripted-iframe-child-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-resource-properties/property-scripted-iframe-child-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: [#545](https://github.com/veripublica/epub-test-books/issues/545)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an iframe of OEBPS/framed.xhtml, which has a script element. Neither has the scripted property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. framed.xhtml contains scripting, so its own manifest item must have the scripted property.

## Question

`content.xhtml` frames `framed.xhtml`, which has a script, and neither has the `scripted` property. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> EPUB creators MUST set the following properties whenever a resource referenced by an item element matches their respective definitions:

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> These properties do not apply recursively to content included into a resource (e.g., via the [html] iframe element). For example, if a non-scripted XHTML content document embeds a scripted content document, only the embedded document's manifest item properties attribute will have the scripted value.

## Expected result

Invalid. framed.xhtml contains scripting, so its own manifest item must have the scripted property.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i property-scripted-iframe-child-missing.epub -u --advisory` | ERROR OPF-014; INVALID | `property-scripted-iframe-child-missing.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck property-scripted-iframe-child-missing.epub -u` | ERROR OPF-014; INVALID | `property-scripted-iframe-child-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The same as `property-scripted-iframe-child`, without `properties="scripted"` on `framed.xhtml`.

## History

- 2026-11-13: First version.
