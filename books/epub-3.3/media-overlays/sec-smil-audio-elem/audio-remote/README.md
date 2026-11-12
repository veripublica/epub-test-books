# A media overlay `audio` on the web (valid)

- Book: `audio-remote.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-smil-audio-elem/audio-remote/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: content.smil's audio has src="https://example.com/a.mp3"; the book has no audio file, the manifest lists the remote MP3, and the overlay's item has properties="remote-resources".

Expected result: Valid. Audio may be stored outside the container.

## Question

`content.smil`'s `audio` has `src="https://example.com/a.mp3"`; the book has no audio file, the manifest lists the remote MP3, and the overlay's item has `properties="remote-resources"`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-smil-audio-elem`](https://www.w3.org/TR/epub-33/#sec-smil-audio-elem):

> The audio file MUST be one of the audio formats listed in the core media type resources table.

EPUB 3.3, [`sec-resource-locations`](https://www.w3.org/TR/epub-33/#sec-resource-locations):

> EPUB creators MAY host the following types of publication resources outside the EPUB container: Audio resources.

## Expected result

Valid. Audio may be stored outside the container.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i audio-remote.epub -u --advisory` | no findings; VALID | `audio-remote.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck audio-remote.epub -u` | no findings; VALID | `audio-remote.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: `content.smil`'s `audio` has `src="https://example.com/a.mp3"`; the book has no audio file, the manifest lists the remote MP3, and the overlay's item has `properties="remote-resources"`.

## History

- 2026-11-12: First version.
