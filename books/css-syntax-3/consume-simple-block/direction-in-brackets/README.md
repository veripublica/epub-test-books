# `direction: rtl;` inside square brackets (valid)

- Book: `direction-in-brackets.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-simple-block/direction-in-brackets/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: styloria, after its review of the encoding sets
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { color: [direction: rtl;]; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. A [ starts a simple block that runs to its ]; the ; inside it ends nothing. So direction: rtl; is part of the color value, not a declaration, and the sheet has no direction property.

## Question

`style.css` holds `p { color: [direction: rtl;]; }`. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`consume-simple-block`](https://www.w3.org/TR/css-syntax-3/#consume-simple-block) (5.5.9 Consume a simple block; Candidate Recommendation Draft, 1 October 2026):

> <eof-token>
>
> ending token
>
> Discard a token from input. Return block.
>
> anything else
>
> Consume a component value from input and append the result to block’s value.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. A `[` starts a simple block that runs to its `]`; the `;` inside it ends nothing. So `direction: rtl;` is part of the `color` value, not a declaration, and the sheet has no `direction` property.

CSS result: One rule with one declaration, `color`, whose value is the block `[direction: rtl;]`. That does not match the grammar of `color`, so the declaration is dropped: re-read as a rule, it reaches its `;`, which is a parse error.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i direction-in-brackets.epub -u --advisory` | USAGE ADV-024; VALID | `direction-in-brackets.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-brackets.epub -u` | ERROR CSS-008; INVALID | `direction-in-brackets.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the block as an error (CSS-008).

- **epubcheck: wrong error.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output, except USAGE ADV-024, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { color: [direction: rtl;]; }`, in UTF-8.

## History

- 2026-11-12: First version.
