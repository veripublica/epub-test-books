# A script outside the container

- Book: `remote-script.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-resource-locations/remote-script/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: [#549](https://github.com/veripublica/epub-test-books/issues/549)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml loads a script from an https URL, listed in the manifest. Its manifest item has the scripted and remote-resources properties. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Scripts are not among the resources that may be hosted outside the container.

## Question

`content.xhtml` loads a script from an `https` URL. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-resource-locations`](https://www.w3.org/TR/epub-33/#sec-resource-locations):

> EPUB creators MAY host the following types of publication resources outside the EPUB container: Audio resources. Video resources. Resources retrieved via scripting APIs (e.g., XmlHttpRequest [xhr] and Fetch [fetch]). Font resources.
>
> EPUB creators MUST store all other resources within the EPUB container.

## Expected result

Invalid. Scripts are not among the resources that may be hosted outside the container.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i remote-script.epub -u --advisory` | ERROR RSC-006; INVALID | `remote-script.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck remote-script.epub -u` | ERROR RSC-006; INVALID | `remote-script.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<script src="https://example.org/epub-test-books/script.js"></script>` in its head and `properties="scripted remote-resources"`. That URL is a manifest item, `application/javascript`.

## History

- 2026-11-13: First version.
