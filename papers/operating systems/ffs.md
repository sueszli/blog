> McKusick, Marshall K., et al. "A fast file system for UNIX." ACM Transactions on Computer Systems (TOCS) 2.3 (1984): 181-197.

# ffs

“a fast file system for unix”: alternative implementation of the unix file system (ufs) with better performance.

other sources:

- implementation: https://github.com/openbsd/src/blob/master/sys/ufs/ffs/fs.h
- https://github.com/openbsd/src/blob/master/sys/ufs/ffs/fs.h
- https://gunkies.org/wiki/BSD_Fast_File_System
- https://slideplayer.com/slide/9894780/
- https://blog.koehntopp.info/2023/05/06/50-years-in-filesystems-1984.html
- https://www.youtube.com/watch?v=1BbMBdGPoHM
- https://en.m.wikipedia.org/wiki/Marshall_Kirk_McKusick
- http://www.cse.unsw.edu.au/~cs9242/02/lectures/09-fs/node4.html

# introduction

_unix operating system_

- the os is the intermediary software layer between programs and the computer hardware that manages resources like memory, cpu etc.
- unix is a family of operating systems.
- what’s special about unix is that “everything is a file(descriptor)” - even interprocess communication and peripheral access.

_fs / file system_

- data structure that the operating system uses to control how data is stored and retrieved from a storage device.
- the storage device can be: SSDs, magnetic tapes, optical discs, tmpfs, main memory/RAM as a temporary file system, remote/virtual file
- SDDs were invented in 1989 and became commercially available in 1991

_fs architecture_

usually 2 or 3 layers, often combined:

- logical file system: has API for file operations like `OPEN`, `CLOSE`, `READ`, etc. and manages file descriptors.
- virtual file system: allows multiple instances of the physical file system to be used concurrently.
- physical file system: processes physical operations on blocks of the storage device (ie. disk). interacts with the device drivers.

_addresses on a hard disk drive: CHS_

- see: https://en.m.wikipedia.org/wiki/Cylinder-head-sector
- addresses of each physical data-block on a hard disk drive

```txt
// hierarchy of a file system

disk drive
	multiple disk drive partitions
		a single file system
			files (directories are special files)
				inode / file decriptor
					data blocks
```

_disk drive_

- physical space that stores file-systems
- is partitioned into disk-partitions

_file system_

- logical system which contains files
- directories are also just files, that point to other files
- every file has an associated file-descriptor called ‘inode’

_inodes (block index node)_

- see: https://en.m.wikipedia.org/wiki/Inode_pointer_structure
- link to all data-blocks for that file (and other things like file ownership, last mod timestap, access times)
- we assume that the first 8 data-blocks of each file are reserved for the inode itself (actually somewhere between 5-13)
- inodes may reference ‘indirect blocks’ that contain other block indixes

_data-blocks_

- actual data located on the physical disk (which can also store addresses to other disk blocks)

_super block_

- very critical, describes the file system
- placed in the beginning of each partitionn
- immutable data like: num of data blocks in fs, max num files

# ufs vs. ffs comparison

### // ufs

_disk partitions_

- subdivision of physical space on a disk drive that doesn’t overlap
- can store max 1 file-system

_file-system_

- starts with super-block

_inode_

- each indirect level (no matter at what depth) can hold 128 indirect-block-addresses

_data-blocks_

- each have 512 bytes

_super block_

- also stores pointer to the ‘free list’ (linked list of all free blocks in the system)

### // ffs

_disk partitions_

- logical disk partitions, file-systems can span multiple partitions
- is divided into ‘cylinder groups’ which are consecutive on the disk

_cylinder-groups_

- each contain ‘bookkeeping’:

     - redundant super-block copy
     - static number of inodes (usually 1 inode for each 2048 bytes in cylinder group for extra redundancy)
     - bitmap describing available space in group (this replaces the old ‘free list’)
     - space usage within cylinder group

- the bookkeeping data isn’t placed at the top of the platter because that’s the place most likely to get damaged — a sequentially increasing offset is used (the blocks spiral from the outside into the center)
- the remaining space is used for data blocks.

_file-system_

- starts with super-block as well but it’s replicated during file-system creation to protect against corruption and catastrophic loss
- replicas are only accessed when corruption is detected
- must be min 4096 bytes large if files are max 2^32 bytes to limit max 2 levels of indirection

# ufs

original 512 byte system, introduced with 4.2 BSD, developed by bell labs.

_why ufs had to be improved_

- low reliability because there was just one copy of the super block
- low throughput that doesn’t suffice for applications or mapping files into virtual address spaces
- provides ~2% of the maximum disk bandwidth
- ~20kb/s per arm: very long seek times because of low locality

     150mb ufs had 4mb of inodes followed by 146mb of data

     inodes of files in same directory weren’t placed close to eachother

     data blocks of the same file weren’t placed on the same cylinder (max 512 bytes per disk transaction):

     - limited read-ahead
     - small block size
     - seek for every 512 byte

_initial optimization: 2x basic block size (from 512b to 1024b)_

- 2x more throughput, +2% disk bandwitdth usage
     - each disk transfer accessed twice as much data leading to the need of less indirect blocks
