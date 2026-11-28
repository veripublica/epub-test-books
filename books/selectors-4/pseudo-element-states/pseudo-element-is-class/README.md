# A class selector inside `:is()` after a pseudo-element, `p::before:is(.x)` (valid)

- Book: `pseudo-element-is-class.epub`, built from the EPUB 3 template
- Built by: `scripts/selectors-4/pseudo-element-states/pseudo-element-is-class/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, for its 0.21 release (note 2026-11-18)
- Issue: [#663](https://github.com/veripublica/epub-test-books/issues/663)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p::before:is(.x) { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `p::before:is(.x) { margin: 0; }`. Does a validator accept the book?

## Clause

Selectors Level 4, [`pseudo-element-states`](https://www.w3.org/TR/selectors-4/#pseudo-element-states) (3.6.3. Pseudo-classing Pseudo-elements; Working Draft, 22 January 2026):

> This specification allows any pseudo-element to be followed by any combination of the logical combination pseudo-classes and the user action pseudo-classes. Other specifications may allow additional pseudo-classes to be attached to particular pseudo-elements. Combinations that are not explicitly allowed are invalid selectors.

Selectors Level 4, [`logical-combination`](https://www.w3.org/TR/selectors-4/#logical-combination) (4. Logical Combinations; Working Draft, 22 January 2026):

> Selector logic can be manipulated by compounding (logical AND), selector lists (logical OR), and the logical combination pseudo-classes :is(), :where(), and :not(). The logical combination pseudo-classes are allowed anywhere that any other pseudo-classes are allowed, but pass any restrictions to their arguments.

Selectors Level 4, [`matches`](https://www.w3.org/TR/selectors-4/#matches) (4.2. The Matches-Any Pseudo-class: :is(); Working Draft, 22 January 2026):

> The matches-any pseudo-class, :is(), is a functional pseudo-class taking a <forgiving-selector-list> as its sole argument. If the argument, after parsing, is an empty list, the pseudo-class is valid but matches nothing.

Selectors Level 4, [`forgiving-selector`](https://www.w3.org/TR/selectors-4/#forgiving-selector) (16.1. <forgiving-selector-list> and <forgiving-relative-selector-list>; Working Draft, 22 January 2026):

> The <forgiving-selector-list> production instead parses each selector in the list individually, simply ignoring ones that fail to parse, so the remaining selectors can still be used.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule, kept, that matches nothing. `:is()` is allowed after `::before` and passes the restriction to its argument, so `.x` is invalid there. `:is()` takes a forgiving list, so `.x` is left out, and an `:is()` with an empty list is valid but matches nothing.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i pseudo-element-is-class.epub -u --advisory` | no findings; VALID | `pseudo-element-is-class.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck pseudo-element-is-class.epub -u` | no findings; VALID | `pseudo-element-is-class.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p::before:is(.x) { margin: 0; }`, in UTF-8.

## History

- 2026-11-18: First version.
