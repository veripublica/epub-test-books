# Contributing

These rules are fixed. A change to them is proposed as an issue labelled
`process` and decided in that issue, in the open.

The maintainer decides, in the issue, and says why. Anyone may comment,
object, or ask for an issue to be reopened, and every decision stays
readable where it was made.

## 1. A set starts as an issue

You do not need to build anything. Open an issue with the **New set**
template. It states:

1. **the question:** one thing the book shows;
2. **the clause:** the specification, its version, the section anchor, and
   the sentence quoted;
3. **the expected result,** derived from the clause, before any tool runs;
4. **what the verifiers say today,** if known: epubveri and epubcheck, with
   versions;
5. **the origin:** `built here` or `reduced from a real book`.

If you are not sure of the clause or the expected result, say what you saw;
the issue is where it gets worked out. The maintainer builds the book.

A pull request that brings a finished book is closed and turned into an
issue. The book is used as input only, and rebuilt from a template, so that
every book in the library comes out of the same build.

Never attach or link a commercial book, and never name its title or
publisher, in an issue, a commit or a README. Reduce it first (§3).

## 2. Templates

Every book starts from a template in `books/templates/` and changes only
what its question needs.

- A template carries every part its EPUB version requires, and meets its
  recommendations (SHOULD) too, so a correct validator reports nothing on
  it. Each part cites its clause in the template's README.
- EPUB 3 books follow EPUB 3.3, the current W3C Recommendation. EPUB 2
  books follow EPUB 2.0.1.
- Placeholder values are valid values, so they raise nothing. The template
  title is `Test book`; each set uses its own short title. The language is
  `en`. A set that needs an ISBN adds one on purpose, with a correct check
  digit.
- Each set has its own fixed identifier: a `urn:uuid:` derived (UUID v5)
  from its path, so books never share one and a rebuild never changes it.
- Each book explains itself. Its first document, "About this book", is
  generated from the set README. The defect never goes in that document.
  In CSS sets it stays unstyled, so it does not affect the cascade under
  test.
- `dcterms:modified` (EPUB 2: `dc:date opf:event="modification"`) is the
  last date in the set README's History, so the book says when it last
  changed. `dc:date` is the first.
- The build is reproducible: the same sources give the same bytes.
- A template is a set itself: zero findings from epubveri and from
  epubcheck, both versions recorded. A change to a template is re-verified
  before any book is built from it, and every book built from it is re-run.

## 3. Reducing a real book

Whole books are never accepted. A reduced book:

- starts from a template, and takes in only the part that shows the
  pattern;
- has its text replaced by placeholder text;
- has no fonts, and no images except generated ones;
- has no title, author, publisher, identifier (ISBN, `dc:identifier`, UUID)
  or file name that points to the source;
- keeps only the stylesheet rules that still trigger the pattern, with
  distinctive class and id names renamed.

If the pattern disappears when something is removed, that part is needed;
keep it in its smallest form and say why in the README.

## 4. Verifying a set

1. The book is built by a script under `scripts/`, at the same path as its
   set under `books/`, and opened as a pull request that links its issue.
   Nothing executable goes under `books/`. A defect that a correct ZIP
   writer cannot produce is made by changing the finished file's bytes in
   a separate step (`scripts/lib/zippatch.py`).
2. Both verifiers run on it, with every message shown:
   `epubveri -i <book> -u --advisory` and `epubcheck <book> -u`
   (`scripts/check.py`). The library uses epubcheck's latest release and
   epubveri's latest release.
3. Both outputs are compared with the expected result. The specification
   decides; neither tool does. Every place where a verifier differs from the
   expected result is marked in the README with one of three marks:
   - **intended:** the clause, and the verifier's issue if one exists;
   - **spec unclear, followed epubcheck:** with the W3C issue, where one is
     worth filing;
   - **missed:** a defect in the verifier that missed it, with that
     verifier's issue.
4. The README records, for each epubveri finding, whether it is in the
   default output or under `--advisory`.
5. **Review by the project or person who asked for the set.** The
   maintainer approves the merge. The merge closes the issue; the set ships
   in the next release.

A disputed reading of the specification is settled by the maintainer in the
issue. Where the specification text itself is unclear, an issue goes to
W3C (the specification's repository, or `w3c/epubcheck` for epubcheck's
reading), and the set waits.

## 5. Objections and corrections

Anyone may object to a set at any time: comment under its issue, or ask for
it to be reopened. A reopened issue is settled the same way as a new one.

Being wrong is expected, and it stays visible. If the expected result
changes, the set changes, its README's History says what changed and why,
and the release notes list it with the issue.

Old verifier outputs are never edited. A new run adds a new file with its
version; a new difference gets its mark.

## 6. Bundles

A bundle (for example, every CSS set in one book) is generated from
verified sets by a script in `scripts/`, goes under `books/bundles/`, and
its README says so. A bundle is a quick check of many sets at once. It
settles nothing on its own: one fatal defect can hide the others.

## 7. Releases

Releases are tags, `vMAJOR.MINOR.PATCH`. Tools pin a tag.

- **PATCH:** README, documentation or script fixes that change no book and
  no expected result.
- **MINOR:** new sets, new outputs, new bundles.
- **MAJOR:** a set's book or expected result changes, a set is removed or
  moved, or a template changes. A pinned test may now see something
  different.

While the version is `0.x`, a MINOR release may carry what would be MAJOR,
and its notes say so.

Every release, in this order:

1. `python3 scripts/release.py index vX.Y.Z` writes `books/INDEX.md` and
   `books/index.json` for that release: one line per book, with its expected
   result, both verifiers' results, its marks, its issue and its download.
2. `python3 scripts/release.py check vX.Y.Z --full` passes. It fails if the
   index was made for another release or does not match the books, if a
   rebuild changes a book's bytes, or if a verifier output is not current.
3. The tag goes on that commit. CI checks the index against the tag again.
4. The GitHub release carries every book as its own file, named
   `<spec>--<anchor>--<set>.epub`, and all of them in one
   `epub-test-books-vX.Y.Z.zip` (`python3 scripts/release.py bundle`).

A release whose index was made for another release does not ship.

## 8. Licence of contributions

By contributing you agree that your contribution is licensed as the rest of
the repository: everything under `books/`, READMEs and documentation under
CC BY 4.0; everything under `scripts/` under AGPL-3.0-only, with the books
and other output the scripts produce under CC BY 4.0. You confirm that what
you send is built from scratch or reduced as in §3, and that you have the
right to give it.
