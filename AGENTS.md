# epub-test-books: detail for code agents and maintainers

`README.md` is the short introduction. This file holds the detail, and is
kept true at every release. The rules for adding a set are in
`CONTRIBUTING.md`; this file points to them rather than repeating them.

## Status

Latest release: v0.2.0 (2026-11-08). It holds the two templates and 22
sets on the EPUB container (OCF), under `books/epub-3.3/ocf/<anchor>/<set>/`:
damaged ZIP files, the mimetype file, ZIP compression and file names,
`container.xml` and `rootfile`, and URLs in the container. `books/INDEX.md`
lists every book on one page, and `books/index.json` holds the same list for
programs.

## Scope

A library of small EPUBs for testing EPUB tools, one question per book: mostly
the tools that check or change books (validators, converters, fixers), and
reading apps where a book's behaviour matters. Each book shows one thing,
either a rule from the EPUB or CSS specifications or a defect pattern seen in
real books, and nothing else, so a tool's result on it can be read without
guessing. Many books are broken on purpose.

W3C's [EPUB tests](https://w3c.github.io/epub-tests/) cover reading systems,
judged by a person reading each book. This library is about tools, and
records what two validators say about each book.

Rules every book follows:

- **One question per book,** built from a template that raises no finding
  (CONTRIBUTING §2).
- **The specification decides.** The expected result is written in the set's
  issue, from the quoted clause, before any tool runs (CONTRIBUTING §1).
- **Two verifiers, exact versions.** epubveri and epubcheck run on every
  book; each output is kept under its version; every difference from the
  expected result is marked intended, spec unclear (followed epubcheck), or
  missed (CONTRIBUTING §4).
- **No commercial content.** Books are built from scratch, or reduced from a
  real book (CONTRIBUTING §3).
- **Each book explains itself** in its first document, "About this book".
- **Reproducible.** The same sources give the same bytes.

## What it declines to do

- **No whole books,** and no commercial titles or publishers named or linked
  in an issue, commit or README.
- **No fonts, and no images except generated ones,** in reduced books.
- **No books from pull requests.** A PR that brings a book is turned into an
  issue; the book is rebuilt from a template.
- **No tool's rule id as a key.** Sets are filed by specification clause;
  rule ids appear only in the set README.
- **No settling by bundle** (CONTRIBUTING §6).
- **No set on unsettled specification text.** It waits (CONTRIBUTING §4).
- **No executable files under `books/`.**

## Layout

```
books/                          CC BY 4.0
  templates/
    epub3-minimal/              EPUB 3.3, zero findings
    epub2-minimal/              EPUB 2.0.1, zero findings
  epub-3.3/<area>/<anchor>/<set>/
  epub-2.0.1/<area>/<anchor>/<set>/
  css-<module>/<anchor>/<set>/
  bundles/                      generated from verified sets
  INDEX.md, index.json          generated at each release (scripts/release.py)
scripts/                        AGPL-3.0-only
  lib/epubbook.py               shared builder: metadata, about.xhtml, ZIP
  lib/zippatch.py               byte changes made to a finished ZIP
  lib/rawzip.py                 a ZIP writer that controls every header field,
                                ZIP encryption included
  lib/minifont.py               a two-glyph TrueType font, and font obfuscation
  lib/ocfvariants.py            the OCF sets' containers, one function each
  check.py                      runs both verifiers, keeps their outputs
  release.py                    index, release check, download bundle
  templates/<template>/build.py builds a template; package() for sets
  <same path as the set>/build.py
```

- `<area>` is the part of the specification (`ocf`, `package`, `content`,
  `nav`, …); `<anchor>` is the section's stable anchor in the specification,
  not its number, because numbers change between versions.
- A set that touches more than one clause goes under its main clause, and
  its README lists the others.

### A set folder

- `README.md` with these sections: a header list (book, build script,
  origin, who asked, issue, other clauses); **About this book** (the text
  that goes into the book); **Question**; **Clause** (quoted, with links);
  **Expected result**; **Verifier results** (table with versions, commands
  and output files; the marks); **Other readers** (optional: what common ZIP
  or EPUB readers do with it); **Build**; **History** (`- YYYY-MM-DD: what
  changed and why`).
- The book or books, `<set>.epub`.
- One output per verifier run: `<book>.epubveri-<version>.txt`,
  `<book>.epubcheck-<version>.txt`. Never edited after they are published.

### Inside a book (EPUB 3)

`mimetype`, `META-INF/container.xml`, `OEBPS/package.opf`,
`OEBPS/about.xhtml` (first in the spine), `OEBPS/content.xhtml` (the
document a set changes), `OEBPS/nav.xhtml` (not in the spine). EPUB 2 has
`OEBPS/toc.ncx` in place of the navigation document. The templates' READMEs
list every part and its clause.

