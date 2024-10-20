class Solution:
    def go(self, grid, i, j):
        if self.m - 1 == i and self.n - 1 == j:
            return 1
        
        p1, p2 = 0, 0
        if i < self.m - 1 and grid[i+1][j] != 1:
            p1 = self.go(grid, i + 1, j)
        if j < self.n - 1 and grid[i][j+1] != 1:
            p2 = self.go(grid, i, j + 1)

        return p1 + p2

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.m = len(obstacleGrid)
        self.n = len(obstacleGrid[0])

        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        return self.go(obstacleGrid, 0, 0)
