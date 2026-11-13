# An event handler attribute without the scripted property

- Book: `property-scripted-event-handler-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-resource-properties/property-scripted-event-handler-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: [#541](https://github.com/veripublica/epub-test-books/issues/541)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a p element with an onclick attribute, no script element, and its manifest item has no scripted property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. An event handler content attribute holds JavaScript, so the document contains scripting and must have the scripted property.

## Question

`content.xhtml` has an `onclick` attribute, no `script` element, and no `scripted` property. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> EPUB creators MUST set the following properties whenever a resource referenced by an item element matches their respective definitions:

EPUB 3.3, [`scripted`](https://www.w3.org/TR/epub-33/#scripted):

> The scripted property indicates that the described publication resource is a scripted content document (i.e., contains scripting and/or [html] form elements).

HTML Living Standard, [`event-handler-content-attributes`](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-content-attributes) (8.1.8.1 Event handlers):

> Event handler content attributes, when specified, must contain valid JavaScript code which, when parsed, would match the FunctionBody production after automatic semicolon insertion.

## Expected result

Invalid. An event handler content attribute holds JavaScript, so the document contains scripting and must have the scripted property.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i property-scripted-event-handler-missing.epub -u --advisory` | ERROR OPF-014; INVALID | `property-scripted-event-handler-missing.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck property-scripted-event-handler-missing.epub -u` | ERROR OPF-014; INVALID | `property-scripted-event-handler-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<p onclick="this.hidden = true">Content.</p>`. The manifest is not changed.

## History

- 2026-11-13: First version.
