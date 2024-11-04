class Solution:
    def __init__(self):
        self.dp = dict()

    def fib(self, n: int) -> int:
        if n in [0, 1]:
            return n

        if n in self.dp:
            return self.dp[n]

        self.dp[n] = self.fib(n - 2) + self.fib(n - 1)

        return self.dp[n]
