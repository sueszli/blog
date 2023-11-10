this ranking is specifically for teams that build web backends / distributed systems.

we take a look at technologies and tools that developers currently use ("popularity") and want to use in the future ("growth").

- **popularity matters most**

  popularity is crucial because it brings more resources: libraries, tools, developers, and job opportunities.

  for me, when adopting a new language, the libraries and ecosystem are key. i aim to prototype quickly and collaborate with a large pool of people. practicality is prioritized over elegant code in esoteric languages.

- **growth is usually just hype**

  it's wise to wait before immediately adopting fast-growing languages.

  new languages emerge frequently, but it takes about 5 years for them to gain critical mass. for example:

  - c took 11 years (1975 to 1985)
  - java and other garbage-collected languages took 5-6 years (1995 to 2001)
  - ruby trended for 13 years (2006 to 2019) but never achieved widespread adoption.

  for some context, it's work taking a look at [wikipedia's history of programming languages](https://en.m.wikipedia.org/wiki/history_of_programming_languages).

- **technology adoption needs a reason**

  technologies, for customers or developers, must solve problems and be ✨convenient✨ to use and for replacing existing ones. when making choices, consider the "programming language triangle":

  - simplicity = faster development cycles, easier maintenance → lower time to market
  - efficiency = high performance, low resource usage (memory, cpu, disk, network) → lower costs
  - safety = robustness, security, minimal runtime exceptions, clear stack traces → higher availability and reliability

  based on which stage a business is in (startup, growth, or scale), it will prioritize different parts of the triangle but overall most businesses prioritize simplicity and safety over performance, leading to the incorporation of garbage collection in most popular languages.

  raw performance optimization usually occurs in specific and limited parts of a system once a business reaches a specific scale.

<br><br>

# comparing data sources

rankings based on multiple sources:

- **code_report**

  - https://plrank.com/ ⭐️ – is the most well-rounded ranking, based on multiple sources

- **stackoverflow**

  - official: https://survey.stackoverflow.co/2023/ → [comparing popularity vs. growth](https://survey.stackoverflow.co/2023/?utm_source=banner&utm_medium=display&utm_campaign=dev-survey-results-2023&utm_content=survey-results#section-admired-and-desired-programming-scripting-and-markup-languages)

  - https://survey.stackoverflow.co/2022/#worked-with-vs-want-to-work-with-language-worked-want-prof
  - https://insights.stackoverflow.com/trends?tags=java%2Cc%2Cc%2B%2B%2Cpython%2Cjavascript%2Ctypescript%2Cgo%2Crust%2Cnode.js

- **github**

  - official: https://octoverse.github.com/2022/top-programming-languages

  - https://ossinsight.io/collections/programming-language/trends/ → [specifically for distributed systems](https://ossinsight.io/explore/?id=dffebb3a-e5b8-4726-883c-137df2436c16)
  - https://anvaka.github.io/map-of-github/#2/0/0
  - https://tjpalmer.github.io/languish/
  - https://madnight.github.io/githut/
  - https://githut.info/
  - https://live.ossinsight.io/

- **jetbrains**

  - https://www.jetbrains.com/lp/devecosystem-2022 → [specifically based on platforms](https://www.jetbrains.com/lp/devecosystem-2022/#platfroms-by-language)

- **google**

  - https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=JavaScript,%2Fm%2F05z1_,java,golang

<br><br>

# comparing languages

- **javascript:** largest ecosystem, used for everything

  see: [https://www.youtube.com/watch?v=2Z4fZtSKlcE](https://www.youtube.com/watch?v=2Z4fZtSKlcE)

  creation dates: javascript in 1995, nodejs in 2009, typescript in 2012

  - is the number one by a wide margin

    about [≈65%](https://2022.stateofjs.com/en-US/usage/#what_do_you_use_js_for) of all js developers also use node.js

    has the best ecosystem and is used in almost every company

  - performance difference to java and go gets substantial as you scale up your system - but is still better than python

  - built-in async and worker threads: parallelism only through multiprocessing, not multithreading

    worker threads do not operate exactly like threads. each worker thread has its own v8 and event loop instance

<br>

- **python:** growing fast with ai hype, best for data processing and analysis, will be faster without GIL soon

  created 1991

  - extremely popular, ideal for building utilities and data analytics

  - has fast c libraries but its own performance is poor which is why it is frequently 10-100x slower in benchmarks than node.js

    global interpreter lock GIL (only one thread at a time), parallelism only through multiprocessing, not multithreading

    a lot of progress has been made to improve the performance with fastapi

    new superset languages are being developed for simd like the “mojo” language

    - https://travisluong.medium.com/fastapi-vs-fastify-vs-spring-boot-vs-gin-benchmark-b672a5c39d6c
    - https://benchmarksgame-team.pages.debian.net/benchmarksgame/box-plot-summary-charts.html
    - https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/python.html

<br>

- **java:** well established for systems but not not suitable for new projects

  created 1995

  - old, extremely bulky and requires a lot of boilerplate - java is like the cobol of the 21st century: not fun to work with but here to stay

    but it’s good to know for distributed systems developers as it has an established ecosystem for distributed systems, ie. apache libraries or akka

  - still trying to catch up in cloud computing and serverless applications through small native builds

    - native binaries for fast startup time and low memory footprint: graalvm

      ahead of time compiler which results in longer build times

    - kubernetes deployment: quarkus

      small artifacts, fast boot times, and low first-byte latency

    - concurrency: project loom

      lightweight and efficient virtual threads called fibers which are currently under development and will be finalized in java21

      but these technologies are still a work in progress and most enterprises are sticking to java8 and are reluctant to use newer versions of java or frameworks other than spring-boot

      - https://www.reddit.com/r/java/comments/11rp29f/jep_draft_8303683_virtual_threads/
      - https://github.com/readme/featured/java-programming-language
      - https://www.jetbrains.com/lp/devecosystem-2020/java/

<br>

- **c#:** not used for systems as often as java is and doesn’t have nice jvm interop

<br>

- **c/cpp:** too difficult to build safe networked systems with - but has the best raw performance

<br>

- **php:** dead

<br>

- **go:** minimalist systems language with easy concurrency and a moderate ecosystem

  created 2009

  good:

  - decent ecosystem, almost as popular as java for distributed systems

  - small native builds, built-in csp model

    designed specifically for distributed systems, microservices and cloud-native apps

    - https://go.dev/doc/faq#What_is_the_purpose_of_the_project
    - https://go.dev/talks/2012/splash.article
    - https://www.reddit.com/r/golang/comments/11c9wv1/why_go/

  bad:

  - can be unergonomic, because of how little syntactic sugar it has, but it does a lot correct right out of the box (ie. error handling)

  - growth seems to stagnate - it doesn’t have anything that could make it stick

  - few jobs but they are well paid because they are reserved for seniors (which makes it difficult to get into)

<br>

- **ruby:** dead

<br>

- **rust:** safe c++ alternative for networked systems, but is lacking the ecosystem

  created 2015

  good:

  - solves a real problem with the ownership model: provides safety without sacrificing performance. this is why microsoft and the linux foundation are porting some of their networking code to it.
  - fastest growing language

  bad:

  - still very new, with a very small ecosystem
  - practically no jobs, most fans are just hobby developers. adoption will still take a couple of years

  - [https://blog.jetbrains.com/rust/2023/01/18/rust-deveco-2022-discover-recent-trends/](https://blog.jetbrains.com/rust/2023/01/18/rust-deveco-2022-discover-recent-trends/#:~:text=The%20share%20of%20developers%20using,2021%20to%2018%25%20in%202022.&text=Florian:%20%E2%80%9CI've%20noticed,professional%20at%20a%20good%20rate)
  - https://www.jetbrains.com/lp/devecosystem-2020/rust/

<br>

- **kotlin:** not a java superset, can't compete with java

  created 2011

  good:

  - null safety, coroutines, native builds

    null safety can be achieved with lombok, java now supports virtual threads, graalvm enables native compilation

  bad:

  - default for android and gradle but still too few jobs - usually kotlin makes up a small part of a java job

  - kotlin is not a superset of java (like typescript to javascript) but a standalone jvm language that is trying to compete with java. it does benefit from sharing the same ecosystem, but so did groovy, clojure, scala (which all failed to gain traction).

    - https://www.reddit.com/r/java/comments/ndwz92/can_i_get_some_reasons_to_use_java_instead_of
    - https://www.quora.com/Is-Kotlin-a-superset-of-Java
    - https://kotlinlang.org/docs/comparison-to-java.html

<br>

- **swift:** mostly for ios development

<br>

- **dart/flutter:** can’t compete with react-native’s ecosystem

<br>

- **lua:** mostly for embedded scripting

<br>

- **scala:** dead