- degradation
     - because ‘free list’ allocation and block placement was random transfer rates went from 157kb/s down to 30kb/s in a few weeks
     - the only way to restore performance was to dump, rebuild, restore entire fs or run a process that reorders allocations.

# ffs

used in FreeBSD, NetBSD, OpenBSD, NeXTStep, Solaris

## fragments

_fragments to avoid fragmentation_

- bigger data-blocks lead to more waste
- if we pick 4096b data-blocks instead of 1024b, we save 4 transactions
     - but bigger blocks are not always better: most unix systems store many small files
     - based on experience this leads to wasted space (no user data) on blocks
- we split data-blocks into smaller parts called fragments
- fragment size (2,4,8) is specified when file system is created and must be >512b

_NFS: fragment storage allocation_

- ‘blockmap’ in each each cylinder group also records available space at fragment level
  example: 4096 block size / 1024 fragment size:

     - X = fragment is in use
     - O = fragment is free
     - fragments of adjoining blocks cannot be used as a full block, but fragments in the same block (like 0-3) could be merged into a full block.

- creating file: if we don’t find all the fragments we just take another full block and return a single fragment.
- appending file:

     a) enough space in current block, just extend

     b) no space in remaining fragments - move parts to whole new block, repeat recursively

     this can lead to a lot of reallocations and be pretty slow

## free space reserve parameter

_free space reserve_

- performance degrades by overfilling the system
- layout policy has the parameter called “free space reserve” that avoids 100% utilization so throughput is good (less time searching for free blocks).
- the parameter can be changed any time.
- based on experience:
     - waste ufs 1024b = 11.8%
     - waste ffs 4096b/512b with ‘free space reserve’ set at 5% = 6.9% + 5%

## layout policies

_layout policies_

1. global policy routines

      fs wide summary information

      place inodes, data-blocks

      calculate rotationally optimal placements for files and directories

      decide when it’s worth it to switch cylinders and sacrifice locality

      ideally none of the cylinder groups should ever become completely full

2. local allocation routines

      layout policy

      based on inodes we can tell which files are in the same directory

      locally optimal scheme to lay out data blocks

      - put inodes (if files are in the same directory) in the same cylinder-group
      - put new directory inodes in cylinder-groups that are relatively empty
      - put all data-blocks for the same file in the same cylinder-group at ‘rotationally optimal positions’ (after calculating these)

           ‘rotationally optimal blocks’ are either consecutive or rotationally delayed and are ideal for systems that don’t need processor intervention between multiple data transfers.

           super-block contains a vector of lists called ‘rotational layout table’ to know how disk sectors are placed

      4 level allocation strategy:

      1. use next available block which is rotationally closest to requested block
      2. else use blocks within the same cylinder-group
      3. else use the quadratic hash of the cylinder-group-number to repeat
      4. else search linearly

## parameterization

_parameterization_

- ffs adapts itself to underlying hardware (processor speed, storage transfer speeds, number of blocks per track, disk spin rate, …) for optimal allocation
- ffs tries to allocate new blocks on the same cylinder as the previous block for the same file.

# benchmarking

based on empirical studies

test programs measure rate at which user programs can transfer data to or from a file without performing any processing on it.

data must be large enough that OS buffering doesn’t affect results.

tests ran 3x consecutively.

10% free space reserve (with 0% the results are half as good).

(disk) bandwidth is given per filesystem.

no degradation: throughput stays high over longer timeperiods

speedup: 2x less disk accesses for inode seeks (close to 8x for large flat directories)

the larger block size contributes most to the speedup.

there is some slowdown because of block (re)allocation.

but net cost for each byte allocated is the same for ufs and ffs.

writes are slower because kernel must do some work.

throughput / bandwidth usage could also be improved by:

- aligning address spaces:

     slow memory-to-memory operations: disk buffer → systems address space → data buffers in users address space

     this could be mitigated by aligning the address spaces but it was too complex for this OS.

- preallocating multiple blocks / batch allocating (used in DEMOS fs) when a file is growing fast and then releasing the unused fragments

     not included because it only makes up 10% of write calls and the current rates are limited by the number of available processors

- chaining together kernel operations to read multiple blocks in a single transaction by taking into consideration how many blocks are skipped while processing data

     this could push the bandwidth usage above 50%

# final result

higher throughput rates

more flexible allocation policies (bigger blocks for bigger files, smaller blocks for smaller files)

clusters data that is accessed sequentially

10x faster file access rate than traditional unix fs

some functional enhancements that i don’t care about (better api, lock mechanisms, improved namespace)

_key takeaways_

> “The global policies try to balance the two conflicting goals of localizing data that is concurrently accessed while spreading out unrelated data.”

- “increase the locality of reference to minimize seek latency [… but don’t take it to the extreme or it leads to] a single huge cluster of data resembling the old file system”
- “[cluster related information, ] but […] also try to spread unrelated data among different cylinder groups”
- “improve the layout of data to make larger transfers possible”
- improve granularity of allocs, but also merge blocks together where necessary
  in general: large data-blocks in the same cylinder lead to spill-overs of smaller ones
- add redundancy for resilience
