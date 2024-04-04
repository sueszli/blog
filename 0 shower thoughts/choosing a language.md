# choosing a programming language

programming languages are abstractions over machine code.

but the compilers and interpreters that translate these abstractions into machine code can never be as efficient as hand-written assembly code.

so by using any programming language other than assembly, you are already trading off control and performance over convenience.

the same tradeoff applies to the choice of programming language.

_purposes of abstractions:_

- simplicity:

     - productivity: easier for you to write code.
     - quality: easier for you to read other people's code.
     - community: more people to collaborate with, a larger ecosystem.

     when your code gets run more than it gets written, these things become irrelevant.

- safety:

     we want to avoid spacial and temporal memory errors [^mem]

     - runtime checks: hurts performance as we waste cpu cycles on checks and memory management.
     - compile-time checks: doesn't impact performance.

     when your code gets run more than it gets written, people get in fights over whether sacrificing runtime safety for performance is worth the risks involved.

you should start investing in performance when your infrastructure costs exceed your developer costs.

caring too early about performance leads to premature optimization, while caring too late leads to costly rewrites.

## performance

the most popular benchmark, called [the benchmark game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/box-plot-summary-charts.html), also clusters languages into tiers based on performance.

0. closest to metal:
      - c
      - c++
      - rust
1. loss of performance is negligible:
      - c#
      - go
      - swift
      - java
      - ocaml
      - node.js
2. loss of performance is noticeable:
      - php
      - erlang
      - python
      - lua
      - perl
      - ruby

## popularity

we want to be able to collaborate and take advantage of existing ecosystems.

this means having to constrain ourselves to some of the most popular languages.

this decision is based on the following sources:

- code_report:
     - https://plrank.com/
- stackoverflow
     - 2023: https://survey.stackoverflow.co/2023/
     - 2022: https://survey.stackoverflow.co/2022/
     - all time: https://insights.stackoverflow.com/trends?tags=java%2Cc%2Cc%2B%2B%2Cpython%2Cjavascript%2Ctypescript%2Cgo%2Crust%2Cnode.js
- github
     - 2023: https://github.blog/wp-content/uploads/2023/11/github-top-10-programming-languages.png?w=1024&resize=1024%2C576
     - 2022: https://octoverse.github.com/2022/top-programming-languages
     - https://ossinsight.io/collections/programming-language/trends/
     - https://anvaka.github.io/map-of-github/#2/0/0
     - https://tjpalmer.github.io/languish/
     - https://madnight.github.io/githut/
     - https://githut.info/
     - https://live.ossinsight.io/
- jetbrains
     - https://www.jetbrains.com/lp/devecosystem-2023/
     - https://www.jetbrains.com/lp/devecosystem-2022/
- google: https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=JavaScript,%2Fm%2F05z1_,java,golang

## my personal preferences

_python_

- popularity:
     - great for prototyping and data centric work. preferred over R, Julia, Matlab and all other scripting languages.
- performance:
     - just as good as node for most io-bound tasks (fastapi). but for cpu-bound tasks the low performance is very noticeable. frequently 10-100x slower than node.
     - a lot of work is being put into removing the GIL.
     - new superset languages are being developed like "mojo".
     - has zero-overhead interopt with c/c++ through cpython extensions.
     - no multithreading support. only multiprocessing.

_javascript/typescript_

- popularity:
     - great for full-stack web development because it lets you share code between the frontend and backend. preferred over php, dart, swift, objective-c and all because with react-native and electron you can target all platforms with one codebase.
     - around [65% of js devs also use node.js](https://2022.stateofjs.com/en-US/usage/#what_do_you_use_js_for). but i don't think that the node users outnumber python users. node outside of fullstack development doesn't make much sense.
- performance:
     - async works great for io-bound tasks.
     - for cpu-bound tasks a lot of work was already put into runtime engines like v8, deno and bun which are frequently underappreciated.
     - no multithreading support. only multiprocessing. node `worker_threads` are closer to lightweight processes than threads. each have their own v8 engine and event loop instance.

_go_

- popularity:
     - great for networked systems, cloud development. great package manager. compilable to small binaries.
     - not as widely used as java, not significantly faster than java, but a lot easier to write highly concurrent code in.
- performance:
     - very simple concurrency model without "colored functions", very lightweight goroutines. kind of like an imperative and more approachable version of erlang/elixir.

_java_

- popularity:
     - popular in big companies. preferred over c#, kotlin, scala, groovy, clojure and all other jvm languages.
          - java is preferred to kotlin because it's not a java superset and can't compete with it.
          - [features aren't compelling enough](https://kotlinlang.org/docs/comparison-to-java.html): null safety (java lomboks), coroutines (java virtual threads), native builds (project graalvm)
          - access to jvm ecosystem but [not a superset of java](https://www.reddit.com/r/java/comments/ndwz92/can_i_get_some_reasons_to_use_java_instead_of). this is dangerous: groovy, clojure and scala all failed to compete.
     - catching up with projects like graalvm, quarkus and loom. newer versions are becoming more ergonomic.
- performance:
     - the jvm is very fast and highly optimized for long-running processes but it has a high startup time (cold start) and a high memory footprint.

_c++_

- popularity:
     - the most popular languages for systems programming. preferred over c (unless you're working on embedded systems or writing a kernel or a bootloader, where you just need a single level of abstraction over assembly). huge ecosystem with cuda, opencl, vulkan, opengl, directx, sdl, qt, boost, eigen, tensorflow, pytorch, etc.
     - hard to write safe code in using smart pointers and RAII.
- performance:
     - close to zero overhead.

_rust_

- popularity:
     - the only systems programming language with memory safety guarantees enforced at compile time with ownership model and borrow checker.
     - not popular enough (yet?) to be considered for most projects. very small ecosystem. [most fans are just hobby developers](https://blog.jetbrains.com/rust/2023/01/18/rust-deveco-2022-discover-recent-trends/#work-or-hobby?).
     - makes a lot of sense when adversaries have an attack surface via network access. which is why ie. the network stack of the linux kernel has adopted rust.
     - feels like a revival of [ada](https://ada-lang.io/) and tackles many similar weaknesses.
- performance:
     - close to zero overhead.

## references

_inspiration:_

- [brett cannon's blog post](https://snarky.ca/programming-language-selection-is-a-form-of-premature-optimization/)
- theo/t3: ["performance doesn't matter...until it does."](https://www.youtube.com/watch?v=2Z4fZtSKlcE)
- theo/t3: ["is 'full stack' even real?"](https://youtu.be/rAjd8z-Fx5A)
- [uncle bob's discussion on performance](https://github.com/unclebob/cmuratori-discussion/blob/main/cleancodeqa.md)

[^mem]: report from the white house https://stackoverflow.blog/2024/03/04/in-rust-we-trust-white-house-office-urges-memory-safety/#:~:text=spatial%20and%20temporal
