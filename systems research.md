# what is systems research?

i like to build. so naturally, i'm interested in systems of all kinds.

people who work on systems are often referred to as "systems people", as in a "systems researcher" or a "systems engineer" – but what does that actually mean?

- https://stackoverflow.com/questions/4106930/what-does-it-mean-by-a-systems-language
- https://www.reddit.com/r/golang/comments/73pe61/what_does_this_author_mean_by_golang_is_a_systems

this confusion on social media is justified.

there's a lot more to it than you might think. the term "systems" is ambiguous and the meaning always depends on which context it's used in.

## classification

it's very hard to classify the entirety of computer science research. some good starting points are the [acm research classification](https://cran.r-project.org/web/classifications/ACM.html) the [arxiv taxonomy](https://arxiv.org/category_taxonomy) and the [csrankings](http://csrankings.org/) website.

i personally like the arxiv taxonomy and the csranking classification the most. here's how i would combine them:

- data

     - cs.AI (Artificial Intelligence)
     - cs.CE (Computational Engineering, Finance, and Science)
     - cs.CV (Computer Vision and Pattern Recognition)
     - cs.DB (Databases)
     - cs.MA (Multiagent Systems)
     - cs.LG (Machine Learning)
     - cs.DL (Digital Libraries)
     - cs.IR (Information Retrieval)
     - cs.NE (Neural and Evolutionary Computing)

- systems

     - cs.SE (Software Engineering)
     - cs.NI (Networking and Internet Architecture)
     - cs.DC (Distributed, Parallel, and Cluster Computing)
     - cs.PF (Performance)
     - cs.AR (Hardware Architecture)
     - cs.OS (Operating Systems)

- security

     - cs.CR (Cryptography and Security)

- theory

     - cs.CC (Computational Complexity)
     - cs.CG (Computational Geometry)
     - cs.CL (Computation and Language)
     - cs.PL (Programming Languages)
     - cs.SY (Systems and Control)
     - cs.IT (Information Theory)
     - cs.DM (Discrete Mathematics)
     - cs.DS (Data Structures and Algorithms)
     - cs.NA (Numerical Analysis)
     - cs.GT (Computer Science and Game Theory)
     - cs.FL (Formal Languages and Automata Theory)
     - cs.MS (Mathematical Software)
     - cs.LO (Logic in Computer Science)
     - cs.SC (Symbolic Computation)

- graphics and hci

     - cs.GR (Graphics)
     - cs.MM (Multimedia)
     - cs.HC (Human-Computer Interaction)
     - cs.SD (Sound)

- interdisciplinary areas

     - cs.GL (General Literature)
     - cs.OH (Other Computer Science)
     - cs.CY (Computers and Society)
     - cs.SI (Social and Information Networks)
     - cs.ET (Emerging Technologies)
     - cs.RO (Robotics)

## conclusion

in short: a system is the sum of its primitives.

these primitives can be anything ranging from people (social networks), intelligent agents (multiagent systems), autonomous vehicles (robotics), to software modules, services or entire hardware components.

you could argue that anyone working on any of these primitives could be considered a "systems person".

but effectively, the term "systems" is used to refer to the following:

- cs.SE (Software Engineering)

     - question: how do we write code at scale?
     - research topics: tools, software metrics, testing and debugging, programming environments

- cs.NI (Networking and Internet Architecture) + cs.DC (Distributed, Parallel, and Cluster Computing)

     - question: how do we make computers collaborate?
     - research topics: network protocols and architectures, network security, web backend architectures, distributed computing, parallel computing, cluster computing, cloud computing

- cs.AR (Hardware Architecture) +  cs.OS (Operating Systems)

     - question: how can we make things from the real world interact with software?
     - research topics: hardware design, embedded systems, operating systems, internet of things, robotics

but even within these categories, there's a lot to unpack as they are covering a wide range of abstraction levels.

and even people within the same lab could be working on completely different things.

- as a distributed systems researcher you could be writing formal proofs in TLA+ or Coq to create a new distributed consensus algorithm, extending the kernel for faster RDMA access, sniffing packets to find vulnerabilities in network protocols, or writing a new load balancer for a web backend that implements machine learning to optimize resource allocation.

- the same applies to kernel researchers: while one could be hardening the kernel against power side-channel and physical memory attacks, the other could be working on fault tolerant network protocols for space exploration.

as you can see, the only thing these people have in common are the journals and conferences they publish in.
