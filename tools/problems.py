"""Problem bank: every entry is real, tested code. Order = release order.
The first BACKFILL entries are the history; the rest are dripped one per day."""

P = []


def add(slug, title, topic, diff, cx, code, tests):
    P.append(dict(slug=slug, title=title, topic=topic, diff=diff, cx=cx,
                  code=code.strip("\n") + "\n", tests=tests.strip("\n") + "\n"))


add("two_sum", "Two Sum", "Hashing", "Easy", "O(n) time, O(n) space", r'''
def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of the two numbers that add up to target, or []."""
    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
''', r'''
from cselab.two_sum import two_sum


def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_duplicates():
    assert two_sum([3, 3], 6) == [0, 1]


def test_none():
    assert two_sum([1, 2], 10) == []
''')

add("valid_parentheses", "Valid Parentheses", "Stack", "Easy", "O(n) time, O(n) space", r'''
def is_valid(s: str) -> bool:
    """True if every bracket in s is closed in the right order."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        elif ch in "([{":
            stack.append(ch)
    return not stack
''', r'''
from cselab.valid_parentheses import is_valid


def test_valid():
    assert is_valid("()[]{}")
    assert is_valid("{[()]}")
    assert is_valid("")


def test_invalid():
    assert not is_valid("(]")
    assert not is_valid("(((")
    assert not is_valid("]")
''')

add("merge_intervals", "Merge Intervals", "Sorting", "Medium", "O(n log n) time, O(n) space", r'''
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge all overlapping closed intervals."""
    out: list[list[int]] = []
    for start, end in sorted(intervals):
        if out and start <= out[-1][1]:
            out[-1][1] = max(out[-1][1], end)
        else:
            out.append([start, end])
    return out
''', r'''
from cselab.merge_intervals import merge_intervals


def test_overlap():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_touching():
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]


def test_unsorted_and_empty():
    assert merge_intervals([[5, 6], [1, 2]]) == [[1, 2], [5, 6]]
    assert merge_intervals([]) == []
''')

add("binary_search", "Binary Search & Lower Bound", "Searching", "Easy", "O(log n) time, O(1) space", r'''
def binary_search(a: list[int], target: int) -> int:
    """Index of target in sorted a, or -1."""
    i = lower_bound(a, target)
    return i if i < len(a) and a[i] == target else -1


def lower_bound(a: list[int], target: int) -> int:
    """First index whose value is >= target (len(a) if none)."""
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
''', r'''
from cselab.binary_search import binary_search, lower_bound


def test_found_and_missing():
    a = [1, 3, 5, 7, 9]
    assert binary_search(a, 7) == 3
    assert binary_search(a, 4) == -1
    assert binary_search([], 1) == -1


def test_lower_bound_duplicates():
    assert lower_bound([1, 2, 2, 2, 3], 2) == 1
    assert lower_bound([1, 2, 3], 10) == 3
    assert lower_bound([1, 2, 3], 0) == 0
''')

add("reverse_linked_list", "Reverse a Linked List", "Linked List", "Easy", "O(n) time, O(1) space", r'''
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def from_list(values: list[int]) -> "ListNode | None":
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head: "ListNode | None") -> list[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def reverse_list(head: "ListNode | None") -> "ListNode | None":
    """Reverse the list in place and return the new head."""
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev
''', r'''
from cselab.reverse_linked_list import from_list, reverse_list, to_list


def test_reverse():
    assert to_list(reverse_list(from_list([1, 2, 3, 4]))) == [4, 3, 2, 1]


def test_edges():
    assert reverse_list(None) is None
    assert to_list(reverse_list(from_list([7]))) == [7]
''')

add("max_subarray", "Maximum Subarray (Kadane)", "Dynamic Programming", "Medium", "O(n) time, O(1) space", r'''
def max_subarray(nums: list[int]) -> int:
    """Largest sum of a non-empty contiguous subarray."""
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
''', r'''
from cselab.max_subarray import max_subarray


def test_mixed():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_all_negative():
    assert max_subarray([-3, -1, -2]) == -1


def test_single():
    assert max_subarray([5]) == 5
''')

add("climbing_stairs", "Climbing Stairs", "Dynamic Programming", "Easy", "O(n) time, O(1) space", r'''
def climb_stairs(n: int) -> int:
    """Distinct ways to climb n steps taking 1 or 2 at a time."""
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
''', r'''
from cselab.climbing_stairs import climb_stairs


def test_small():
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8


def test_zero_and_large():
    assert climb_stairs(0) == 1
    assert climb_stairs(45) == 1836311903
''')

