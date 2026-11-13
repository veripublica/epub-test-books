# A module script, with the scripted property (valid)

- Book: `module-script.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-scripted-content/module-script/build.py`
- Origin: built here
- Expected: valid
- Marks: epubveri: wrong error; epubcheck: wrong error
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: [#534](https://github.com/veripublica/epub-test-books/issues/534)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a script element with type="module", and its manifest item has the scripted property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. A script with type="module" is a JavaScript module script, not a data block. So the document is a scripted content document, and the scripted property is right.

## Question

`content.xhtml` has `<script type="module">` and the `scripted` property. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-scripted-content`](https://www.w3.org/TR/epub-33/#sec-scripted-content):

> When an EPUB content document contains scripting, this specification refers to it as a scripted content document. This label also applies to XHTML content documents that contain [html] form elements.
>
> The scripted property of the manifest item element is used to indicate that an EPUB content document is a scripted content document.
>
> When an [html] script element contains a data block [html], it does not represent scripted content.

HTML Living Standard, [`attr-script-type`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-type) (4.12.1 The script element):

> Setting the attribute to an ASCII case-insensitive match for "module" means that the script is a JavaScript module script, to be interpreted according to the JavaScript Module top-level production.
>
> Setting the attribute to any other value means that the script is a data block, which is not processed by the user agent, but instead by author script or other tools.

## Expected result

Valid. A script with type="module" is a JavaScript module script, not a data block. So the document is a scripted content document, and the scripted property is right.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i module-script.epub -u --advisory` | ERROR OPF-015; INVALID | `module-script.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck module-script.epub -u` | ERROR OPF-015; INVALID | `module-script.epubcheck-5.4.0.txt` |

Neither agrees with the expected result. epubveri reports the scripted property as not needed (OPF-015). epubcheck reports the scripted property as not needed (OPF-015).

- **epubveri: wrong error.** epubveri issue pending.
- **epubcheck: wrong error.** [w3c/epubcheck#1773](https://github.com/w3c/epubcheck/issues/1773).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<script type="module">let a = 1;</script>`, and its manifest item `properties="scripted"`.

## History

- 2026-11-13: First version.
