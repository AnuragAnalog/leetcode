from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def getMaxPathSum(matrix):
    maxi = -10**9
    m = len(matrix)
    n = len(matrix[0])

    dp = [[0] * n for _ in range(m)]

    for j in range(n):
        dp[0][j] = matrix[0][j]

    for i in range(1, m):
        for j in range(n):
            maxi = -10**9
            for k in [-1, 0, 1]:
                if j+k >= 0 and j+k <= n-1:
                    maxi = max(maxi, dp[i-1][j+k])
                else:
                    maxi = max(maxi, -10**9) 
            dp[i][j] = matrix[i][j] + maxi
    
    return max(dp[-1])
