# cse-lab

![tests](https://github.com/tohraan/cse-lab/actions/workflows/ci.yml/badge.svg)

Data structures, algorithms and systems building blocks in plain Python.
Every problem is built the same way: sketch the API, write the tests, implement, document the complexity.

```bash
pip install pytest
pytest -q
```

## Problems (3)

| # | Problem | Topic | Difficulty | Complexity |
|---|---------|-------|------------|------------|
| 1 | [Two Sum](cselab/two_sum.py) | Hashing | Easy | O(n) time, O(n) space |
| 2 | [Valid Parentheses](cselab/valid_parentheses.py) | Stack | Easy | O(n) time, O(n) space |
| 3 | [Merge Intervals](cselab/merge_intervals.py) | Sorting | Medium | O(n log n) time, O(n) space |

## How this repo is built

Problems are released in small commits (`tools/stages.py`). A daily workflow
(`.github/workflows/drip.yml`) releases the next batch until the bank in
`tools/problems.py` runs out. The first commits were backfilled with
`tools/build_history.py`, so their dates are planned, not the day the code was
first typed. Everything after the backfill carries its real date.
