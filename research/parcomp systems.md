> “Processor Architecture and Technology Trends” from the book: T. Rauber and G. Rünger. Parallel Programming - for Multicore and Cluster Systems, Third Edition. Springer, 2023. isbn: 978-3-031-28923-1. → Section 2.1

chapter 2.1 (processor architecture and technology trends) discusses processor architecture and technology trends, focusing on how these trends have influenced the performance of computer systems. 

the chapter highlights two main factors that have historically contributed to performance increases: clock frequency and the number of transistors on a chip. 

- **clock frequency** is the number of cycles per second a processor can execute and is measured in hertz (hz).  earlier, between 1987 and 2003, there was a significant annual increase in clock frequency. however, this trend has slowed down since 2003 due to limitations in cooling technology. an increase in clock frequency leads to higher power consumption, mainly due to leakage currents that generate heat. efficient cooling is required to manage this heat, and current technology cannot handle processors with a significantly higher clock rate without extra effort.

- **transistor count** refers to the number of transistors on a processor chip, which can be used as a rough estimate of its complexity and performance. moore's law states that the number of transistors on a chip doubles roughly every 18 to 24 months. while the rate of increase has slowed down in recent years, the number of transistors continues to grow. this increase in transistors has been used to improve processor architecture in various ways, including adding more functional units, larger caches, and more registers.

the chapter also details four phases of microprocessor design trends, all driven by internal parallelism:

1. **parallelism at bit-level:** this refers to the increase in word size used by processors for operations, which went from 4 bits to 32 bits and eventually to 64 bits by the early 1990s. this trend was driven by the need for higher floating-point accuracy and a larger address space.

2. **pipeline parallelism:** this technique overlaps the execution of multiple instructions by dividing the execution process into stages (ie. MIPS). each instruction goes through these stages one after another in an assembly line fashion. if there are no dependencies between instructions, this allows for a higher throughput of instructions executed per unit time.

3. **parallelism by multiple functional units:** modern processors are often multiple-issue processors, meaning they can execute multiple instructions simultaneously using independent functional units like alus (arithmetic logical unit), fpus (floating-point unit), load/store units, or branch units. this approach is also known as instruction-level parallelism (ilp).

4. **parallelism at process or thread level:** this technique utilizes multiple cores on a single processor chip, each with its own control flow. this requires parallel programming techniques to manage the separate flows . the cores can access the same memory and potentially share caches, necessitating coordination and synchronization techniques which are covered in later chapters of the book.
