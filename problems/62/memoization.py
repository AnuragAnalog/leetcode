class Solution:
    def go(self, i, j, dp):
        if i == self.m - 1 and j == self.n - 1:
            return 1
        
        if dp[i][j] != -1:
            return dp[i][j]

        p1, p2 = 0, 0
        if i < self.m - 1:
            p1 = self.go(i + 1, j, dp)
        if j < self.n - 1:
            p2 = self.go(i, j + 1, dp)

        dp[i][j] = p1 + p2
        
        return dp[i][j]

    def uniquePaths(self, m, n):
        self.m = m
        self.n = n

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        return self.go(0, 0, dp)
