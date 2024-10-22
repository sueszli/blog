> Dragojević, Aleksandar, et al. "{FaRM}: Fast remote memory." 11th USENIX Symposium on Networked Systems Design and Implementation (NSDI 14). 2014.

# farm

other sources:

- https://www.youtube.com/watch?v=UoL3FGcDsE4&t=1195s&ab_channel=USENIX
- https://www.microsoft.com/en-us/research/wp-content/uploads/2014/02/aleksandar-dragojevic.pdf
- https://www.usenix.org/sites/default/files/conference/protected-files/nsdi14_slides_dragojevic.pdf

# prelude

_introduction_

1. single cpus can’t keep up

      “[…] in the future as request rates go up we expect to become cpu bottlenecked”

      horizontal scaling / distributed computing is necessary

2. main memory is getting cheaper

      DRAM got cheap, can store entire dataset of most applications.

      100GB-1TB / server

      10-100TB / cluster

3. TCP/IP networking stack will be the next bottleneck

      the TCP networking stack has become the bottleneck of the request processing.

      farm suggests RDMA as an alternative

_why rdma_

1. reliable

      Requests are sent over reliable connections called “queue pairs”. Network failures are exposed as a terminated connection.

2. fast

      RDMA to improve both latency and throughput much higher than traditional TCP/IP systems.

      100 Gbps throughput

      1-3 µs latency

      it bypasses the kernel and remote cpu for remote read/write operatings.

      Avoids the overheads of protocol stacks.

      Everything happens in user-level.

3. affordable

      RoCE (RDMA over Converged Ethernet) hardware supports RDMA over Ethernet with data center bridging extensions that are widely available.

      RDMA became accessible thorugh ethernet cables only (not just “infiniband”).

_rdma explained_

- NICs perform RDMA requests.
- it bypasses the kernel and remote cpu for remote read/write operatings.
- Avoids the overheads of protocol stacks.

steps (keep in mind: most NICs guarantee that writes are commited in an increasing access order):

1. server NIC registers “memory regions” in NIC page table: virtual/physical-page mappings
2. “memory region” capability sent to clients
3. server receives RDMA request with “memory region” and offset
4. server reads memory with DMA and executes operation in a cache coherent way

_rdma vs. tcp benchmark_

20 machines, random read, RoCE networks, optimized NICs:

1. rdma with direct reads (2x)
2. rdma with rpc (2x)
3. tcp/ip with rpc

_remarks:_

- we don’t talk about UDP:

     it is half as fast as TCP in these systems

- local memory is still up to 23x faster than RDMA

     “spacial locality / locality awayre optimizations”

     “function shipping”: sending instructions to be executed as close to data as possible.

# introduction

> Aleksandar: “Farm is […] a [main memory] distributed computing platform for modern data center hardware”

_programming model / API_

- it provides: synchronization, shared address space, communication.

     ```c
     // transaction
     Tx*  txCreate(); // starts transaction, returns context
     void txAlloc(Tx *t, int size, Addr a, Cont *c);
     void txFree(Tx *t, Addr a, Cont *c);
     void txRead(Tx *t, Addr a, int size, Cont *c);
     void txWrite(Tx *t, ObjBuf *old, ObjBuf *new);
     void txCommit(Tx *t, Cont *c);

     // lock free distributed transactions
     Lf*  lockFreeStart();
     void lockFreeRead(Lf* op, Addr a, int size,Cont *c);
     void lockFreeEnd(Lf *op);

     Incarnation objGetIncarnation(ObjBuf *o);
     void objIncrementIncarnation(ObjBuf *o);

     // rdma based messaging
     void msgRegisterHandler(MsgId i, Cont *c);
     void msgSend(Addr a, MsgId i, Msg *m, Cont *c);
     ```

- `Cont*` (continuation):

     consists of the “context pointer” and the “continuation function” which gets called by thread that initiated the operation, after it completed - also passes results of context pointer to callback.

- locality:

     can be improved for allocations by passing a “hint” (existing object’s address).

     farm attemtps to store objects in the same machine (even after recovery)

_applications_

- it’s made for performance / latency sensitive applications like:

     Graph processing

     Scale-out OLTP (online transaction processing)

     Deep neural networks

     Distributed databases