add("coin_change", "Coin Change", "Dynamic Programming", "Medium", "O(amount * coins) time, O(amount) space", r'''
def coin_change(coins: list[int], amount: int) -> int:
    """Fewest coins that make amount, or -1."""
    inf = amount + 1
    dp = [0] + [inf] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount] if dp[amount] != inf else -1
''', r'''
from cselab.coin_change import coin_change


def test_basic():
    assert coin_change([1, 2, 5], 11) == 3


def test_impossible():
    assert coin_change([2], 3) == -1


def test_zero():
    assert coin_change([1], 0) == 0


def test_greedy_fails():
    assert coin_change([1, 3, 4], 6) == 2
''')

add("lru_cache", "LRU Cache", "Design", "Medium", "O(1) get/put, O(capacity) space", r'''
from collections import OrderedDict


class LRUCache:
    """Fixed-capacity cache that evicts the least recently used key."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._d: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self._d:
            return -1
        self._d.move_to_end(key)
        return self._d[key]

    def put(self, key: int, value: int) -> None:
        if key in self._d:
            self._d.move_to_end(key)
        self._d[key] = value
        if len(self._d) > self.capacity:
            self._d.popitem(last=False)
''', r'''
from cselab.lru_cache import LRUCache


def test_eviction_order():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)  # evicts 2
    assert c.get(2) == -1
    assert c.get(3) == 3


def test_update_refreshes():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    c.put(1, 10)
    c.put(3, 3)  # evicts 2, not 1
    assert c.get(1) == 10
    assert c.get(2) == -1
''')

add("min_stack", "Min Stack", "Design", "Medium", "O(1) per operation", r'''
class MinStack:
    """Stack that returns its minimum in O(1)."""

    def __init__(self) -> None:
        self._s: list[tuple[int, int]] = []  # (value, min so far)

    def push(self, x: int) -> None:
        self._s.append((x, min(x, self._s[-1][1]) if self._s else x))

    def pop(self) -> int:
        return self._s.pop()[0]

    def top(self) -> int:
        return self._s[-1][0]

    def get_min(self) -> int:
        return self._s[-1][1]
''', r'''
from cselab.min_stack import MinStack


def test_min_tracks_pops():
    s = MinStack()
    for x in (5, 3, 7, 3, 1):
        s.push(x)
    assert s.get_min() == 1
    s.pop()
    assert s.get_min() == 3
    s.pop()
    s.pop()
    assert s.get_min() == 3
    assert s.top() == 3
    s.pop()
    assert s.get_min() == 5
''')

add("trie", "Trie (Prefix Tree)", "Trees", "Medium", "O(L) per operation", r'''
class Trie:
    def __init__(self) -> None:
        self._root: dict = {}

    def insert(self, word: str) -> None:
        node = self._root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def _walk(self, s: str):
        node = self._root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return bool(node and "$" in node)

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None
''', r'''
from cselab.trie import Trie


def test_trie():
    t = Trie()
    t.insert("apple")
    assert t.search("apple")
    assert not t.search("app")
    assert t.starts_with("app")
    t.insert("app")
    assert t.search("app")
    assert not t.starts_with("b")
''')

add("union_find", "Union-Find (DSU)", "Graphs", "Medium", "~O(alpha(n)) per operation", r'''
class UnionFind:
    """Disjoint sets with path compression and union by size."""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True

    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)
''', r'''
from cselab.union_find import UnionFind


def test_union_and_components():
    u = UnionFind(5)
    assert u.union(0, 1)
    assert u.union(1, 2)
    assert not u.union(0, 2)
    assert u.connected(0, 2)
    assert not u.connected(0, 4)
    assert u.components == 3
''')

add("topological_sort", "Topological Sort (Kahn)", "Graphs", "Medium", "O(V + E) time and space", r'''
from collections import deque


def topological_sort(n: int, edges: list[tuple[int, int]]) -> list[int]:
    """Order of nodes 0..n-1 where every edge u->v has u before v; [] if cyclic."""
    adj: list[list[int]] = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order: list[int] = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []
''', r'''
from cselab.topological_sort import topological_sort


def test_order_respects_edges():
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    order = topological_sort(6, edges)
    assert sorted(order) == list(range(6))
    pos = {v: i for i, v in enumerate(order)}
    assert all(pos[u] < pos[v] for u, v in edges)


def test_cycle():
    assert topological_sort(3, [(0, 1), (1, 2), (2, 0)]) == []
''')

