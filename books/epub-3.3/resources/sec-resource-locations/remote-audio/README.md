# Audio outside the container (valid)

- Book: `remote-audio.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-resource-locations/remote-audio/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#137](https://github.com/veripublica/epub-test-books/issues/137)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An audio element plays an MP3 at a web address, listed in the manifest. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Audio may be outside the container.

## Question

An `audio` element plays an MP3 at an `https` URL, listed in the manifest, and the content item has `remote-resources`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-resource-locations`](https://www.w3.org/TR/epub-33/#sec-resource-locations):

> EPUB creators MAY host the following types of publication resources outside the EPUB container: Audio resources.

## Expected result

Valid. Audio may be outside the container.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i remote-audio.epub -u --advisory` | no findings; VALID | `remote-audio.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck remote-audio.epub -u` | no findings; VALID | `remote-audio.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, an `audio` element has an `https` source. In `OEBPS/package.opf`, that URL is a manifest item and the content item has the `remote-resources` property.

## History

- 2026-11-09: First version.
