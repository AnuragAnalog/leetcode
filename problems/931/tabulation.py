class Solution:
    def go(self, matrix, sum_val, i, j, dp):
        if self.m - 1 == i:
            return sum_val

        if dp[i][j] != 10**10:
            return dp[i][j]

        s1, s2 = 10**10, 10**10
        if j > 0:
            s1 = self.go(matrix, sum_val + matrix[i + 1][j - 1], i + 1, j - 1, dp)
        if j < self.n - 1:
            s2 = self.go(matrix, sum_val + matrix[i + 1][j + 1], i + 1, j + 1, dp)
        s3 = self.go(matrix, sum_val + matrix[i + 1][j], i + 1, j, dp)

        dp[i][j] = min([s1, s2, s3])

        return dp[i][j]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.m = len(matrix)
        self.n = len(matrix)

        dp = [[10**10 for _ in range(self.n)] for _ in range(self.m)]

        for j in range(self.n):
            dp[0][j] = matrix[0][j]

        for i in range(1, self.m):
            for j in range(self.n):
                s1, s2 = 10**10, 10**10
                if j > 0:
                    s1 = dp[i-1][j-1]
                if j < self.n - 1:
                    s2 = dp[i-1][j+1]
                s3 = dp[i-1][j]
                dp[i][j] = matrix[i][j] + min([s1, s2, s3])

        return min(dp[-1])
