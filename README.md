# Cache Management System
## Overview
This Python script, authored by Mehrnaz Miri, implements a cache management system using two different algorithms: FIFO (First In, First Out) and LFU (Least Frequently Used). The system allows users to input requests and choose between these two algorithms for cache management.

## Usage
1. Run the script.
2. Input integers representing user requests. Enter 0 to indicate the end of input.
3. Choose from the following options:
   1.  Enter 1 for FIFO.
   2.  Enter 2 for LFU.
   3. Enter Q to exit the program.

## Algorithms
- **FIFO (First In, First Out)**

In FIFO, the cache operates on a principle where the oldest entered requests are removed first when the cache is full. If a requested page is not in the cache, it is added to the cache. Otherwise, it is considered a cache hit.

- **LFU (Least Frequently Used)**

In LFU, the cache keeps track of how frequently each page is accessed. When the cache is full and a new page is requested, the least frequently used page is replaced. If a requested page is not in the cache, it is added to the cache. Otherwise, it is considered a cache hit.

## Notes
The cache size is not explicitly defined in the script and is assumed to be dynamic.

The script only displays the last 8 requests in the cache for FIFO. This behavior can be modified as needed.

The LFU algorithm's implementation might need adjustments for more accurate frequency tracking, depending on the specific requirements.
