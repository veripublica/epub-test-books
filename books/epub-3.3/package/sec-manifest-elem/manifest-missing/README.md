# No manifest

- Book: `manifest-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-manifest-elem/manifest-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the package document section
- Issue: [#47](https://github.com/veripublica/epub-test-books/issues/47)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package document has no manifest element, so the spine points to nothing and no item is the navigation document. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The element is required. The spine's references then point to nothing and no item is the navigation document. Both follow from the same defect and can't be separated from it.

## Question

The package document has no `manifest` element. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-manifest-elem`](https://www.w3.org/TR/epub-33/#sec-manifest-elem):

> REQUIRED second child of package, following metadata.

## Expected result

Invalid. The element is required. The spine's references then point to nothing and no item is the navigation document. Both follow from the same defect and can't be separated from it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i manifest-missing.epub -u --advisory` | ERROR RSC-005, ERROR RSC-005, ERROR OPF-049, ERROR RSC-005, ERROR OPF-049, USAGE OPF-003, USAGE OPF-003, USAGE OPF-003; INVALID | `manifest-missing.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck manifest-missing.epub -u` | ERROR RSC-005, ERROR OPF-049, ERROR OPF-049, ERROR RSC-005, ERROR RSC-005, USAGE OPF-003, USAGE OPF-003, USAGE OPF-003; INVALID | `manifest-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

The other errors are the consequences the expected result names: the spine points to nothing, no item is the navigation document, and the files in the container are no longer listed.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the `manifest` element is removed.

## History

- 2026-11-09: First version.