Metadata in every book: a `urn:uuid:` (UUID v5 of
`https://github.com/veripublica/epub-test-books/books/<set path>`); title;
`en`; `dc:creator` and `dc:publisher` `veripublica`; `dc:contributor` (who
asked for the set); `dc:date` and `dcterms:modified` from the README's
History; `dc:description` (the question); `dc:subject`; `dc:rights` (the
credit line); `dc:source` (the repository); `belongs-to-collection`
`epub-test-books` with `collection-type` `set` (EPUB 3 only); EPUB
Accessibility 1.1 discovery metadata. A set that tests one of these changes
it on purpose and says so.

## Commands

Python 3, standard library only (tested with 3.14).

```sh
python3 scripts/templates/epub3-minimal/build.py           # build a template
python3 scripts/<set path>/build.py                        # build a set
python3 scripts/check.py books/<set path>                  # run both verifiers
```

```sh
python3 scripts/release.py lint                            # what CI runs on every PR
python3 scripts/release.py index vX.Y.Z                    # regenerate the index
python3 scripts/release.py check vX.Y.Z --full             # the gate before a tag
python3 scripts/release.py bundle vX.Y.Z <outdir>          # the release assets
```

`check.py` writes `<book>.<tool>-<version>.txt` next to each book. If an
output for that version already exists and the new run differs, it stops
instead of overwriting.

Verifiers: [epubveri](https://github.com/veripublica/epubveri) (latest
release) run as `epubveri -i <book> -u --advisory`;
[epubcheck](https://github.com/w3c/epubcheck) (latest release, 5.4.0 at
present) run as `epubcheck <book> -u`. Without `-u`, usage-level messages
are hidden by both.

## Using the books

Read them in place; do not copy them into your repository.

- **In CI:** check out a release tag (`repository: veripublica/epub-test-books`,
  `ref: v0.2.0`). Pin a tag, never `main`: a new set changes what your tests
  see.
- **Locally:** one clone, read-only. Write your tool's outputs into your own
  project.
- A test suite that cannot find the books says it skipped them; it does not
  pass silently.

## Releases

Tags, `vMAJOR.MINOR.PATCH` (CONTRIBUTING §7):

- **PATCH:** documentation or script fixes that change no book and no
  expected result.
- **MINOR:** new sets, outputs or bundles.
- **MAJOR:** a book or expected result changes, a set is removed or moved, or
  a template changes.

While the version is `0.x`, a MINOR release may carry what would be MAJOR,
and its notes say so. Every changed expected result is listed in the release
notes with its issue.

The release steps are in CONTRIBUTING §7: regenerate the index for the tag,
pass `release.py check <tag> --full`, tag, then publish every book as
`<spec>--<anchor>--<set>--<valid|invalid>.epub` plus
`epub-test-books-<tag>.zip`. CI
(`.github/workflows/check.yml`) runs `lint` on every pull request and push,
and on a tag also checks that the index was made for that tag.

Index fields per book (`index.json`): `path`, `book`, `asset`, `sha256`,
`title`, `question`, `expected`, `marks`, `asked_by`, `issue`, and for
`epubveri` and `epubcheck` each: `version`, `verdict`, `messages`, `output`.
They come from the set README's header lines (`- Expected:`, `- Marks:`,
`- Asked for by:`, `- Issue:`) and the newest verifier output files.

## Workflow

1. Anyone opens a **New set** issue (`.github/ISSUE_TEMPLATE/new-set.md`).
2. The maintainer settles the clause and expected result in the issue and
   builds the book from a template (`.github/pull_request_template.md` holds
   the checklist).
3. Both verifiers run; outputs are added; differences are marked.
4. The project or person who asked reviews it; the maintainer approves the
   merge, which closes the issue. The set ships in the next release.
5. Anyone may object later under the issue. A reopened issue is settled the
   same way as a new one.

A change to `README.md`, `CONTRIBUTING.md` or this process is proposed as an
issue labelled `process`.

## Licence

- `books/`, READMEs and documentation: CC BY 4.0 (`LICENSE`).
- `scripts/`: AGPL-3.0-only (`LICENSE-AGPL`).
- The books and other output the scripts produce are CC BY 4.0, whatever
  parts of the scripts they contain. Running an unmodified script places no
  duty on the user.
- `NOTICE` states the map. SPDX: `CC-BY-4.0 AND AGPL-3.0-only`.

Credit line for anyone who copies books into their own project:

```
EPUB test books © veripublica contributors, CC BY 4.0, https://github.com/veripublica/epub-test-books
```

If someone believes a book carries their work, the book is removed first and
discussed after.
