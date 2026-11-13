# A `media:duration` that is not a clock value

- Book: `duration-not-clock.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-mo-package-metadata/duration-not-clock/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the media overlays section
- Issue: [#473](https://github.com/veripublica/epub-test-books/issues/473)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: Both durations are 3 seconds.

Expected result: Invalid. 3 seconds matches none of the clock value forms.

## Question

Both durations are `3 seconds`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-duration`](https://www.w3.org/TR/epub-33/#sec-duration):

> Allowed value(s): MUST be a [smil3] clock value.

SMIL 3.0 Timing and Synchronization, [`Timing-ClockValueSyntax`](https://www.w3.org/TR/SMIL3/smil-timing.html#Timing-ClockValueSyntax) (Clock values; W3C Recommendation, 1 December 2008):

> `Clock-value ::= ( Full-clock-value | Partial-clock-value | Timecount-value ) Full-clock-value ::= Hours ":" Minutes ":" Seconds ("." Fraction )? Partial-clock-value ::= Minutes ":" Seconds ("." Fraction )? Timecount-value ::= Timecount ("." Fraction )? ( Metric )? Metric ::= "h" | "min" | "s" | "ms" Hours ::= DIGIT + /* any positive number */ Minutes ::= 2DIGIT /* range from 00 to 59 */ Seconds ::= 2DIGIT /* range from 00 to 59 */ Fraction ::= DIGIT + Timecount ::= DIGIT + 2DIGIT ::= DIGIT DIGIT DIGIT ::= [0-9]`

> For Timecount values, the default metric suffix is "s" (for seconds).

## Expected result

Invalid. `3 seconds` matches none of the clock value forms.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i duration-not-clock.epub -u --advisory` | ERROR RSC-005, ERROR RSC-005; INVALID | `duration-not-clock.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck duration-not-clock.epub -u` | ERROR RSC-005, ERROR RSC-005; INVALID | `duration-not-clock.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: Both durations are `3 seconds`.

## History

- 2026-11-12: First version.
