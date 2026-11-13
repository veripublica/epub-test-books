# An epub:trigger in the body (valid)

- Book: `trigger-in-body.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-epub-trigger/trigger-in-body/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#582](https://github.com/veripublica/epub-test-books/issues/582)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an audio element, a p with id b1, and after them in the body an epub:trigger that shows b1 when it is clicked. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The trigger may also be in flow content. Deprecated, so a warning would fit.

## Question

`content.xhtml` has an `epub:trigger` in its body. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-xhtml-epub-trigger`](https://www.w3.org/TR/epub-33/#sec-xhtml-epub-trigger):

> Use of the element is deprecated. Refer to the epub:trigger element definition in [epubcontentdocs-301] for more information.

EPUB Content Documents 3.0.1, [2.1.3.4 The epub:trigger Element](https://idpf.org/epub/301/spec/epub-contentdocs.html) (Recommended Specification, 26 June 2014):

> Usage As a child of head and in Flow content. Repeatable.

## Expected result

Valid. The trigger may also be in flow content. Deprecated, so a warning would fit.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i trigger-in-body.epub -u --advisory` | WARNING RSC-017; VALID | `trigger-in-body.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck trigger-in-body.epub -u` | WARNING RSC-017; VALID | `trigger-in-body.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

WARNING RSC-017 does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets an `audio` element (`id="a1"`, `OEBPS/sound.mp3`, three seconds of silence, `audio/mpeg`) and a `p` with `id="b1"`, and after them in the body `<epub:trigger action="show" ref="b1" ev:observer="b1" ev:event="click"/>`. The accessibility metadata says the book has audio.

## History

- 2026-11-13: First version.
