# An epub:trigger whose ref names no element

- Book: `trigger-ref-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-epub-trigger/trigger-ref-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#583](https://github.com/veripublica/epub-test-books/issues/583)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an epub:trigger with ref="nowhere", and no element has that id. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. ref is an IDREF, so it must name an element in the document.

## Question

`content.xhtml` has an `epub:trigger` with `ref="nowhere"`, an id no element has. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-epub-trigger`](https://www.w3.org/TR/epub-33/#sec-xhtml-epub-trigger):

> Use of the element is deprecated. Refer to the epub:trigger element definition in [epubcontentdocs-301] for more information.

EPUB Content Documents 3.0.1, [2.1.3.4 The epub:trigger Element](https://idpf.org/epub/301/spec/epub-contentdocs.html) (Recommended Specification, 26 June 2014):

> ref [required] An IDREF [XML] that identifies the element that is the object of the action.

## Expected result

Invalid. ref is an IDREF, so it must name an element in the document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i trigger-ref-missing.epub -u --advisory` | ERROR RSC-005, WARNING RSC-017; INVALID | `trigger-ref-missing.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck trigger-ref-missing.epub -u` | WARNING RSC-017, ERROR RSC-005; INVALID | `trigger-ref-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

WARNING RSC-017 does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets an `audio` element (`id="a1"`, `OEBPS/sound.mp3`, three seconds of silence, `audio/mpeg`) and a `p` with `id="b1"`, and in the head `<epub:trigger action="show" ref="nowhere" ev:observer="b1" ev:event="click"/>`. The accessibility metadata says the book has audio.

## History

- 2026-11-13: First version.