- we used FaRM to build a key-value store and a graph store similar to Facebook’s.
- they both perform well, for example, a 20-machine cluster can perform 167 million key-value lookups per second with a latency of 31µs.

# memory sharing

_shared memory abstractions_

1. partitioned global address space PGAS / shared address space

      the entire cluster memory is shared.

      convenient for programming:

      necessary for efficient rdma: for read/write operations you need the transfer starting address + size.

      shared address space consists of 2gb “regions”, identified by 32bit with 32bit offsets relative to the start of the region.

      because were using distributed hashtables, regions are actually virtual rings.

      each machine is mapped into **k** virtual rings by hashing its IP address with **k** hash functions.

      cluster members are managed with zookeeper

      memory allocations are very granular (from 64byte to 1MB):

      - slabs — slab allocators, for threads
      - blocks — blocks from the shared memory, for individual machines
      - regions — entire regions, for whole clusters
        PhyCo allocates region and registers it with NIC

2. distributed transactions

      what can applications do in this shared address space?

      transactions = atomic execution of multiple operations (operations: allocate, read, write, and free objects)

      properties of transactions:

      - ACID transactions

           atomicity = either everything happens or nothing does

           consistency = data is in a valid state

           isolation = concurrency doesn’t cause side effects

           durability = writes are permanent

      - fault tolerance

           logging and recovery in main memory (on SSDs / non volatile ram) similary to RAMCloud

           allow transparency: location, concurrency, failures

      - strict serializability

           = system makes sure that all actions look like they happened one after another

      - optimistic concurrency control

           = writes are buffered and only written at commit time, at which conflicts are fixed

      - two-phase commit protocol (with RDMA-based messaging)

           phase 1: locks set, coordinator sends broadcast to check

           phase 2: coordinator receives response, everyone agreed, operation validated, operation commited, set gets unlocked

_lock-free reads_

- = atomic execution of a single read
- can be performed with a single RDMA.
- are strictly serializable with transactions, and support for collocating objects.
- consistent even if concurrent write operation is happening.

- a) traditional lock free read implementation (single machine)

     version: 64bit counter in header to detect inconsistencies

     - write: locks everything, updates data, increment counter, unlock everything
     - read: read version, read data, read version again (must be equal to first read or operation gets redone) → we have 3 network accesses for each read, which is too slow to make sense for rdma

- b) farm lock free read implementation

     NICs observe changes on cache lines.

     version: 16bit for more space efficiency, we only need to be consistent during the read and track time.

     - write: lock all cache lines, update, increment counter, unlock everything

          (everything done locally, versions of multiple cache lines can be checked with a single rdma)

     - read: single rdma read, check versions match and read doesn’t take too long

          we track time

          _t-update-min = 40ns_

          _t-read-max = 40ns _ 2^16 _ (1 - epsilon) = 2ms_

# optimizations

_locality awareness_

- local memory is still up to 23x faster than RDMA
- “spacial locality / locality awayre optimizations”
- “function shipping”: sending instructions to be executed as close to data as possible.

_phyCo_

- problem:

     larger registered memory for remote access = worse memory

     this is because NIC was running out of space to cache all page tables.

     large page support in windows and linux was too small.

- goal:

     larger pages for fewer entries in NIC page tables.

- solution:

     a kernel driver that allocates a large number of physically-contiguous and naturally-aligned 2 GB memory regions at boot time (2 GB is the maximum page size supported by our NICs).

     this allowed to modify the NIC driver to use 2 GB pages.

     reduced the number of page table entries per region from >0.5 million to 1.

_connection multiplexing_

- number of necessary queue pairs:

     queue pairs per machine = 2 × m (number of machines) × t^2 (because of 2 queues per thread on each machine)

- using a single queue pairs:

     queue pairs per machine = 2 × m × t

- sharing queue pairs among **q** threads in NUMA-aware way:

     queue pairs per machine = 2 × m × t / q

     this trades off parallelism for a reduction in the amount of queue pair data on the NIC.

- you have to find the perfect balance between cluster size, paralleism, num of queue pairs (see graph).

- we expect to solve this problem in the future by using “Dynamically Connected Transport”, which sets up connections on demand.
