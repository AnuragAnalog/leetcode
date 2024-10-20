class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n+1):
            v1, v2 = 0, 0
            v1 = dp[i - 1]
            if i > 1:
                v2 = dp[i - 2]
            dp[i] = v1 + v2

        return dp[n]
