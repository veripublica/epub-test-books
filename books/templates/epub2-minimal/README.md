# Template: EPUB 2.0.1

The starting point for every EPUB 2 book in this library. It carries every
part EPUB 2.0.1 requires, meets its recommendations, and raises no finding in
either verifier. A set copies it and changes only what its question needs.

- Book: `epub2-minimal.epub`
- Built by: `scripts/templates/epub2-minimal/build.py`
- Specification: EPUB 2.0.1, made of
  [OPF 2.0.1](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm),
  [OPS 2.0.1](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm) and
  [OCF 2.0.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc)
- Origin: built here
- Expected: valid, no finding at any level
- Marks: none

## About this book

This book is the EPUB 2.0.1 template of epub-test-books, a library of small
EPUB files that each show one rule or one defect.

It carries every part EPUB 2.0.1 requires and meets its recommendations, so
a correct validator reports nothing on it. Every other EPUB 2 book in the
library is built from it and changes only what its own question needs.

Expected result: no finding of any kind (no error, warning, info or usage
message).

The document after this one is the part a set changes. In the template it
holds only a placeholder paragraph.

## Expected result

No finding at any level, from a validator that follows the specification.

## Parts

OPF and OPS anchors are `#SectionN` in their HTML editions. OCF 2.0.1 is a
Word document, cited by section number. Level: M = must or required,
S = should or recommended, O = optional, chosen by the library.

| Part | Level | Clause |
|------|-------|--------|
| `mimetype` is the first entry, uncompressed, unencrypted, ASCII `application/epub+zip` | M | OCF §3.4, §4 |
| Only stored and Deflate entries, no spanning | M | OCF §4 |
| No ZIP64 | S | OCF §4 |
| `META-INF/container.xml`, `version="1.0"`, a `rootfile` of `application/oebps-package+xml` | M | OCF §3.5, §3.5.1 |
| Only one such `rootfile` | S | OCF §3.5.1 |
| Package document named `*.opf` | S | OPF `Section2.0` |
| `package` `version="2.0"`, `unique-identifier="uid"` | M | OPF `Section2.1` |
| `dc:identifier id="uid"`: a `urn:uuid:` (UUID v5 of the set's path, fixed); `dc:title` `Test book`; `dc:language` `en` | M | OPF `Section2.2`, `Section2.2.1`, `Section2.2.12` |
| No deprecated `dc-metadata` or `x-metadata` | S | OPF `Section2.2` |
| Manifest lists every file except the package document, each with `id`, `href` and `media-type`, no fragment, no duplicate | M | OPF `Section2.3` |
| Spine: two linear `itemref`s, each item once, `toc="ncx"` | M | OPF `Section2.4` |
| NCX: manifest item of `application/x-dtbncx+xml` without fallback; valid to `ncx-2005-1.dtd`; `version` and `xmlns` written out; `dtb:uid` equal to the identifier; a `navMap`; with the DOCTYPE, `playOrder` on every `navPoint` | M | OPF `Section2.4.1.2` |
| XHTML content documents: well-formed XML 1.0, UTF-8, valid XHTML 1.1, with the XHTML 1.1 DOCTYPE | M | OPS `Section1.4.1.2`, `Section2.1` |
| Preferred vocabulary only | S | OPS `Section2.1` |
| The XHTML 1.1 and NCX DTDs are not in the manifest | M | OPF `Section2.3` (see the note below) |

### Chosen by the library

| Part | Level | Note |
|------|-------|------|
| `OEBPS/about.xhtml`, first in the spine: the "About this book" section above | O | the defect never goes in this document |
| `OEBPS/content.xhtml`: the document a set changes | O | |
| `dc:creator` and `dc:publisher` `veripublica`, `dc:rights` the credit line, `dc:source` the repository, `dc:description`, `dc:subject` | O | OPF `Section2.2` |
| `dc:date opf:event="publication"`: the first History date; `dc:date opf:event="modification"`: the last one. OPF 2.0.1 has no `dcterms:modified` | O | OPF `Section2.2.7` |
| Accessibility metadata as `<meta name="schema:…" content="…"/>`: the same values as the EPUB 3 template | O | A11y 1.1 `sec-application` |
| No collection: OPF 2.0.1 has no collection element, and a `meta` name would mean nothing to a reading system | O | |
| No `guide`, cover, CSS, fonts or images | O | |
| Reproducible ZIP: fixed entry order, timestamps and attributes | O | |

### Note on OPF `Section2.3`

The section says the DTDs of "certain core document types do not need to be
included", then introduces the list with "The list of DTDs that do need to
be included in the manifest is", followed by the XHTML 1.1, SVG 1.1, DTBook
and NCX DTDs. The template reads the list as the exceptions, as the sentence
before it says, and as both verifiers do: the DTDs are not in the manifest.

## Verifier results

Run with `scripts/check.py`. Each output file is named with the verifier's
exact version and never edited afterwards.

| Verifier | Command | Result |
|----------|---------|--------|
| epubveri 0.40.1 | `epubveri -i epub2-minimal.epub -u --advisory` | 0 findings, VALID (`epub2-minimal.epubveri-0.40.1.txt`) |
| epubcheck 5.4.0 | `epubcheck epub2-minimal.epub -u` | 0 fatals, errors, warnings, infos and usages (`epub2-minimal.epubcheck-5.4.0.txt`) |

Both agree with the expected result, so there is nothing to mark.

## History

- 2026-11-08: First version.
