class Solution:
    def search(self, n, dp):
        if n in [0, 1]:
            return 1

        if dp[n] != -1:
            return dp[n]

        total = 0
        for i in range(1, n+1):
            total += (self.search(i-1, dp) * self.search(n - i, dp))

        dp[n] = total

        return dp[n]

    def numTrees(self, n: int) -> int:
        dp = [-1] * (n+1)

        return self.search(n, dp)