add("dijkstra", "Dijkstra Shortest Paths", "Graphs", "Medium", "O((V + E) log V) time", r'''
import heapq


def dijkstra(graph: dict[int, list[tuple[int, int]]], src: int) -> dict[int, int]:
    """Shortest distance from src to every reachable node (non-negative weights)."""
    dist = {src: 0}
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float("inf")):
            continue
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist
''', r'''
from cselab.dijkstra import dijkstra


def test_shortest_paths():
    g = {0: [(1, 4), (2, 1)], 2: [(1, 2), (3, 7)], 1: [(3, 1)]}
    assert dijkstra(g, 0) == {0: 0, 2: 1, 1: 3, 3: 4}


def test_unreachable_omitted():
    assert dijkstra({0: [(1, 1)], 5: [(6, 1)]}, 0) == {0: 0, 1: 1}
''')

add("bfs_grid", "Shortest Path in a Grid (BFS)", "Graphs", "Medium", "O(rows * cols) time and space", r'''
from collections import deque


def shortest_path(grid: list[list[int]]) -> int:
    """Steps from top-left to bottom-right through 0-cells (4-directional), or -1."""
    if not grid or grid[0][0] or grid[-1][-1]:
        return -1
    rows, cols = len(grid), len(grid[0])
    q = deque([(0, 0, 0)])
    seen = {(0, 0)}
    while q:
        r, c, d = q.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return d
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and not grid[nr][nc] and (nr, nc) not in seen:
                seen.add((nr, nc))
                q.append((nr, nc, d + 1))
    return -1
''', r'''
from cselab.bfs_grid import shortest_path


def test_open_grid():
    assert shortest_path([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 4


def test_walls():
    assert shortest_path([[0, 1, 0], [0, 1, 0], [0, 0, 0]]) == 4
    assert shortest_path([[0, 1], [1, 0]]) == -1
    assert shortest_path([[1]]) == -1
    assert shortest_path([[0]]) == 0
''')

add("number_of_islands", "Number of Islands", "Graphs", "Medium", "O(rows * cols) time and space", r'''
def num_islands(grid: list[list[str]]) -> int:
    """Count 4-connected groups of '1' cells."""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    seen = [[False] * cols for _ in range(rows)]
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and not seen[r][c]:
                count += 1
                stack = [(r, c)]
                seen[r][c] = True
                while stack:
                    y, x = stack.pop()
                    for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                        if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == "1" and not seen[ny][nx]:
                            seen[ny][nx] = True
                            stack.append((ny, nx))
    return count
''', r'''
from cselab.number_of_islands import num_islands


def test_islands():
    g = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert num_islands(g) == 3


def test_empty_and_water():
    assert num_islands([]) == 0
    assert num_islands([list("000")]) == 0
''')

add("lcs", "Longest Common Subsequence", "Dynamic Programming", "Medium", "O(m * n) time, O(n) space", r'''
def lcs_length(a: str, b: str) -> int:
    """Length of the longest common subsequence of a and b."""
    prev = [0] * (len(b) + 1)
    for ch in a:
        cur = [0]
        for j, other in enumerate(b, 1):
            cur.append(prev[j - 1] + 1 if ch == other else max(prev[j], cur[j - 1]))
        prev = cur
    return prev[-1]
''', r'''
from cselab.lcs import lcs_length


def test_lcs():
    assert lcs_length("abcde", "ace") == 3
    assert lcs_length("abc", "abc") == 3
    assert lcs_length("abc", "def") == 0
    assert lcs_length("", "abc") == 0
''')

add("edit_distance", "Edit Distance (Levenshtein)", "Dynamic Programming", "Hard", "O(m * n) time, O(n) space", r'''
def edit_distance(a: str, b: str) -> int:
    """Minimum insertions, deletions and substitutions turning a into b."""
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]
''', r'''
from cselab.edit_distance import edit_distance


def test_known():
    assert edit_distance("horse", "ros") == 3
    assert edit_distance("intention", "execution") == 5


def test_edges():
    assert edit_distance("", "abc") == 3
    assert edit_distance("abc", "") == 3
    assert edit_distance("same", "same") == 0
''')

add("knapsack", "0/1 Knapsack", "Dynamic Programming", "Medium", "O(n * W) time, O(W) space", r'''
def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    """Max total value of items fitting in capacity, each used at most once."""
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]
''', r'''
from cselab.knapsack import knapsack


def test_classic():
    assert knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9


def test_edges():
    assert knapsack([5], [10], 4) == 0
    assert knapsack([], [], 10) == 0
    assert knapsack([2, 2], [3, 3], 3) == 3
''')

