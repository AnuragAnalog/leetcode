class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        for i in range(1, m):
            for j in range(1, n):
                val = 0
                if obstacleGrid[i-1][j] != 1:
                    val += dp[i-1][j]
                if obstacleGrid[i][j-1] != 1:
                    val += dp[i][j-1]
                dp[i][j] = val

        return dp[m - 1][n - 1]
