# A `direction` declaration with a value it does not take, `direction: sideways` (valid)

- Book: `direction-invalid-value.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/style-rules/direction-invalid-value/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, after w3c/epub-specs#3115 (held CSS cases)
- Issue: [#669](https://github.com/veripublica/epub-test-books/issues/669)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { direction: sideways; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. sideways is not a value of direction, so CSS ignores the declaration. The parsed style sheet therefore holds no direction property, and EPUB 3.3 forbids only a declared one (w3c/epub-specs#3115).

## Question

`style.css` holds `p { direction: sideways; }`. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`style-rules`](https://www.w3.org/TR/css-syntax-3/#style-rules) (8.1. Style rules; Candidate Recommendation Draft, 1 October 2026):

> Declarations for an unknown CSS property or whose value does not match the syntax defined by the property are invalid and must be ignored.
>
> The validity of the style rule’s contents have no effect on the validity of the style rule itself.

CSS Writing Modes Level 3, [`direction`](https://www.w3.org/TR/css-writing-modes-3/#direction) (2.1 Specifying Directionality: the direction property; Recommendation, 10 December 2019) gives its values as `ltr | rtl`.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. `sideways` is not a value of `direction`, so CSS ignores the declaration. The parsed style sheet holds no `direction` property, it holds no `unicode-bidi` either, and it is UTF-8, so EPUB 3.3 asks nothing more of it.

EPUB 3.3 does not say whether "include" means that the property is declared or only that its name is written in the style sheet, so this set waited for the Working Group. The question went to [w3c/epub-specs#3115](https://github.com/w3c/epub-specs/issues/3115). The [answer](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6880091067) there: "It means the property must be declared." For a checker, "if the parsed sheet produces an object that contains a property with the name 'direction', you should report an error." The issue was closed on 2026-11-19 with the requirement's text unchanged ("[the current spec text stands](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6896967498)"); only the note under it was rewritten, in [w3c/epub-specs#3118](https://github.com/w3c/epub-specs/pull/3118).

CSS result: One rule, `p`, kept with no declarations. `sideways` does not match `direction`'s grammar, `ltr | rtl`, so the declaration is invalid and ignored. The rule itself stays valid.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i direction-invalid-value.epub -u --advisory` | USAGE ADV-024; VALID | `direction-invalid-value.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-invalid-value.epub -u` | ERROR CSS-001; INVALID | `direction-invalid-value.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the dropped `direction` declaration as an error (CSS-001).

- **epubcheck: wrong error.** [w3c/epubcheck#1781](https://github.com/w3c/epubcheck/issues/1781).

Every epubveri finding here is in its default output, except USAGE ADV-024, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { direction: sideways; }`, in UTF-8.

## History

- 2026-11-20: First version.
