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

     - runtime safety: hurts performance as we waste cpu cycles on checks and memory management.
     - compile-time safety: doesn't impact performance.

     when your code gets run more than it gets written, people get in fights over whether sacrificing runtime safety for performance is worth the risks involved.

you should start investing in performance when your infrastructure costs exceed your developer costs.

caring too early about performance leads to premature optimization, while caring too late leads to costly rewrites.

> i highly recommend checking out theo/t3's videos called ["performance doesn't matter...until it does."](https://www.youtube.com/watch?v=2Z4fZtSKlcE) and ["is 'full stack' even real?"](https://youtu.be/rAjd8z-Fx5A) as well as [uncle bob's discussion on performance](https://github.com/unclebob/cmuratori-discussion/blob/main/cleancodeqa.md) as they cover a lot of the same points.

## performance

the most popular benchmark, called [the benchmark game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/box-plot-summary-charts.html), also clusters languages into tiers based on performance.

0. closest to metal:
      - c
      - c++
      - rust
1. loss of performance is negligible.
      - c#
      - go
      - swift
      - java
      - ocaml
      - node.js
2. loss of performance is noticeable.
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

## conclusion

1. **JavaScript/TypeScript**

      - around [65% of js devs also use node.js](https://2022.stateofjs.com/en-US/usage/#what_do_you_use_js_for). it's unclear whether the node.js users alone still outnumber python users.
      - performance difference to java and go becomes really noticable as you scale up. has built-in async and worker threads: parallelism only through multiprocessing, not multithreading. worker threads do not operate exactly like threads. each worker thread has its own v8 and event loop instance.

2. **Python** ⭐

      - low performance is very noticeable. frequently 10-100x slower than nodejs. this will change soon as a lot of effort is being put into removing the GIL.
      - new superset languages are being developed for simd like “mojo”.
      - has great interopt with c/c++.

3. **Java** ⭐

      - verbose and bulky. trying to catch up with like projects like graalvm, quarkus, and loom.

4. ~~C#~~ – java is preferred. java has a larger data and systems ecosystem while c# is mostly used for game development.

5. **C/C++** ⭐

      - cpp syntax feels really awkward.
      - for networked systems, cpp is preferred over c because of smart pointers and RAII. but they're really hard to get right.

6. ~~PHP~~ – node.js is preferred to php.
7. ~~Shell~~

8. **Go** ⭐

      - the simplicity of python with the speed of java.
      - compilable to small binaries. very popular for cloud native development and networked systems.

9. **Rust** ⭐

      - great competitor to cpp: ownership model and borrow checker enforce memory safety.
      - very small ecosystem. [most fans are just hobby developers](https://blog.jetbrains.com/rust/2023/01/18/rust-deveco-2022-discover-recent-trends/#work-or-hobby?). adoption will still take a couple of years but it's growing fast and microsoft and the linux foundation have partially adopted it.

10. ~~Kotlin~~ – java is preferred to kotlin because it's not a java superset and can't compete with it.
       - [features aren't compelling enough](https://kotlinlang.org/docs/comparison-to-java.html): null safety (java lomboks), coroutines (java virtual threads), native builds (project graalvm)
       - access to jvm ecosystem but [not a superset of java](https://www.reddit.com/r/java/comments/ndwz92/can_i_get_some_reasons_to_use_java_instead_of). this is dangerous: groovy, clojure and scala all failed to compete.
11. ~~Ruby~~ – python is preferred to ruby because ruby is losing popularity fast.
12. ~~Swift~~ – javascript (react-native and electron) is preferred to swift until swift is more widely adopted.
13. ~~R~~
14. ~~PowerShell~~
15. ~~Dart~~ – javascript (react-native) is preferred to dart (flutter) until flutter's ecosystem catches up.
16. ~~Lua~~
17. ~~Scala~~ – java is preferred to scala because scala is losing popularity fast.
18. ~~Visual Basic~~
