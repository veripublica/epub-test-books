# Contributing

These rules are fixed from the start. A change to them is proposed as an
issue labelled `process` and decided in that issue, in the open.

## 1. A set starts as an issue

Open an issue with the **New set** template before building anything. It
states:

1. **the question:** one thing the book shows;
2. **the clause:** the specification, its version, the section anchor, and
   the sentence quoted;
3. **the expected result,** derived from the clause, before any tool runs;
4. **what the verifiers say today,** if known: epubveri and epubcheck, with
   versions;
5. **the origin:** `built here` or `reduced from a real book`.

Never attach or link a commercial book, and never name its title or
publisher, in an issue, a commit or a README. Reduce it first (§3).

## 2. Templates

Every book starts from a template in `books/templates/` and changes only
what its question needs.

- A template carries every part its EPUB version requires. The list comes
  from the specification, and each item cites its clause in the template's
  README.
- Placeholder values are valid values, so they raise nothing: a fixed
  `urn:uuid:` identifier, `Test book` as the title, `en` as the language. A
  set that needs an ISBN adds one on purpose, with a correct check digit.
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

1. The book is built and opened as a pull request that links its issue.
   The book goes under `books/`; its build script, if any, under `scripts/`
   at the same path. Nothing executable goes under `books/`.
2. epubveri runs on it, and its output is compared with the expected result.
3. epubcheck runs on it. Every place where the two differ is marked in the
   README with one of three marks:
   - **intended:** the clause, and the epubcheck issue if one exists;
   - **spec unclear, followed epubcheck:** with the W3C issue, where one is
     worth filing;
   - **missed:** a defect in the verifier that missed it, with that
     verifier's issue.
4. The README records, for each epubveri finding, whether it is in the
   default output or under `--advisory`.
5. **Review by someone other than the issue's author.** The set is merged
   only after that approval. The merge closes the issue; the set ships in
   the next release.

A disputed reading of the specification is settled by the maintainers in
the issue. Where the specification text itself is unclear, an issue goes to
W3C (the specification's repository, or `w3c/epubcheck` for epubcheck's
reading), and the set waits.

## 5. Objections

Anyone may object to a set at any time: comment under its issue, or ask for
it to be reopened. A reopened issue is settled the same way as a new one.
If the expected result changes, the set changes, and the change is listed
in the release notes.

Old verifier outputs are never edited. A new run adds a new file with its
version; a new difference gets its mark.

## 6. Bundles

A bundle (for example, every CSS set in one book) is generated from
verified sets by a script in `scripts/`, goes under `books/bundles/`, and
its README says so. A bundle
is a quick check of many sets at once. It settles nothing on its own: one
fatal defect can hide the others.

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

## 8. Licence of contributions

By contributing you agree that your contribution is licensed as the rest of
the repository: everything under `books/`, READMEs and documentation under
CC BY 4.0; everything under `scripts/` under AGPL-3.0-only, with the books
and other output the scripts produce under CC BY 4.0. You confirm that the book is built from scratch or reduced as in
§3, and that you have the right to give it.
