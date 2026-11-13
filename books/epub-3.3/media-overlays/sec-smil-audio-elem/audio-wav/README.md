# A media overlay `audio` that is a WAV file

- Book: `audio-wav.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-smil-audio-elem/audio-wav/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: audio.mp3 is replaced by audio.wav (audio/wav, a tenth of a second of silence), and content.smil points to it.

Expected result: Invalid. WAV is not one of the core media type audio formats.

## Question

`audio.mp3` is replaced by `audio.wav` (`audio/wav`, a tenth of a second of silence), and `content.smil` points to it. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-smil-audio-elem`](https://www.w3.org/TR/epub-33/#sec-smil-audio-elem):

> The audio file MUST be one of the audio formats listed in the core media type resources table.

## Expected result

Invalid. WAV is not one of the core media type audio formats.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i audio-wav.epub -u --advisory` | ERROR MED-005; INVALID | `audio-wav.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck audio-wav.epub -u` | ERROR MED-005; INVALID | `audio-wav.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: `audio.mp3` is replaced by `audio.wav` (`audio/wav`, a tenth of a second of silence), and `content.smil` points to it.

## History

- 2026-11-12: First version.