add("merge_sort", "Merge Sort", "Sorting", "Medium", "O(n log n) time, O(n) space", r'''
def merge_sort(a: list[int]) -> list[int]:
    """Stable merge sort; returns a new list."""
    if len(a) <= 1:
        return list(a)
    mid = len(a) // 2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    out: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out
''', r'''
import random

from cselab.merge_sort import merge_sort


def test_sorted_matches_builtin():
    rng = random.Random(7)
    for _ in range(50):
        a = [rng.randint(-50, 50) for _ in range(rng.randint(0, 40))]
        assert merge_sort(a) == sorted(a)


def test_does_not_mutate():
    a = [3, 1, 2]
    merge_sort(a)
    assert a == [3, 1, 2]
''')

add("kth_largest", "Kth Largest Element", "Heap", "Medium", "O(n log k) time, O(k) space", r'''
import heapq


def kth_largest(nums: list[int], k: int) -> int:
    """The k-th largest value (1-based) using a size-k min-heap."""
    heap = nums[:k]
    heapq.heapify(heap)
    for x in nums[k:]:
        if x > heap[0]:
            heapq.heapreplace(heap, x)
    return heap[0]
''', r'''
from cselab.kth_largest import kth_largest


def test_kth():
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert kth_largest([1], 1) == 1
''')

add("top_k_frequent", "Top K Frequent Elements", "Hashing", "Medium", "O(n) time with bucket sort", r'''
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """The k most frequent values (bucket sort by frequency)."""
    freq: dict[int, int] = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for x, f in freq.items():
        buckets[f].append(x)
    out: list[int] = []
    for f in range(len(nums), 0, -1):
        for x in buckets[f]:
            out.append(x)
            if len(out) == k:
                return out
    return out
''', r'''
from cselab.top_k_frequent import top_k_frequent


def test_top_k():
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert top_k_frequent([4, 4, 4, 5, 5, 6], 1) == [4]
''')

add("valid_anagram", "Valid Anagram", "Hashing", "Easy", "O(n) time, O(1) space", r'''
from collections import Counter


def is_anagram(a: str, b: str) -> bool:
    """True if b is a rearrangement of a."""
    return Counter(a) == Counter(b)
''', r'''
from cselab.valid_anagram import is_anagram


def test_anagram():
    assert is_anagram("listen", "silent")
    assert not is_anagram("rat", "car")
    assert not is_anagram("aab", "abb")
    assert is_anagram("", "")
''')

add("longest_unique_substring", "Longest Substring Without Repeats", "Sliding Window", "Medium", "O(n) time, O(k) space", r'''
def longest_unique_substring(s: str) -> int:
    """Length of the longest substring with all distinct characters."""
    last: dict[str, int] = {}
    start = best = 0
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1
        last[ch] = i
        best = max(best, i - start + 1)
    return best
''', r'''
from cselab.longest_unique_substring import longest_unique_substring


def test_cases():
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1
    assert longest_unique_substring("pwwkew") == 3
    assert longest_unique_substring("") == 0
    assert longest_unique_substring("abba") == 2
''')

add("three_sum", "3Sum", "Two Pointers", "Medium", "O(n^2) time, O(1) extra space", r'''
def three_sum(nums: list[int]) -> list[list[int]]:
    """All unique triplets that sum to zero."""
    nums = sorted(nums)
    out: list[list[int]] = []
    for i, a in enumerate(nums):
        if i and a == nums[i - 1]:
            continue
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            s = a + nums[lo] + nums[hi]
            if s < 0:
                lo += 1
            elif s > 0:
                hi -= 1
            else:
                out.append([a, nums[lo], nums[hi]])
                lo += 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
    return out
''', r'''
from cselab.three_sum import three_sum


def test_three_sum():
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([1, 2, 3]) == []
''')

add("container_most_water", "Container With Most Water", "Two Pointers", "Medium", "O(n) time, O(1) space", r'''
def max_area(height: list[int]) -> int:
    """Largest water area between two lines, moving the shorter side inward."""
    lo, hi, best = 0, len(height) - 1, 0
    while lo < hi:
        best = max(best, (hi - lo) * min(height[lo], height[hi]))
        if height[lo] < height[hi]:
            lo += 1
        else:
            hi -= 1
    return best
''', r'''
from cselab.container_most_water import max_area


def test_area():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([5]) == 0
''')

add("rotate_matrix", "Rotate Image", "Matrix", "Medium", "O(n^2) time, O(1) space", r'''
def rotate(matrix: list[list[int]]) -> None:
    """Rotate an n x n matrix 90 degrees clockwise, in place."""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
''', r'''
from cselab.rotate_matrix import rotate


def test_rotate_3x3():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(m)
    assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def test_rotate_1x1_and_2x2():
    m = [[1]]
    rotate(m)
    assert m == [[1]]
    m = [[1, 2], [3, 4]]
    rotate(m)
    assert m == [[3, 1], [4, 2]]
''')

