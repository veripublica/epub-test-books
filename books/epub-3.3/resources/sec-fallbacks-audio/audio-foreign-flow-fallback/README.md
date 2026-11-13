# Foreign audio with only flow content as a fallback

- Book: `audio-foreign-flow-fallback.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-fallbacks-audio/audio-foreign-flow-fallback/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#134](https://github.com/veripublica/epub-test-books/issues/134)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An audio element plays a WAV file, a foreign resource, and its only fallback is a paragraph inside it. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Flow content does not count as a fallback for foreign audio.

## Question

An `audio` element plays a WAV file, which is a foreign resource, and its only fallback is a paragraph inside it. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-fallbacks-audio`](https://www.w3.org/TR/epub-33/#sec-fallbacks-audio):

> EPUB creators MUST NOT use embedded [html] flow content within a media element (i.e, audio or video) as an intrinsic fallback for audio foreign resources.

## Expected result

Invalid. Flow content does not count as a fallback for foreign audio.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i audio-foreign-flow-fallback.epub -u --advisory` | ERROR RSC-032; INVALID | `audio-foreign-flow-fallback.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck audio-foreign-flow-fallback.epub -u` | ERROR RSC-032; INVALID | `audio-foreign-flow-fallback.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated WAV is added to the manifest, and `content.xhtml` has an `audio` element with a paragraph inside it.

## History

- 2026-11-09: First version.
