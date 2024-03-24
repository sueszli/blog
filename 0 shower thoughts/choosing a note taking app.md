# which note taking app should i use?

when looking at note taking software, we have to differentiate between the editors (notion, coda, asana, obsidian, ...) and file formats (html, markdown, asciidoc, restructuredtext, ...).

## file formats

the file format must be future-proof and in plain text.

- [comparison of lightweight markup languages](https://en.m.wikipedia.org/wiki/Lightweight_markup_language#:~:text=Comparison%20of%20language%20features)
- [well-known document markup languages](https://en.m.wikipedia.org/wiki/List_of_document_markup_languages#:~:text=Well%2Dknown%20document%20markup%20languages)
- [markdown vs. asciiDoc vs. reStructuredText](https://www.dewanahmed.com/markdown-asciidoc-restructuredtext/)
- [github gist](https://gist.github.com/ChrisTollefson/a3af6d902a74a0afd1c2d79aadc9bb3f)
- [github markup](https://github.com/github/markup) (the official github plaintext parser)

the 4 most popular formats, which are supported by github's parser, are:

1. html:
      - created 1 year after xml (1996).
      - the most expressive markup language: also supports scripting and styling - but is also way too verbose for the very same reason.
      - the most future-proof markup language: is now the language of the web.
2. markdown (md):
      - created in 2004.
      - huge community and ecosystem: supported by all static site generators, default language for github, stackoverflow, reddit, confluence.
      - easy to write and import/export into most other formats.
      - one of the least expressive: difficult to format and structure text. no vertical spacing.
      - ambiguous syntax: has too many dialects / flavors and the parser is implemented differently by every company (obsidian, github, confluence all have their own flavour).
3. asciidoc (adoc):
      - too verbose to be productive in.
      - used frequently to write books or large documents.
      - has more features than markdown and doesn't need html to make up for them.
4. restructuredtext (rst):
      - unpopular and only used in the python community.
      - very elegant: lets you write nested blocks and lists (the only markup language that does this).

in conclusion, the only 2 formats worth considering are: html, markdown.

## best editor: html

_best html editors:_

- [notion](https://www.notion.so/) (convenient for small projects):
     - **most convenient: true wysiwyg experience**, syncs data between all devices, pages are easy to share as websites
     - **slow and unreliable: feels janky both on mobile and on web**, always breaks on documents, sometimes doesn’t sync data which is scary
     - export feature kind of sucks:
          - html – works great, but must be un-minified to be editable again
          - pdf – lossy, doesn’t keep all data and formatting
          - markdown – lossy, doesn’t keep all data and formatting
- coda: no export feature
- mem: not as popular yet
- microsoft loop: not released yet
- anytype: not released yet

## best editor: md

_best markdown editors:_

- [obsidian](https://obsidian.md/) (best for larger documents):

     - free
     - **local: no upload limits, no need to think about backups**
     - **inconvenient:** you have to obey very specific markdown rules
     - largest community
     - has a nice wysiwyg editor called 'live preview' but it still doesn't feel as nice as vscode
     - highly customizable: lets you inject custom css and javascript

- [vscode](https://code.visualstudio.com/) (best for small scripts):

     - free
     - coding shortcuts, linting, github copilot
     - not a wysiwyg editor (the [milkdown](https://milkdown.dev/) plugin is still in development) but has all obsidian features with plugins like "foam"

- [outline](https://github.com/outline/outline) (check out the online demo [here](https://student-tuwien-ac.getoutline.com/collection/welcome-zpKDLvb5ZS) – very close to notion but still a work in progress):
     - subscription: 7-10$ a month
     - self hosted: 7-10$ a month
          - free if self hosted (but infrastructure costs at least $6/month based on the official [installation tutorial](https://thomasgriffin.com/how-to-install-the-outline-knowledge-base-wiki-on-ubuntu/)) → installing takes 1-2 hours even if you know what you're doing
          - [docker tutorial](https://hub.docker.com/r/outlinewiki/outline)
          - [source tutorial](https://docs.getoutline.com/s/hosting/doc/from-source-BlBxrNzMIP)

_alternatives:_

- [zettlr](https://www.zettlr.com/) – close to obsidian, but not as pretty
- [logseq](https://demo.logseq.com/) – uses bullet-style blocks for everything which is annoying
- [simplenote](https://app.simplenote.com/) / [simplenote-electron](https://github.com/Automattic/simplenote-electron) – not a wysiwg editor
- [bangle.io](https://app.bangle.io/landing) – still pretty buggy
- [mark text](https://github.com/marktext/marktext) – don’t like the ui
- [joplin](https://joplinapp.org/) – don’t like the ui
- [nota](https://nota.md/buy.html) – txt editor, not markdown
- [caret](https://caret.io/) (previous version of nota) – buggy and slow
- [fsnotes](https://fsnot.es/) – not worth paying for
- [byword](https://apps.apple.com/app/byword/id420212497?mt=12) – not worth paying for
- [typora](https://typora.io/) – not worth paying for

## conclusion

notion and obsidian are the best choices – and they both have their own strengths and weaknesses.

- notion is fun and convenient: it has the least mental overhead and gets the job done. ideal for working in teams.
- obsidian is meant for larger projects: ideal for taking research notes.