add("spiral_order", "Spiral Matrix", "Matrix", "Medium", "O(m * n) time", r'''
def spiral_order(matrix: list[list[int]]) -> list[int]:
    """Elements of the matrix in clockwise spiral order."""
    out: list[int] = []
    if not matrix:
        return out
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        out.extend(matrix[top][left:right + 1])
        out.extend(matrix[r][right] for r in range(top + 1, bottom + 1))
        if top < bottom:
            out.extend(reversed(matrix[bottom][left:right]))
        if left < right:
            out.extend(matrix[r][left] for r in range(bottom - 1, top, -1))
        top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
    return out
''', r'''
from cselab.spiral_order import spiral_order


def test_spiral():
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]
    assert spiral_order([]) == []
''')

add("permutations", "Permutations", "Backtracking", "Medium", "O(n * n!) time", r'''
def permutations(nums: list[int]) -> list[list[int]]:
    """All orderings of nums (distinct values)."""
    out: list[list[int]] = []

    def go(cur: list[int], used: list[bool]) -> None:
        if len(cur) == len(nums):
            out.append(cur[:])
            return
        for i, x in enumerate(nums):
            if not used[i]:
                used[i] = True
                cur.append(x)
                go(cur, used)
                cur.pop()
                used[i] = False

    go([], [False] * len(nums))
    return out
''', r'''
from itertools import permutations as std

from cselab.permutations import permutations


def test_matches_itertools():
    assert permutations([1, 2, 3]) == [list(p) for p in std([1, 2, 3])]


def test_edges():
    assert permutations([]) == [[]]
    assert permutations([9]) == [[9]]
''')

add("subsets", "Subsets", "Backtracking", "Medium", "O(n * 2^n) time", r'''
def subsets(nums: list[int]) -> list[list[int]]:
    """The power set of nums."""
    out: list[list[int]] = [[]]
    for x in nums:
        out += [s + [x] for s in out]
    return out
''', r'''
from cselab.subsets import subsets


def test_power_set():
    result = subsets([1, 2, 3])
    assert len(result) == 8
    assert sorted(map(tuple, result)) == sorted([(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)])


def test_empty():
    assert subsets([]) == [[]]
''')

add("n_queens", "N-Queens (count)", "Backtracking", "Hard", "O(n!) time worst case", r'''
def total_n_queens(n: int) -> int:
    """Number of ways to place n non-attacking queens on an n x n board."""
    cols: set[int] = set()
    diag1: set[int] = set()
    diag2: set[int] = set()

    def place(r: int) -> int:
        if r == n:
            return 1
        total = 0
        for c in range(n):
            if c in cols or r - c in diag1 or r + c in diag2:
                continue
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            total += place(r + 1)
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)
        return total

    return place(0)
''', r'''
from cselab.n_queens import total_n_queens


def test_known_counts():
    assert [total_n_queens(n) for n in range(1, 9)] == [1, 0, 0, 2, 10, 4, 40, 92]
''')

add("inorder_traversal", "Binary Tree Inorder (iterative)", "Trees", "Easy", "O(n) time, O(h) space", r'''
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: "TreeNode | None") -> list[int]:
    """Left, node, right - with an explicit stack instead of recursion."""
    out: list[int] = []
    stack: list[TreeNode] = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        out.append(node.val)
        node = node.right
    return out
''', r'''
from cselab.inorder_traversal import TreeNode, inorder


def test_inorder():
    root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(2.5), None))
    assert inorder(root) == [1, 2, 2.5, 3]


def test_empty_and_deep():
    assert inorder(None) == []
    node = None
    for i in range(5000):  # would blow the recursion limit if recursive
        node = TreeNode(i, node, None)
    assert len(inorder(node)) == 5000
''')

add("level_order", "Level Order Traversal", "Trees", "Medium", "O(n) time and space", r'''
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: "TreeNode | None") -> list[list[int]]:
    """Node values grouped by depth, left to right."""
    out: list[list[int]] = []
    q = deque([root] if root else [])
    while q:
        out.append([n.val for n in q])
        for _ in range(len(q)):
            n = q.popleft()
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
    return out
''', r'''
from cselab.level_order import TreeNode, level_order


def test_levels():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(root) == [[3], [9, 20], [15, 7]]


def test_empty():
    assert level_order(None) == []
''')

