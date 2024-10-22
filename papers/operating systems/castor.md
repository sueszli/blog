> Mashtizadeh, Ali José, et al. "Towards practical default-on multi-core record/replay." ACM SIGPLAN Notices 52.4 (2017): 693-708.

# castor

low overhead (2-10%) record/replay for multi-core apps.

used for replay-debugging.

> shared memory non-determinism is a key challenge to multicore record/replay. systems have coped in two ways. some reproduce all data races precisely. others like castor only record and replay explicit synchronization.

_1) recording unmodified applications (interposing at the compiler level)_

- a custom compiler pass can avoid the need for manual instrumentation.
- records language-level events by using the 'clang/llvm compiler pass' - so no source-code modification needed.
- the compiler pass was also used to benchmark the system.
- inter-thread shared-memory non-deterministic events: system calls, synchronization with volatile variables, atomics, ad hoc synchronization.
     - a) input-non-determinism
          - = input changes over a network.
          - we record events in the log.
     - b) ordering non-determinism
          - = operation order changes which leads to the program behaving differently.
          - we record events and the global ‘timestamp counter’ (tsc) in the log.

_2) data races have negligible impact on replay_

- castor cannot replay data-races like they occured - but it doesn’t matter.
- data-races are shared memory access that isn’t synchronized.
- programs today don’t support 'benign data races' for performance gains. instead we use 'relaxed-memory-order' atomics.

_3) low overhead through hardware optimized logging_

- makes always-on recording possible.
- ‘transactional memory’ and timestamp counter’ (tsc) for contention-free logging with a low tail-latency.
- incremental log sorting to keep end-to-end latency (time until replay after record / how far the replica is lagging behind) based on a timestamp for the event creation. the os often yields control from thread before it can add its log into its queue so we force the commit to the queue to be atomic.
- seperate queue per core so it scales with number of cores.
- based on what mode the program is in, the ring buffers have different sizes.

## record mode

the `record` command runs app in record mode.

- self contained mode: no external dependencies, everything is logged.
- passthrough mode: just the initial filesystem is captured with ZFS snapshots.

starts recording agent.

each application thread writes log entries in their own ring-buffer / fifo queue in the shared memory.

entres are the size of L1/L2 cache lines.

`head` and `tail` of ring-buffer have their own dedicated space.

recording agent drains buffers, logs, orders events and writes everything to disk or a network.

_record modes:_

- **a) fault tolerance**

     - short ring buffers, dedicated core which constantly polls and checks whether all data can fit in the L1/L2 cache. logs get sorted online.

- **b) debugging and analysis**

     - bigger ring buffers, recording agent sleeps when there aren’t too many events. logs get sorted offline.

- **c) crash recording**

     - huge ring buffers, no recording agent, no draining of logs. when the logs fill up a checkpoint gets set and everything gets flushed into the disk asynchronously.

## replay mode

the `replay` command runs app in record mode.

starts replaying agent.

log entries get placed back into each threads buffer and get consumed.

_replay modes:_

- a) totally ordered replay

     - events sorted by their event id, get executed in parallel based on a global counter.

- b) partially ordered replay

     - replay agent infers which events are dependent of eachother and executes them based off of that.

_divergence detection:_

when replayed execution differs from the recorded execution so much that continuing the replay is either not possible or dangerous.

- event divergence: next log event doesn’t make sense to thread.
- deadlock divergence: threads lock up during replay because a lock is missing somewhere.
- argument divergence: checksum doesn’t match with argument so the data is corrupted.

when data-races occur, they can be problematic in 3 different ways:

- log divergence: log doesn’t make sense.
- output divergence: user visible results don’t make sense (treated just like log divergence in castor).
- value divergence: intermediate values in calculations don’t make sense.
