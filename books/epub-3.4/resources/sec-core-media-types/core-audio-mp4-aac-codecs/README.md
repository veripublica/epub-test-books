# AAC audio in MP4, audio/mp4; codecs=aac (valid)

- Book: `core-audio-mp4-aac-codecs.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.4/resources/sec-core-media-types/core-audio-mp4-aac-codecs/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, from the EPUB 3.4 core media types (w3c/epub-specs#2979)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml plays sound.mp4, half a second of silent AAC LC audio in an MP4 container, in an audio element. Its manifest item is audio/mp4; codecs=aac and has no fallback. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. EPUB 3.4 adds audio/mp4; codecs=aac as a media type for AAC LC in MP4, a core media type.

## Question

`content.xhtml` plays AAC LC audio in an MP4 container, declared as `audio/mp4; codecs=aac`, with no fallback. Does a validator accept the book?

## Clause

EPUB 3.4, [`sec-core-media-types`](https://www.w3.org/TR/epub-34/#sec-core-media-types) (3.2 Core media types; Candidate Recommendation Draft, 25 November 2026):

> Publication resources that conform to the MIME media type [rfc2046] specifications defined in the following table MAY be included in EPUB publications without fallbacks when they are used in EPUB content documents and foreign content documents.

> | audio/mp4; codecs=aac, audio/mp4 | [mpeg4-audio], [mp4] | AAC LC audio using MP4 container | 3.0 |

## Expected result

Valid. EPUB 3.4 lists `audio/mp4; codecs=aac` next to `audio/mp4` as the media type of AAC LC in MP4, a core media type, so an `audio` element may play it without a fallback.

EPUB 3.3 lists only `audio/mp4` for this row.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i core-audio-mp4-aac-codecs.epub -u --advisory` | no findings; VALID | `core-audio-mp4-aac-codecs.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck core-audio-mp4-aac-codecs.epub -u` | no findings; VALID | `core-audio-mp4-aac-codecs.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<p><audio src="sound.mp4" controls="controls">No audio.</audio></p>` in `content.xhtml`, and `OEBPS/sound.mp4` (`audio/mp4; codecs=aac`) in the manifest. The audio is 0.5 s of mono silence at 48 kHz in AAC LC, kept as bytes in `scripts/lib/encodedmedia.py` with the command that made it.

## History

- 2026-11-28: First version.
