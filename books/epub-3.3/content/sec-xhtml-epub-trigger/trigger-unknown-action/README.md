# An epub:trigger with an action EPUB 3.0.1 does not define

- Book: `trigger-unknown-action.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-epub-trigger/trigger-unknown-action/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#584](https://github.com/veripublica/epub-test-books/issues/584)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an epub:trigger with action="explode". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. action takes one of seven values, and explode is not one of them.

## Question

`content.xhtml` has an `epub:trigger` with `action="explode"`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-epub-trigger`](https://www.w3.org/TR/epub-33/#sec-xhtml-epub-trigger):

> Use of the element is deprecated. Refer to the epub:trigger element definition in [epubcontentdocs-301] for more information.

EPUB Content Documents 3.0.1, [2.1.3.4 The epub:trigger Element](https://idpf.org/epub/301/spec/epub-contentdocs.html) (Recommended Specification, 26 June 2014):

> action [required] The action to perform for this event. Allowed values: show | hide | play | pause | resume | mute | unmute

## Expected result

Invalid. action takes one of seven values, and explode is not one of them.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i trigger-unknown-action.epub -u --advisory` | ERROR RSC-005, WARNING RSC-017; INVALID | `trigger-unknown-action.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck trigger-unknown-action.epub -u` | ERROR RSC-005, WARNING RSC-017; INVALID | `trigger-unknown-action.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

WARNING RSC-017 does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets an `audio` element (`id="a1"`, `OEBPS/sound.mp3`, three seconds of silence, `audio/mpeg`) and a `p` with `id="b1"`, and in the head `<epub:trigger action="explode" ref="b1" ev:observer="b1" ev:event="click"/>`. The accessibility metadata says the book has audio.

## History

- 2026-11-13: First version.
