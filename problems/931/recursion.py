class Solution:
    def go(self, matrix, sum_val, i, j):
        if self.m - 1 == i:
            return sum_val

        s1, s2 = 10**10, 10**10
        if j > 0:
            s1 = self.go(matrix, sum_val + matrix[i + 1][j - 1], i + 1, j - 1)
        if j < self.n - 1:
            s2 = self.go(matrix, sum_val + matrix[i + 1][j + 1], i + 1, j + 1)
        s3 = self.go(matrix, sum_val + matrix[i + 1][j], i + 1, j)

        return min([s1, s2, s3])

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.m = len(matrix)
        self.n = len(matrix)

        mini = 10**10
        for j in range(self.n):
            mini = min(mini, self.go(matrix, matrix[0][j], 0, j))

        return mini
