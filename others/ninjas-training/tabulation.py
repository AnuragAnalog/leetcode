from typing import *


def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[0] * 4 for _ in range(n)]

    for i in range(4):
        maxi = 0
        for j in range(3):
            if i != j:
                maxi = max(maxi, points[0][j])

        dp[0][i] = maxi

    for i in range(1, n):
        for j in range(4):
            maxi = 0
            for k in range(3):
                if k != j:
                    maxi = max(maxi, points[i][k] + dp[i - 1][k])

            dp[i][j] = maxi

    return dp[n - 1][3]
