Understanding Algorithm Efficiency and Scalability

Overview

This project demonstrates the implementation and analysis of two
fundamental algorithms — Randomized Quicksort and Hashing with Chaining.
It compares their efficiency and scalability through both theoretical
and empirical testing.

------------------------------------------------------------------------

How to Run the Code

1. Run the Quicksort Demo

    python quicksort.py

Displays sorted outputs using both Randomized and Deterministic
Quicksort.

2. Run Performance Benchmarks

    python benchmark_quicksort.py

Compares runtime of both algorithms and generates: -
quicksort_results.csv — benchmark data - quicksort_random_median.png —
visualization chart

3. Run Hash Table Tests

    python tests_hash_table.py

Expected output:

    All hash table tests passed.

------------------------------------------------------------------------

Summary of Findings

-   Randomized Quicksort maintained O(n log n) performance on all data
    distributions.
-   Deterministic Quicksort slowed drastically on sorted and
    reverse-sorted arrays due to poor pivot choices.
-   Hashing with Chaining maintained O(1) average operation time thanks
    to dynamic resizing and uniform hashing.

------------------------------------------------------------------------

Files in This Project

  ------------------------------------------------------------------------------------------------------------------------------
  File                                                                         Description
  ---------------------------------------------------------------------------- -------------------------------------------------
  quicksort.py                                                                 Implements both sorting algorithms

  benchmark_quicksort.py                                                       Measures and compares sorting performance

  hash_table_chaining.py                                                       Implements hash table using chaining

  tests_hash_table.py                                                          Tests hash table operations

  quicksort_results.csv                                                        Benchmark data results

  quicksort_random_median.png                                                  Performance visualization

  report 						                       Final report
  ------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------


