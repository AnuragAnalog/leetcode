class Solution:
    def go(self, grid, i, j, dp):
        if self.m - 1 == i and self.n - 1 == j:
            return 1

        if dp[i][j] != -1:
            return dp[i][j]
        
        p1, p2 = 0, 0
        if i < self.m - 1 and grid[i+1][j] != 1:
            p1 = self.go(grid, i + 1, j, dp)
        if j < self.n - 1 and grid[i][j+1] != 1:
            p2 = self.go(grid, i, j + 1, dp)

        dp[i][j] = p1 + p2

        return dp[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.m = len(obstacleGrid)
        self.n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(self.n)] for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0

        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        return self.go(obstacleGrid, 0, 0, dp)
