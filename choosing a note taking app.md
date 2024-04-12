# choosing a note taking app

## why markdown?

if you want to write notes, you have to choose a file format.

i suggest plaintext [^plain], so that you can easily search, version control, backup and share your notes. you don't want to use a binary format like docx or odt.

there are lots of plaintext formats to choose from [^comp1] [^comp2] [^comp3].

but you also want your format to be widely supported.

let's take the ability of your notes to be rendered on github as a constraint [^gh1] [^gh2] and then rank them by popularity:

1. markdown (md):
      - created in 2004.
      - huge community and ecosystem: supported by all static site generators, default language for github, stackoverflow, reddit, confluence.
      - easy to write and import/export into most other formats.
      - one of the least expressive: difficult to format and structure text.
      - ambiguous syntax: has too many dialects / flavors and the parser is implemented differently by every company (obsidian, github, confluence all have their own flavour).
2. html:
      - created 1 year after xml (1996).
      - most expressive: supports styling, scripting, can be interactive.
      - tag soup: difficult to write and read.
3. asciidoc (adoc):
      - not well known enough - mostly used by book authors or in the java community.
      - too verbose to be productive in.
      - very experssive. has a lot more features than markdown.
4. restructuredtext (rst):
      - not well known enough - mostly used in the python community.
      - but actually very elegant: intuitive syntax, easy to write and read. native support for nested blocks and lists.

you will most likely only see markdown in the wild since the others are either not known well enough or too verbose. and at the end of the day it doesn't matter too much since you can always convert between formats with tools like [pandoc](https://pandoc.org/).

i highly discourage using html for notes since you'll be constrained to a rendering engine / wysiwyg editor to be productive. this in itself can be circumvented if there would be nice html editors to write notes in. but there aren't any. i only know [notion](https://www.notion.so/). but it has some serious drawbacks:

- slow and unreliable: feels janky both on mobile and on web, always breaks on large documents, sometimes doesn’t sync data which is scary
- export feature kind of sucks:
     - html – works great, but must be un-minified to be editable again
     - pdf – lossy, doesn’t keep all data and formatting
     - markdown – lossy, doesn’t keep all data and formatting

## requirements

first, here are my requirements. i want a markdown editor that:

- is popular: has a large community, well maintained, frequently updated
- is offline/local-first
- is free or has a one-time payment, no monthly subscription
- is wysiwyg / has live preview: doesn't require you to open a second preview window
- can render math: large complex equations

## my recommendations

- obsidian
     - website: https://obsidian.md/
     - largest community, lots of plugins, highly customizable
     - has live preview, can render math
- marktext
     - website: https://github.com/marktext/marktext
     - true wysiwyg editor, very similar to notion in terms of block editing
     - not as pretty as obsidian
     - discussion: https://news.ycombinator.com/item?id=29687061
     - no longer maintained: https://github.com/marktext/marktext/issues/1290#issuecomment-726744803

## other options

_too expensive (when compared to free options)_

- typora
     - website: https://typora.io/
- byword
     - website: https://apps.apple.com/app/byword/id420212497?mt=12

_bad ui/ux (compared to recommendations)_

- fsnotes
     - website: https://fsnot.es/
     - github repository: https://github.com/glushchenko/fsnotes
- zettlr
     - website: https://www.zettlr.com/
- joplin
     - website: https://joplinapp.org/
- trilium
     - website: https://github.com/zadam/trilium
- logseq
     - website: https://logseq.com/
     - uses bullet points for structure, which ruins the point of markdown

_still in development_

- nota
     - most promising, extremely nice user interface
     - website: https://nota.md/buy.html
     - previous version: caret, https://caret.io/ (surprisingly buggy and slow)
- vscode extensions
     - very promising
     - vscode: https://code.visualstudio.com/
     - milkdown: https://milkdown.dev/ → life preview for vscode, still in development
     - dendron: https://www.dendron.so/
     - wikilens: https://marketplace.visualstudio.com/items?itemName=lostintangent.wikilens
- bangle.io
     - very promising
     - website: https://app.bangle.io/landing
- simplenote
     - website: https://app.simplenote.com/
     - also simplenote-electron: https://github.com/Automattic/simplenote-electron → not a wysiwg editor

_has monthly subscription_

- outline
     - website: https://github.com/outline/outline
     - demo: https://student-tuwien-ac.getoutline.com/collection/welcome-zpKDLvb5ZS
     - subscription: 7-10$ a month
     - self hosted: 7-10$ a month based on https://thomasgriffin.com/how-to-install-the-outline-knowledge-base-wiki-on-ubuntu/
          - complex to set up, can take up a few hours
          - docker tutorial: https://hub.docker.com/r/outlinewiki/outline
          - source build tutorial: https://docs.getoutline.com/s/hosting/doc/from-source-BlBxrNzMIP
- ulysses
     - website: https://ulysses.app/
- bear
     - website: https://bear.app/
- roam research
     - website: https://roamresearch.com/
     - basically just like obsidian

## footnotes

[^plain]: [the unreasonable effectiveness of plain text](https://www.youtube.com/watch?v=WgV6M1LyfNY)
[^comp1]: [comparison of lightweight markup languages](https://en.m.wikipedia.org/wiki/Lightweight_markup_language#:~:text=Comparison%20of%20language%20features)
[^comp2]: [well-known document markup languages](https://en.m.wikipedia.org/wiki/List_of_document_markup_languages#:~:text=Well%2Dknown%20document%20markup%20languages)
[^comp3]: [markdown vs. asciiDoc vs. reStructuredText](https://www.dewanahmed.com/markdown-asciidoc-restructuredtext/)
[^gh1]: [github gist](https://gist.github.com/ChrisTollefson/a3af6d902a74a0afd1c2d79aadc9bb3f)
[^gh2]: [github markup](https://github.com/github/markup) (the official github plaintext parser)
