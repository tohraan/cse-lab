"""0/1 Knapsack."""

def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    """Max total value of items fitting in capacity, each used at most once."""
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]
