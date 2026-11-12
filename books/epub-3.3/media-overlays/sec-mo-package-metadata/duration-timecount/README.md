# `media:duration` as a timecount, `3s` (valid)

- Book: `duration-timecount.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-mo-package-metadata/duration-timecount/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: Both durations are 3s.

Expected result: Valid. 3s is a timecount clock value.

## Question

Both durations are `3s`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-duration`](https://www.w3.org/TR/epub-33/#sec-duration):

> Allowed value(s): MUST be a [smil3] clock value.

SMIL 3.0 Timing and Synchronization, [`Timing-ClockValueSyntax`](https://www.w3.org/TR/SMIL3/smil-timing.html#Timing-ClockValueSyntax) (Clock values; W3C Recommendation, 1 December 2008):

> `Clock-value ::= ( Full-clock-value | Partial-clock-value | Timecount-value ) Full-clock-value ::= Hours ":" Minutes ":" Seconds ("." Fraction )? Partial-clock-value ::= Minutes ":" Seconds ("." Fraction )? Timecount-value ::= Timecount ("." Fraction )? ( Metric )? Metric ::= "h" | "min" | "s" | "ms" Hours ::= DIGIT + /* any positive number */ Minutes ::= 2DIGIT /* range from 00 to 59 */ Seconds ::= 2DIGIT /* range from 00 to 59 */ Fraction ::= DIGIT + Timecount ::= DIGIT + 2DIGIT ::= DIGIT DIGIT DIGIT ::= [0-9]`

> For Timecount values, the default metric suffix is "s" (for seconds).

## Expected result

Valid. `3s` is a timecount clock value.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i duration-timecount.epub -u --advisory` | no findings; VALID | `duration-timecount.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck duration-timecount.epub -u` | no findings; VALID | `duration-timecount.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: Both durations are `3s`.

## History

- 2026-11-12: First version.