add("number_theory", "Sieve, GCD and LCM", "Math", "Easy", "Sieve O(n log log n); GCD O(log n)", r'''
def sieve(n: int) -> list[int]:
    """All primes <= n (sieve of Eratosthenes)."""
    if n < 2:
        return []
    is_p = bytearray([1]) * (n + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if is_p[i]:
            is_p[i * i::i] = bytearray(len(is_p[i * i::i]))
    return [i for i, p in enumerate(is_p) if p]


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b) if a and b else 0
''', r'''
from math import gcd as std_gcd

from cselab.number_theory import gcd, lcm, sieve


def test_sieve():
    assert sieve(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert sieve(1) == []
    assert len(sieve(10000)) == 1229


def test_gcd_lcm():
    for a, b in [(12, 18), (17, 5), (0, 9), (100, 75)]:
        assert gcd(a, b) == std_gcd(a, b)
    assert lcm(4, 6) == 12
    assert lcm(0, 5) == 0
''')

add("fast_pow", "Fast Modular Exponentiation", "Math", "Medium", "O(log exp) time", r'''
def pow_mod(base: int, exp: int, mod: int) -> int:
    """base ** exp % mod by repeated squaring."""
    result = 1
    base %= mod
    while exp:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result % mod
''', r'''
from cselab.fast_pow import pow_mod


def test_matches_builtin():
    for b, e, m in [(2, 10, 1000), (7, 0, 13), (3, 200, 1_000_000_007), (10, 18, 7)]:
        assert pow_mod(b, e, m) == pow(b, e, m)


def test_mod_one():
    assert pow_mod(5, 3, 1) == 0
''')

add("bit_tricks", "Bit Tricks", "Bit Manipulation", "Easy", "O(1) / O(set bits)", r'''
def single_number(nums: list[int]) -> int:
    """The value that appears once when every other appears twice."""
    x = 0
    for n in nums:
        x ^= n
    return x


def count_bits(n: int) -> int:
    """Number of set bits (Kernighan's trick)."""
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


def is_power_of_two(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0
''', r'''
from cselab.bit_tricks import count_bits, is_power_of_two, single_number


def test_single_number():
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([7]) == 7


def test_count_bits():
    assert [count_bits(n) for n in (0, 1, 7, 8, 255)] == [0, 1, 3, 1, 8]


def test_power_of_two():
    assert is_power_of_two(1) and is_power_of_two(1024)
    assert not is_power_of_two(0) and not is_power_of_two(6) and not is_power_of_two(-4)
''')

add("is_palindrome", "Valid Palindrome", "Two Pointers", "Easy", "O(n) time, O(1) space", r'''
def is_palindrome(s: str) -> bool:
    """Palindrome check ignoring case and non-alphanumerics."""
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True
''', r'''
from cselab.is_palindrome import is_palindrome


def test_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert is_palindrome("")
    assert is_palindrome(" ")
    assert not is_palindrome("race a car")
''')

add("group_anagrams", "Group Anagrams", "Hashing", "Medium", "O(n * k log k) time", r'''
def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other."""
    groups: dict[str, list[str]] = {}
    for w in words:
        groups.setdefault("".join(sorted(w)), []).append(w)
    return list(groups.values())
''', r'''
from cselab.group_anagrams import group_anagrams


def test_groups():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(sorted(g) for g in result) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]


def test_empty():
    assert group_anagrams([]) == []
''')

add("product_except_self", "Product of Array Except Self", "Arrays", "Medium", "O(n) time, O(1) extra space", r'''
def product_except_self(nums: list[int]) -> list[int]:
    """out[i] is the product of every element except nums[i], without division."""
    n = len(nums)
    out = [1] * n
    left = 1
    for i in range(n):
        out[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        out[i] *= right
        right *= nums[i]
    return out
''', r'''
from cselab.product_except_self import product_except_self


def test_product():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([5]) == [1]
''')

add("first_missing_positive", "First Missing Positive", "Arrays", "Hard", "O(n) time, O(1) space", r'''
def first_missing_positive(nums: list[int]) -> int:
    """Smallest positive integer not in nums (cyclic placement, mutates a copy)."""
    a = list(nums)
    n = len(a)
    for i in range(n):
        while 1 <= a[i] <= n and a[a[i] - 1] != a[i]:
            j = a[i] - 1
            a[i], a[j] = a[j], a[i]
    for i, x in enumerate(a):
        if x != i + 1:
            return i + 1
    return n + 1
''', r'''
from cselab.first_missing_positive import first_missing_positive


def test_cases():
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1
    assert first_missing_positive([]) == 1
    assert first_missing_positive([1, 1]) == 2
''')

BACKFILL = len(P)

# ---- reserve: released one problem per day by the drip workflow ----

