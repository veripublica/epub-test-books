# A user action pseudo-class inside `:not()` after a pseudo-element, `p::before:not(:focus)` (valid)

- Book: `pseudo-element-not-focus.epub`, built from the EPUB 3 template
- Built by: `scripts/selectors-4/pseudo-element-states/pseudo-element-not-focus/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, for its 0.21 release (note 2026-11-18)
- Issue: [#665](https://github.com/veripublica/epub-test-books/issues/665)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p::before:not(:focus) { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `p::before:not(:focus) { margin: 0; }`. Does a validator accept the book?

## Clause

Selectors Level 4, [`pseudo-element-states`](https://www.w3.org/TR/selectors-4/#pseudo-element-states) (3.6.3. Pseudo-classing Pseudo-elements; Working Draft, 22 January 2026):

> This specification allows any pseudo-element to be followed by any combination of the logical combination pseudo-classes and the user action pseudo-classes. Other specifications may allow additional pseudo-classes to be attached to particular pseudo-elements. Combinations that are not explicitly allowed are invalid selectors.

Selectors Level 4, [`logical-combination`](https://www.w3.org/TR/selectors-4/#logical-combination) (4. Logical Combinations; Working Draft, 22 January 2026):

> Selector logic can be manipulated by compounding (logical AND), selector lists (logical OR), and the logical combination pseudo-classes :is(), :where(), and :not(). The logical combination pseudo-classes are allowed anywhere that any other pseudo-classes are allowed, but pass any restrictions to their arguments.

Selectors Level 4, [`useraction-pseudos`](https://www.w3.org/TR/selectors-4/#useraction-pseudos) (9. User Action Pseudo-classes; Working Draft, 22 January 2026):

> Selectors provides several user action pseudo-classes for the selection of an element the user is acting on. (In non-interactive user agents, these pseudo-classes are valid, but never match any element.)

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule, kept: the `::before` of every `p`, while it is not focused. `:not()` is allowed after a pseudo-element and passes the restriction to its argument, which `:focus`, a user action pseudo-class, meets.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.47.0 | `epubveri -i pseudo-element-not-focus.epub -u --advisory` | no findings; VALID | `pseudo-element-not-focus.epubveri-0.47.0.txt` |
| epubcheck 5.4.0 | `epubcheck pseudo-element-not-focus.epub -u` | no findings; VALID | `pseudo-element-not-focus.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p::before:not(:focus) { margin: 0; }`, in UTF-8.

## History

- 2026-11-18: First version.
