# epub-test-books

Small EPUBs for testing EPUB tools, one book per question. Each book shows
one thing — a rule from the EPUB or CSS specifications, or a defect pattern
seen in real books — and nothing else, so a tool's result on it can be read
without guessing.

- **One question per book.** Every book starts from a template that carries
  all the parts its EPUB version requires, so the only finding it raises is
  the one it is built for.
- **The expected result comes first, from the specification.** It is written
  in the set's issue before the book is built, with the clause quoted.
- **Every book is checked against two verifiers,** epubveri and epubcheck,
  with their exact versions recorded. Every place where they differ is
  marked and explained.
- **No commercial content.** Books are built from scratch, or reduced from a
  real book to the smallest part that still shows the pattern, with
  everything that carries the source's rights or identity removed.

## Layout

```
books/                      CC BY 4.0
  templates/
    epub3-minimal/          every part EPUB 3 requires, zero findings
    epub2-minimal/          every part EPUB 2 requires, zero findings
  epub-3.3/<area>/<anchor>/<set>/
  epub-2.0.1/<area>/<anchor>/<set>/
  css-<module>/<anchor>/<set>/
  bundles/                  generated from verified sets; settle nothing alone
scripts/                    AGPL-3.0-only
  <same path as the set>/   the script that builds that set's book
  ...                       bundle and check scripts
```

Books and scripts live in separate trees, so the licence follows the
folder: everything under `books/` is CC BY 4.0, everything under `scripts/`
is AGPL-3.0-only.

A set lives under the specification version and the section's stable
anchor, not its number, because section numbers change between versions.
A set that touches more than one clause goes under its main clause, and its
README lists the others. Tools' own rule ids are listed in the README, never
used as keys.

Each set folder under `books/` holds:

- `README.md`: the question, the clause, the expected result, the origin,
  each verifier's result with its version, and the marks;
- the book or books;
- one output file per verifier run, named with the exact version
  (`epubcheck-5.4.0.txt`, `epubveri-0.31.0.txt`).

Where a book is built by a script, the script lives under `scripts/` at the
same path as its set.

## Using the books

Read them in place; do not copy them into your repository.

- **In CI:** check out a release tag, for example with `actions/checkout`
  (`repository: veripublica/epub-test-books`, `ref: v0.1.0`). Pin a tag,
  never `main`: a new set changes what your tests see.
- **Locally:** one clone, read-only. Write your tool's outputs into your own
  project, never into this repository.
- A test suite that cannot find the books should say it skipped them, not
  pass silently.

## Licence

- `books/`, READMEs and documentation: [CC BY 4.0](LICENSE).
- `scripts/`: [AGPL-3.0-only](LICENSE-AGPL).
- The books and other output the scripts produce are CC BY 4.0, whatever
  parts of the scripts they contain.

You may copy, change and ship the books. If you copy them into your own
project, keep the credit — one line in the folder is enough:

```
EPUB test books © veripublica contributors, CC BY 4.0, https://github.com/veripublica/epub-test-books
```

Nothing here means veripublica endorses your use of it.

## Contributing, and disagreeing

Every set starts as an issue, in public. If you think a set's expected
result is wrong, say so under its issue, or ask for it to be reopened. See
[CONTRIBUTING.md](CONTRIBUTING.md).

If you believe a book here carries your work, open an issue or write to the
maintainers. The book is removed first and discussed after.