add("word_break", "Word Break", "Dynamic Programming", "Medium", "O(n^2) time, O(n) space", r'''
def word_break(s: str, words: list[str]) -> bool:
    """True if s can be segmented into dictionary words."""
    dictionary = set(words)
    ok = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        ok[i] = any(ok[j] and s[j:i] in dictionary for j in range(i))
    return ok[len(s)]
''', r'''
from cselab.word_break import word_break


def test_word_break():
    assert word_break("leetcode", ["leet", "code"])
    assert word_break("applepenapple", ["apple", "pen"])
    assert not word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
    assert word_break("", ["a"])
''')

add("kmp_search", "KMP String Search", "Strings", "Hard", "O(n + m) time, O(m) space", r'''
def kmp_search(text: str, pattern: str) -> list[int]:
    """Start index of every occurrence of pattern in text (empty pattern -> [])."""
    if not pattern:
        return []
    fail = [0] * len(pattern)
    k = 0
    for i in range(1, len(pattern)):
        while k and pattern[i] != pattern[k]:
            k = fail[k - 1]
        if pattern[i] == pattern[k]:
            k += 1
        fail[i] = k
    out: list[int] = []
    k = 0
    for i, ch in enumerate(text):
        while k and ch != pattern[k]:
            k = fail[k - 1]
        if ch == pattern[k]:
            k += 1
        if k == len(pattern):
            out.append(i - k + 1)
            k = fail[k - 1]
    return out
''', r'''
from cselab.kmp_search import kmp_search


def test_search():
    assert kmp_search("abababca", "abab") == [0, 2]
    assert kmp_search("aaaaa", "aa") == [0, 1, 2, 3]
    assert kmp_search("hello", "xyz") == []
    assert kmp_search("hello", "") == []
''')

add("lis", "Longest Increasing Subsequence", "Dynamic Programming", "Medium", "O(n log n) time, O(n) space", r'''
from bisect import bisect_left


def lis_length(nums: list[int]) -> int:
    """Length of the longest strictly increasing subsequence (patience sorting)."""
    tails: list[int] = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
''', r'''
from cselab.lis import lis_length


def test_lis():
    assert lis_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lis_length([0, 1, 0, 3, 2, 3]) == 4
    assert lis_length([7, 7, 7]) == 1
    assert lis_length([]) == 0
''')

add("median_finder", "Running Median", "Heap", "Hard", "O(log n) add, O(1) median", r'''
import heapq


class MedianFinder:
    """Median of a stream using a max-heap (lower half) and a min-heap (upper half)."""

    def __init__(self) -> None:
        self._lo: list[int] = []  # max-heap via negation
        self._hi: list[int] = []

    def add(self, x: int) -> None:
        heapq.heappush(self._lo, -x)
        heapq.heappush(self._hi, -heapq.heappop(self._lo))
        if len(self._hi) > len(self._lo):
            heapq.heappush(self._lo, -heapq.heappop(self._hi))

    def median(self) -> float:
        if len(self._lo) > len(self._hi):
            return float(-self._lo[0])
        return (-self._lo[0] + self._hi[0]) / 2
''', r'''
import random
import statistics

from cselab.median_finder import MedianFinder


def test_stream_matches_statistics():
    rng = random.Random(3)
    m, seen = MedianFinder(), []
    for _ in range(200):
        x = rng.randint(-100, 100)
        m.add(x)
        seen.append(x)
        assert m.median() == statistics.median(seen)
''')

add("token_bucket", "Token Bucket Rate Limiter", "Systems", "Medium", "O(1) per request", r'''
import time
from typing import Callable


class TokenBucket:
    """Allows bursts up to capacity, refilling at `rate` tokens per second."""

    def __init__(self, capacity: float, rate: float, clock: Callable[[], float] = time.monotonic):
        self.capacity = capacity
        self.rate = rate
        self._clock = clock
        self._tokens = capacity
        self._last = clock()

    def allow(self, cost: float = 1.0) -> bool:
        now = self._clock()
        self._tokens = min(self.capacity, self._tokens + (now - self._last) * self.rate)
        self._last = now
        if self._tokens >= cost:
            self._tokens -= cost
            return True
        return False
''', r'''
from cselab.token_bucket import TokenBucket


class FakeClock:
    def __init__(self):
        self.t = 0.0

    def __call__(self):
        return self.t


def test_burst_then_refill():
    clock = FakeClock()
    b = TokenBucket(capacity=3, rate=1, clock=clock)
    assert [b.allow() for _ in range(4)] == [True, True, True, False]
    clock.t = 2.0
    assert [b.allow() for _ in range(3)] == [True, True, False]


def test_never_exceeds_capacity():
    clock = FakeClock()
    b = TokenBucket(capacity=2, rate=10, clock=clock)
    clock.t = 100.0
    assert [b.allow() for _ in range(3)] == [True, True, False]
''')

