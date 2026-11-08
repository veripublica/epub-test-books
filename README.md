# epub-test-books

These are small EPUBs for testing EPUB tools. Each book asks one question: it
shows one rule from the EPUB or CSS specifications, or one defect I have seen
in real books, and nothing else. If your validator, converter or reader gets
it wrong, you can tell exactly what it got wrong.

Every book starts from a template that is already valid, so the only finding
it raises is the one it was built for. I write the expected result from the
specification before the book exists, and I run every book through two
validators, [epubveri](https://github.com/veripublica/epubveri) and
[epubcheck](https://github.com/w3c/epubcheck), keeping their outputs next to
it. Where either of them disagrees with the specification, the book's
README says so and why. None of the books
contain commercial content.

The latest release, v0.2.0, holds the two templates, one for EPUB 3 and one
for EPUB 2, and 22 sets on the EPUB container (OCF): damaged ZIP files, the
mimetype file, file names, `container.xml` and its rootfile. Every book
is listed on one page, [`books/INDEX.md`](./books/INDEX.md), with what it
should give and what each validator says. Each release also has every book
as a download, one by one or all together in a single zip.

To use the books in CI, check out a release tag and read them in place:

```yaml
- uses: actions/checkout@v4
  with:
    repository: veripublica/epub-test-books
    ref: v0.2.0
    path: epub-test-books
```

Pin a tag rather than `main`, because every new set changes what your tests
see.

If a book broke your tool, or you know a rule nobody checks, open an issue.
You don't need to build anything: I make the book, and the discussion stays
under the issue for anyone to read. If you think a book's expected result is
wrong, say so there too. [`CONTRIBUTING.md`](./CONTRIBUTING.md) explains how
a set is built and checked. The folder layout, the release rules
and the rest of the detail are in [`AGENTS.md`](./AGENTS.md). If you believe
a book here carries your work, open an issue or write to me at
baris@kayadelen.com: I remove the book first and we talk after.

## Licence

The books and documentation are [CC BY 4.0](./LICENSE), and the build scripts
are [AGPL-3.0-only](./LICENSE-AGPL). [`NOTICE`](./NOTICE) has the details. If
you copy books into your own project, one line of credit is enough:

```
EPUB test books © veripublica contributors, CC BY 4.0, https://github.com/veripublica/epub-test-books
```
