class Solution:
    def climb(self, n, dp):
        if n == 0:
            return 1

        if dp[n] != -1:
            return dp[n]

        v1, v2 = 0, 0
        v1 = self.climb(n - 1, dp)
        if n > 1:
            v2 = self.climb(n - 2, dp)
        dp[n] = v1 + v2

        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.climb(n, dp)
