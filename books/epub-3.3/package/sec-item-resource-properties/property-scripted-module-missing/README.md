# A module script without the scripted property

- Book: `property-scripted-module-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-resource-properties/property-scripted-module-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, to cover EPUB 3.3 scripting; parked on 2026-11-13 while both verifiers missed it, shipped after epubveri 0.42.0 reports it
- Issue: [#600](https://github.com/veripublica/epub-test-books/issues/600)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a script element with type="module", and its manifest item has no scripted property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A script with type="module" is a JavaScript module script, not a data block, so the document is a scripted content document and must have the scripted property.

## Question

`content.xhtml` has `<script type="module">` and no `scripted` property. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> EPUB creators MUST set the following properties whenever a resource referenced by an item element matches their respective definitions:

EPUB 3.3, [`scripted`](https://www.w3.org/TR/epub-33/#scripted):

> The scripted property indicates that the described publication resource is a scripted content document (i.e., contains scripting and/or [html] form elements).

HTML Living Standard, [`attr-script-type`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-type) (4.12.1 The script element):

> Setting the attribute to an ASCII case-insensitive match for "module" means that the script is a JavaScript module script, to be interpreted according to the JavaScript Module top-level production.
>
> Setting the attribute to any other value means that the script is a data block, which is not processed by the user agent, but instead by author script or other tools.

## Expected result

Invalid. A script with type="module" is a JavaScript module script, not a data block, so the document is a scripted content document and must have the scripted property.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i property-scripted-module-missing.epub -u --advisory` | ERROR OPF-014; INVALID | `property-scripted-module-missing.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck property-scripted-module-missing.epub -u` | no findings; VALID | `property-scripted-module-missing.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it gives no finding, as it treats the module script as a data block.

- **epubcheck: missed.** [w3c/epubcheck#1773](https://github.com/w3c/epubcheck/issues/1773).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<script type="module">let a = 1;</script>`, as in `module-script`. The manifest is not changed.

## History

- 2026-11-13: First version.
