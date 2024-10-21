class Solution:
    def find_sum(self, grid, sum_val, i, j):
        if i == self.m - 1 and j == self.n - 1:
            return (sum_val % self.k == 0)

        p1, p2 = 0, 0
        if i < self.m - 1:
            p1 = self.find_sum(grid, sum_val + grid[i+1][j], i+1, j)
        if j < self.n - 1:
            p2 = self.find_sum(grid, sum_val + grid[i][j+1], i, j+1)

        return p1 + p2

    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.k = k

        return self.find_sum(grid, grid[0][0], 0, 0) % (10**9 + 1)
