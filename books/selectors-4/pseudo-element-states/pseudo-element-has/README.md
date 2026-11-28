# `:has()` after a pseudo-element, `p::before:has(a)` (valid)

- Book: `pseudo-element-has.epub`, built from the EPUB 3 template
- Built by: `scripts/selectors-4/pseudo-element-states/pseudo-element-has/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, for its 0.21 release (note 2026-11-18)
- Issue: [#661](https://github.com/veripublica/epub-test-books/issues/661)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p::before:has(a) { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `p::before:has(a) { margin: 0; }`. Does a validator accept the book?

## Clause

Selectors Level 4, [`pseudo-element-states`](https://www.w3.org/TR/selectors-4/#pseudo-element-states) (3.6.3. Pseudo-classing Pseudo-elements; Working Draft, 22 January 2026):

> This specification allows any pseudo-element to be followed by any combination of the logical combination pseudo-classes and the user action pseudo-classes. Other specifications may allow additional pseudo-classes to be attached to particular pseudo-elements. Combinations that are not explicitly allowed are invalid selectors.

Selectors Level 4, [`logical-combination`](https://www.w3.org/TR/selectors-4/#logical-combination) (4. Logical Combinations; Working Draft, 22 January 2026):

> Selector logic can be manipulated by compounding (logical AND), selector lists (logical OR), and the logical combination pseudo-classes :is(), :where(), and :not(). The logical combination pseudo-classes are allowed anywhere that any other pseudo-classes are allowed, but pass any restrictions to their arguments.

CSS Syntax Level 3, [`style-rules`](https://www.w3.org/TR/css-syntax-3/#style-rules) (8.1. Style rules; Candidate Recommendation Draft, 1 October 2026):

> The prelude of the qualified rule is parsed as a <selector-list>. If this returns failure, the entire style rule is invalid.

CSS Syntax Level 3, [`css-stylesheets`](https://www.w3.org/TR/css-syntax-3/#css-stylesheets) (8. CSS stylesheets; Candidate Recommendation Draft, 1 October 2026):

> If any style rule is invalid, or any at-rule is not recognized or is invalid according to its grammar or context, it’s a parse error. Discard that rule.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: No rule is kept. `:has()` is not one of the logical combination pseudo-classes (`:is()`, `:where()`, `:not()`) and not a user action pseudo-class, so the selector is invalid and the rule is dropped, which is a parse error.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.50.0 | `epubveri -i pseudo-element-has.epub -u --advisory` | USAGE ADV-017; VALID | `pseudo-element-has.epubveri-0.50.0.txt` |
| epubcheck 5.4.0 | `epubcheck pseudo-element-has.epub -u` | no findings; VALID | `pseudo-element-has.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output, except USAGE ADV-017, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p::before:has(a) { margin: 0; }`, in UTF-8.

## History

- 2026-11-18: First version.