add("bloom_filter", "Bloom Filter", "Systems", "Medium", "O(k) per operation, no false negatives", r'''
import hashlib


class BloomFilter:
    """Probabilistic set: may report false positives, never false negatives."""

    def __init__(self, size_bits: int = 8192, hashes: int = 3):
        self.size = size_bits
        self.hashes = hashes
        self._bits = bytearray(size_bits)

    def _positions(self, item: str):
        for i in range(self.hashes):
            digest = hashlib.sha256(f"{i}:{item}".encode()).digest()
            yield int.from_bytes(digest[:8], "big") % self.size

    def add(self, item: str) -> None:
        for p in self._positions(item):
            self._bits[p] = 1

    def might_contain(self, item: str) -> bool:
        return all(self._bits[p] for p in self._positions(item))
''', r'''
from cselab.bloom_filter import BloomFilter


def test_no_false_negatives():
    bf = BloomFilter(10_000, 3)
    items = [f"user:{i}" for i in range(200)]
    for it in items:
        bf.add(it)
    assert all(bf.might_contain(it) for it in items)


def test_low_false_positive_rate():
    bf = BloomFilter(10_000, 3)
    for i in range(200):
        bf.add(f"user:{i}")
    false_pos = sum(bf.might_contain(f"other:{i}") for i in range(1000))
    assert false_pos < 30
''')

add("consistent_hashing", "Consistent Hashing Ring", "Systems", "Hard", "O(log n) lookup", r'''
import bisect
import hashlib


def _h(s: str) -> int:
    return int.from_bytes(hashlib.md5(s.encode()).digest()[:8], "big")


class ConsistentHashRing:
    """Maps keys to nodes so adding/removing a node only moves ~1/n of the keys."""

    def __init__(self, nodes: list[str], replicas: int = 100):
        self.replicas = replicas
        self._ring: list[int] = []
        self._owner: dict[int, str] = {}
        for n in nodes:
            self.add_node(n)

    def add_node(self, node: str) -> None:
        for i in range(self.replicas):
            h = _h(f"{node}#{i}")
            bisect.insort(self._ring, h)
            self._owner[h] = node

    def remove_node(self, node: str) -> None:
        for i in range(self.replicas):
            h = _h(f"{node}#{i}")
            self._ring.remove(h)
            del self._owner[h]

    def get_node(self, key: str) -> str:
        i = bisect.bisect(self._ring, _h(key)) % len(self._ring)
        return self._owner[self._ring[i]]
''', r'''
from cselab.consistent_hashing import ConsistentHashRing


def test_deterministic_and_balanced():
    ring = ConsistentHashRing(["a", "b", "c"])
    keys = [f"key{i}" for i in range(3000)]
    assert [ring.get_node(k) for k in keys] == [ring.get_node(k) for k in keys]
    counts = {n: 0 for n in "abc"}
    for k in keys:
        counts[ring.get_node(k)] += 1
    assert all(500 < c < 1600 for c in counts.values())


def test_removal_only_moves_that_nodes_keys():
    ring = ConsistentHashRing(["a", "b", "c"])
    keys = [f"key{i}" for i in range(2000)]
    before = {k: ring.get_node(k) for k in keys}
    ring.remove_node("b")
    for k in keys:
        if before[k] != "b":
            assert ring.get_node(k) == before[k]
        else:
            assert ring.get_node(k) in ("a", "c")
''')

add("ring_buffer", "Ring Buffer", "Systems", "Easy", "O(1) push, O(n) to_list", r'''
class RingBuffer:
    """Fixed-size buffer that overwrites the oldest item when full."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._buf: list = [None] * capacity
        self._start = 0
        self._len = 0

    def push(self, item) -> None:
        if self._len < self.capacity:
            self._buf[(self._start + self._len) % self.capacity] = item
            self._len += 1
        else:
            self._buf[self._start] = item
            self._start = (self._start + 1) % self.capacity

    def __len__(self) -> int:
        return self._len

    def to_list(self) -> list:
        return [self._buf[(self._start + i) % self.capacity] for i in range(self._len)]
''', r'''
from cselab.ring_buffer import RingBuffer


def test_fill_and_overwrite():
    rb = RingBuffer(3)
    for x in (1, 2):
        rb.push(x)
    assert rb.to_list() == [1, 2] and len(rb) == 2
    for x in (3, 4, 5):
        rb.push(x)
    assert rb.to_list() == [3, 4, 5] and len(rb) == 3
''')
