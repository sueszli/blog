# what does "systems" mean?

when i began grad school at the university of waterloo, one of the most interesting things i noticed was how the labs were grouped by specific research areas.

wanting to specialize in "distributed systems" research, i joined the "systems and networking" (syn) group. however, i was surprised to find that most research in the syn group focused on operating systems, not what i had expected.

at the vienna university of technology (tu wien), we mostly worked with java. our studies were highly focused on distributed systems and internet computing, with very few people engaged in operating systems or low-level research; they had their own department.

in waterloo, it was the opposite. additionally, i discovered that what i wanted to work on wasn't commonly considered "systems" research. i felt confused and began asking people what they believed "systems" research meant, which led me into a rabbit hole.

<br><br>

# the term "systems" is actually ambiguous

a "systems researcher" or "systems engineer" can mean very different things depending on whom you ask.

in academia, according to the [acm classification](https://cran.r-project.org/web/classifications/ACM.html), systems can refer to:

- "computer systems organization": managing loosely coupled computing resources.
- "operating systems": focusing on the kernel.

most often, people refer to the latter.

in the industry, there's a distinction between:

- "distributed systems engineers": these professionals are typically backend web architects/system designers who also code.

  - other job titles: cloud architect, devops engineer, backend developer.
  - responsibilities include task orchestration, distributed computing, data replication, load balancing management, system performance monitoring, and socket programming.

- "systems engineers": managing a company's on-premises infrastructure or working on low-level software close to the os.

  - other job titles: system administrator, network engineer, systems programmer, network administrator.
  - responsibilities include network programming, working on os-level communication, data transfer management, and ensuring network security.

some argue that labeling those who write software for managing distributed systems as "systems engineers" is incorrect.

this has been debated on stack overflow and reddit due to golang being described as a "systems programming language", although it's garbage collected and primarily used for writing web servers:

- https://stackoverflow.com/questions/4106930/what-does-it-mean-by-a-systems-language
- https://www.reddit.com/r/golang/comments/73pe61/what_does_this_author_mean_by_golang_is_a_systems/

again: the term "systems" is ambiguous. identifying as a "systems" researcher while writing web backends (or even frontends) might be annoying to some, but it's technically not incorrect.

it's important to determine the specific type of systems research that interests you, understand the career prospects (having an industry backup plan if aiming for an academic position), and know the job's nature before starting your research.

<br><br>

# what is "distributed systems research"?

distributed systems research is the study of how to make many computers work together over a network. the main goal is to create systems that can handle more work by adding more computers, instead of making each computer faster. this is called horizontal scaling.

distributed systems have many challenges, such as how to coordinate the actions of different computers, how to deal with failures and errors, how to keep the data consistent and secure, and how to measure and improve the performance. systems researchers try to find solutions to these challenges by designing new algorithms, data structures, components, and architectures.

some examples of topics in distributed systems research are:

- algorithms and data structures:

  these are the rules and methods that computers use to communicate, agree, and store data in a distributed system.

  some popular examples include: consensus algorithms (paxos, raft), gossiping/flooding algorithms, leader election, global averaging, ntp etc., key value stores, distributed hash tables.

- software design / software architectures:

  some examples of distributed system architectures are: client-server, peer-to-peer, leader-follower, and hybrid architectures.

  designing a distributed system involves choosing the building blocks and patterns that make up a distributed system, like: message brokers, service discovery, load balancing, and caching services.

  designing p2p systems used to be very popular in the 2000s but is now experiencing a resurgence due to the rise of blockchain technology and more local-first software. although controversial, there are still many interesting uses in this area about self-organizing systems:

  - mobile mesh networks: these enable the formation of delay-tolerant, mobile networks for blackout resistance, network resilience, and wider coverage.
  - decentralized social networks: platforms like mastodon, diaspora, bluesky, minds, peepeth.
  - decentralized file storage systems: ipfs/filecoin, sia.

these are just a few examples of distributed systems research and it's hard to give a complete overview of the field.
