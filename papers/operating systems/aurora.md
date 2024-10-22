> Tsalapatis, Emil, et al. "The Aurora operating system: revisiting the single level store." Proceedings of the Workshop on Hot Topics in Operating Systems. 2021.

_single level storage (SLS) systems_

- applications solely use the memory and the operating system persists this state to disk.
- developers design programs as if they never crash and thus do not write code for persistence and recovery.
- after a crash, the SLS restores the application, including all state (i.e., CPU registers, OS state, and memory), which continues executing oblivious to the interruption.
- this way the manipulation and persistence of apps are managed by the OS.

_aurora_

1. fast checkpoints:

      possible because of hardware improvements like modern flash, coupled with fast PCIe Gen 4, large virtual address spaces.

2. simple persistence:

      supports both unmodified and modified POSIX applications.

      all POSIX primitives are first class objects: ie, Unix domain sockets, System V shared memory, and file descriptors.
