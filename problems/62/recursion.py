class Solution:
    def go(self, i, j):
        if i == self.m - 1 and j == self.n - 1:
            return 1
        
        p1, p2 = 0, 0
        if i < self.m - 1:
            p1 = self.go(i + 1, j)
        if j < self.n - 1:
            p2 = self.go(i, j + 1)

        return p1 + p2

    def uniquePaths(self, m, n):
        self.m = m
        self.n = n

        return self.go(0, 0)
