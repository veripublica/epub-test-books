# A structural pseudo-class after `::part()`, `x-a::part(a):first-child` (valid)

- Book: `part-first-child.epub`, built from the EPUB 3 template
- Built by: `scripts/css-pseudo-4/element-like/part-first-child/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, for its 0.21 release (note 2026-11-18)
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds x-a::part(a):first-child { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `x-a::part(a):first-child { margin: 0; }`. Does a validator accept the book?

## Clause

CSS Pseudo-Elements Module Level 4, [`element-like`](https://www.w3.org/TR/css-pseudo-4/#element-like) (5. Element-backed Pseudo-elements; Working Draft, 27 June 2025):

> All pseudo-classes and pseudo-elements are syntactically allowed after an element-backed pseudo-element (such as x-button::part(label):hover or x-button::part(label)::before), just as if the pseudo-element were a type selector; but some are disallowed from matching:

> The structural pseudo-classes, :has() pseudo-class, :scope pseudo-class, and :host / :host() / :host-context() pseudo-classes never match.

Selectors Level 4, [`pseudo-element-states`](https://www.w3.org/TR/selectors-4/#pseudo-element-states) (3.6.3. Pseudo-classing Pseudo-elements; Working Draft, 22 January 2026):

> This specification allows any pseudo-element to be followed by any combination of the logical combination pseudo-classes and the user action pseudo-classes. Other specifications may allow additional pseudo-classes to be attached to particular pseudo-elements. Combinations that are not explicitly allowed are invalid selectors.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule, kept, that never matches. Any pseudo-class is allowed after an element-backed pseudo-element such as `::part()`, so the selector is valid, but a structural pseudo-class there never matches.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.47.0 | `epubveri -i part-first-child.epub -u --advisory` | no findings; VALID | `part-first-child.epubveri-0.47.0.txt` |
| epubcheck 5.4.0 | `epubcheck part-first-child.epub -u` | no findings; VALID | `part-first-child.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `x-a::part(a):first-child { margin: 0; }`, in UTF-8.

## History

- 2026-11-18: First version.
