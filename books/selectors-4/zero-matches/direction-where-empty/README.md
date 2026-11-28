# `direction: rtl` in a rule whose `:where()` is left empty, `:where(:foo)`

- Book: `direction-where-empty.epub`, built from the EPUB 3 template
- Built by: `scripts/selectors-4/zero-matches/direction-where-empty/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, after w3c/epub-specs#3115 (held CSS cases)
- Issue: [#677](https://github.com/veripublica/epub-test-books/issues/677)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds :where(:foo) { direction: rtl; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. :where() takes a forgiving list, so :foo is left out and the selector :where() is valid but matches nothing. CSS keeps the rule, with its direction declaration. The parsed style sheet therefore holds a direction property, which EPUB 3.3 forbids (w3c/epub-specs#3115).

## Question

`style.css` holds `:where(:foo) { direction: rtl; }`. Does a validator reject the book?

## Clause

Selectors Level 4, [`zero-matches`](https://www.w3.org/TR/selectors-4/#zero-matches) (4.4. The Specificity-adjustment Pseudo-class: :where(); Working Draft, 22 January 2026):

> The Specificity-adjustment pseudo-class, :where(), is a functional pseudo-class with the same syntax and functionality as :is().

Selectors Level 4, [`matches`](https://www.w3.org/TR/selectors-4/#matches) (4.2. The Matches-Any Pseudo-class: :is(); Working Draft, 22 January 2026):

> The matches-any pseudo-class, :is(), is a functional pseudo-class taking a <forgiving-selector-list> as its sole argument. If the argument, after parsing, is an empty list, the pseudo-class is valid but matches nothing.

Selectors Level 4, [`forgiving-selector`](https://www.w3.org/TR/selectors-4/#forgiving-selector) (16.1. <forgiving-selector-list> and <forgiving-relative-selector-list>; Working Draft, 22 January 2026):

> The <forgiving-selector-list> production instead parses each selector in the list individually, simply ignoring ones that fail to parse, so the remaining selectors can still be used.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> It MUST NOT include the direction property [css-writing-modes-3].

## Expected result

Invalid. `:where()` takes a forgiving list, so `:foo` is left out and the selector `:where()` is valid but matches nothing. CSS keeps the rule, with its `direction` declaration. The parsed style sheet holds a `direction` property, which EPUB 3.3 forbids.

EPUB 3.3 does not say whether "include" means that the property is declared or only that its name is written in the style sheet, so this set waited for the Working Group. The question went to [w3c/epub-specs#3115](https://github.com/w3c/epub-specs/issues/3115). The [answer](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6880091067) there: "It means the property must be declared." For a checker, "if the parsed sheet produces an object that contains a property with the name 'direction', you should report an error." The issue was closed on 2026-11-19 with the requirement's text unchanged ("[the current spec text stands](https://github.com/w3c/epub-specs/issues/3115#issuecomment-6896967498)"); only the note under it was rewritten, in [w3c/epub-specs#3118](https://github.com/w3c/epub-specs/pull/3118). That the rule matches nothing does not matter: the declaration is in the parsed sheet.

CSS result: One rule, kept, with one declaration, `direction: rtl`. Its selector `:where()` is empty after `:foo` is left out, so it matches nothing.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.50.0 | `epubveri -i direction-where-empty.epub -u --advisory` | ERROR CSS-001; INVALID | `direction-where-empty.epubveri-0.50.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-where-empty.epub -u` | ERROR CSS-001; INVALID | `direction-where-empty.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `:where(:foo) { direction: rtl; }`, in UTF-8.

## History

- 2026-11-20: First version.
