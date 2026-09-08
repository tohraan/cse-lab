# cse-lab

![tests](https://github.com/tohraan/cse-lab/actions/workflows/ci.yml/badge.svg)

Data structures, algorithms and systems building blocks in plain Python.
Every problem is built the same way: sketch the API, write the tests, implement, document the complexity.

```bash
pip install pytest
pytest -q
```

## Problems (30)

| # | Problem | Topic | Difficulty | Complexity |
|---|---------|-------|------------|------------|
| 1 | [Two Sum](cselab/two_sum.py) | Hashing | Easy | O(n) time, O(n) space |
| 2 | [Valid Parentheses](cselab/valid_parentheses.py) | Stack | Easy | O(n) time, O(n) space |
| 3 | [Merge Intervals](cselab/merge_intervals.py) | Sorting | Medium | O(n log n) time, O(n) space |
| 4 | [Binary Search & Lower Bound](cselab/binary_search.py) | Searching | Easy | O(log n) time, O(1) space |
| 5 | [Reverse a Linked List](cselab/reverse_linked_list.py) | Linked List | Easy | O(n) time, O(1) space |
| 6 | [Maximum Subarray (Kadane)](cselab/max_subarray.py) | Dynamic Programming | Medium | O(n) time, O(1) space |
| 7 | [Climbing Stairs](cselab/climbing_stairs.py) | Dynamic Programming | Easy | O(n) time, O(1) space |
| 8 | [Coin Change](cselab/coin_change.py) | Dynamic Programming | Medium | O(amount * coins) time, O(amount) space |
| 9 | [LRU Cache](cselab/lru_cache.py) | Design | Medium | O(1) get/put, O(capacity) space |
| 10 | [Min Stack](cselab/min_stack.py) | Design | Medium | O(1) per operation |
| 11 | [Trie (Prefix Tree)](cselab/trie.py) | Trees | Medium | O(L) per operation |
| 12 | [Union-Find (DSU)](cselab/union_find.py) | Graphs | Medium | ~O(alpha(n)) per operation |
| 13 | [Topological Sort (Kahn)](cselab/topological_sort.py) | Graphs | Medium | O(V + E) time and space |
| 14 | [Dijkstra Shortest Paths](cselab/dijkstra.py) | Graphs | Medium | O((V + E) log V) time |
| 15 | [Shortest Path in a Grid (BFS)](cselab/bfs_grid.py) | Graphs | Medium | O(rows * cols) time and space |
| 16 | [Number of Islands](cselab/number_of_islands.py) | Graphs | Medium | O(rows * cols) time and space |
| 17 | [Longest Common Subsequence](cselab/lcs.py) | Dynamic Programming | Medium | O(m * n) time, O(n) space |
| 18 | [Edit Distance (Levenshtein)](cselab/edit_distance.py) | Dynamic Programming | Hard | O(m * n) time, O(n) space |
| 19 | [0/1 Knapsack](cselab/knapsack.py) | Dynamic Programming | Medium | O(n * W) time, O(W) space |
| 20 | [Merge Sort](cselab/merge_sort.py) | Sorting | Medium | O(n log n) time, O(n) space |
| 21 | [Kth Largest Element](cselab/kth_largest.py) | Heap | Medium | O(n log k) time, O(k) space |
| 22 | [Top K Frequent Elements](cselab/top_k_frequent.py) | Hashing | Medium | O(n) time with bucket sort |
| 23 | [Valid Anagram](cselab/valid_anagram.py) | Hashing | Easy | O(n) time, O(1) space |
| 24 | [Longest Substring Without Repeats](cselab/longest_unique_substring.py) | Sliding Window | Medium | O(n) time, O(k) space |
| 25 | [3Sum](cselab/three_sum.py) | Two Pointers | Medium | O(n^2) time, O(1) extra space |
| 26 | [Container With Most Water](cselab/container_most_water.py) | Two Pointers | Medium | O(n) time, O(1) space |
| 27 | [Rotate Image](cselab/rotate_matrix.py) | Matrix | Medium | O(n^2) time, O(1) space |
| 28 | [Spiral Matrix](cselab/spiral_order.py) | Matrix | Medium | O(m * n) time |
| 29 | [Permutations](cselab/permutations.py) | Backtracking | Medium | O(n * n!) time |
| 30 | [Subsets](cselab/subsets.py) | Backtracking | Medium | O(n * 2^n) time |

## How this repo is built

Problems are released in small commits (`tools/stages.py`). A daily workflow
(`.github/workflows/drip.yml`) releases the next batch until the bank in
`tools/problems.py` runs out. The first commits were backfilled with
`tools/build_history.py`, so their dates are planned, not the day the code was
first typed. Everything after the backfill carries its real date.
