# A script file, with the scripted property (valid)

- Book: `external-script.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-scripted-content/external-script/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml loads OEBPS/script.js with a script element in its head. The script is in the manifest as application/javascript, and content.xhtml has the scripted property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Scripts are a core media type, and the document that loads one is a scripted content document marked as such.

## Question

`content.xhtml` loads `script.js` (`application/javascript`) and has the `scripted` property. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-scripted-content`](https://www.w3.org/TR/epub-33/#sec-scripted-content):

> When an EPUB content document contains scripting, this specification refers to it as a scripted content document. This label also applies to XHTML content documents that contain [html] form elements.
>
> The scripted property of the manifest item element is used to indicate that an EPUB content document is a scripted content document.

## Expected result

Valid. Scripts are a core media type, and the document that loads one is a scripted content document marked as such.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i external-script.epub -u --advisory` | no findings; VALID | `external-script.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck external-script.epub -u` | no findings; VALID | `external-script.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<script src="script.js"></script>` in its head and `properties="scripted"`. `OEBPS/script.js` is one line of JavaScript, in the manifest as `application/javascript`.

## History

- 2026-11-13: First version.
