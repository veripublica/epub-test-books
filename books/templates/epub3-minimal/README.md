# Template: EPUB 3.3

The starting point for every EPUB 3 book in this library. It carries every
part EPUB 3.3 requires, meets its recommendations, and raises no finding in
either verifier. A set copies it and changes only what its question needs.

- Book: `epub3-minimal.epub`
- Built by: `scripts/templates/epub3-minimal/build.py`
- Specification: [EPUB 3.3](https://www.w3.org/TR/epub-33/), W3C
  Recommendation (version of 13 January 2026)
- Origin: built here

## About this book

This book is the EPUB 3.3 template of epub-test-books, a library of small
EPUB files that each show one rule or one defect.

It carries every part EPUB 3.3 requires and meets its recommendations, so a
correct validator reports nothing on it. Every other EPUB 3 book in the
library is built from it and changes only what its own question needs.

Expected result: no finding of any kind (no error, warning, info or usage
message).

The document after this one is the part a set changes. In the template it
holds only a placeholder paragraph.

## Expected result

No finding at any level, from a validator that follows the specification.
Each part below is there because a clause asks for it, or because the
library chose it and the specification allows it.

## Parts

Anchors are in `https://www.w3.org/TR/epub-33/#<anchor>`. Level: M = MUST or
REQUIRED, S = SHOULD or RECOMMENDED, O = optional, chosen by the library.

### Container

| Part | Level | Clause |
|------|-------|--------|
| `mimetype` is the first entry, stored, exactly `application/epub+zip` in US-ASCII, no padding, no byte order mark, no extra field | M | `sec-zip-container-mime` |
| Only stored and Deflate entries; no spanning, no ZIP encryption; UTF-8 file names; version-needed 10 or 20 | M | `sec-zip-container-zipreqs` |
| No ZIP64 | S | `sec-zip-container-zipreqs` |
| `META-INF/container.xml`, `version="1.0"`, one `rootfile` with `full-path="OEBPS/package.opf"` and `media-type="application/oebps-package+xml"` | M | `sec-container-file-and-dir-structure`, `sec-container-metainf-files` |
| `META-INF` files and `mimetype` are neither in the manifest nor referenced | M | `sec-container-file-and-dir-structure` |
| File names are short, ASCII, unique after case folding | M | `sec-container-filenames` |
| File names have no spaces | S | `sec-container-filenames` |

### Package document

| Part | Level | Clause |
|------|-------|--------|
| `package` root, `version="3.0"`, `unique-identifier="uid"` | M | `sec-package-elem` |
| `dc:identifier id="uid"`: a `urn:uuid:` (UUID v5 of the set's path, fixed) | M | `sec-opf-dcmes-required` |
| `dc:title`: `Test book` | M | `sec-opf-dcmes-required` |
| `dc:language`: `en` | M | `sec-opf-dcmes-required` |
| Exactly one `dcterms:modified`, `YYYY-MM-DDThh:mm:ssZ`, taken from the last History date below | M | `sec-metadata-last-modified` |
| `manifest` lists every resource except the package document, with core media types and unique `href`s | M | `sec-manifest-elem`, `sec-item-elem` |
| Exactly one item with `properties="nav"` | M | `sec-item-elem` |
| `spine` with two linear `itemref`s, each item once; both documents the navigation links to are in it | M | `sec-spine-elem`, `sec-itemref-elem` |

### Documents

| Part | Level | Clause |
|------|-------|--------|
| XML 1.0, no external entities, no XInclude | M | `sec-xml-constraints` |
| UTF-8 | S | `sec-xml-constraints` |
| XHTML content documents in the XML syntax of HTML | M | `sec-xhtml-req` |
| Navigation document: one `toc` nav, every link labelled and pointing to a spine document | M | `sec-nav-content-req`, `sec-nav-def-model` |
| `toc` entries in spine order | S | `sec-nav-toc` |
| Navigation document not in the spine | O | `sec-nav-doc-use-spine` |

### Accessibility

EPUB 3.3 says a publication SHOULD conform to
[EPUB Accessibility 1.1](https://www.w3.org/TR/epub-a11y-11/)
(`sec-epub-conf`).

| Part | Level | Clause |
|------|-------|--------|
| `schema:accessMode` `textual`; `schema:accessibilityFeature` `tableOfContents`, `readingOrder`, `structuralNavigation`; `schema:accessibilityHazard` `none` | S | A11y 1.1 `sec-disc-package` |
| `schema:accessModeSufficient` `textual`; `schema:accessibilitySummary` | S | A11y 1.1 `sec-disc-package` |
| `lang` and `xml:lang` on every document, a `title` in every document, a heading on every page | S | A11y 1.1 `sec-wcag-conf` |
| No conformance claim (`dcterms:conformsTo`, `a11y:certifiedBy`) | O | A11y 1.1 `sec-conf-reporting` |

### Chosen by the library

| Part | Level | Note |
|------|-------|------|
| `OEBPS/about.xhtml`, first in the spine: the "About this book" section above, so the book explains itself | O | the defect never goes in this document |
| `OEBPS/content.xhtml`: the document a set changes | O | |
| `dc:creator` and `dc:publisher` `veripublica`, `dc:rights` the credit line, `dc:source` the repository, `dc:date` the first History date, `dc:description`, `dc:subject` | O | `sec-opf-dcmes-optional` |
| `belongs-to-collection` `epub-test-books`, `collection-type` `set` | O | `sec-belongs-to-collection` |
| No NCX, cover, CSS, fonts or images | O | each is a set of its own when needed |
| Reproducible ZIP: fixed entry order, timestamps and attributes | O | the same sources give the same bytes |

A set that tests one of these parts removes or changes it on purpose, and
its README says so.

## Verifier results

Run with `scripts/check.py`. Each output file is named with the verifier's
exact version and never edited afterwards.

| Verifier | Command | Result |
|----------|---------|--------|
| epubveri 0.37.1 | `epubveri -i epub3-minimal.epub -u --advisory` | 0 findings, VALID (`epub3-minimal.epubveri-0.37.1.txt`) |
| epubcheck 5.4.0 | `epubcheck epub3-minimal.epub -u` | 0 fatals, errors, warnings, infos and usages (`epub3-minimal.epubcheck-5.4.0.txt`) |

Both agree with the expected result, so there is nothing to mark.

## History

- 2026-11-08: First version.
