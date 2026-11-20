# A user action pseudo-class after `::first-line`, `p::first-line:active` (valid)

- Book: `first-line-active.epub`, built from the EPUB 3 template
- Built by: `scripts/selectors-4/pseudo-element-states/first-line-active/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, for its 0.21 release (note 2026-11-18)
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p::first-line:active { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `p::first-line:active { margin: 0; }`. Does a validator accept the book?

## Clause

Selectors Level 4, [`pseudo-element-states`](https://www.w3.org/TR/selectors-4/#pseudo-element-states) (3.6.3. Pseudo-classing Pseudo-elements; Working Draft, 22 January 2026):

> This specification allows any pseudo-element to be followed by any combination of the logical combination pseudo-classes and the user action pseudo-classes. Other specifications may allow additional pseudo-classes to be attached to particular pseudo-elements. Combinations that are not explicitly allowed are invalid selectors.

Selectors Level 4, [`useraction-pseudos`](https://www.w3.org/TR/selectors-4/#useraction-pseudos) (9. User Action Pseudo-classes; Working Draft, 22 January 2026):

> Selectors provides several user action pseudo-classes for the selection of an element the user is acting on. (In non-interactive user agents, these pseudo-classes are valid, but never match any element.)

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule, kept: the first line of every `p`, while it is active. `:active` is a user action pseudo-class, which is allowed after any pseudo-element.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.47.0 | `epubveri -i first-line-active.epub -u --advisory` | no findings; VALID | `first-line-active.epubveri-0.47.0.txt` |
| epubcheck 5.4.0 | `epubcheck first-line-active.epub -u` | no findings; VALID | `first-line-active.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p::first-line:active { margin: 0; }`, in UTF-8.

## History

- 2026-11-18: First version.
