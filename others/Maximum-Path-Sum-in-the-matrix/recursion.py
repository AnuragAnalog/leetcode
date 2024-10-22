from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit

# setrecursionlimit(10**7)


def path(matrix, i, j, m, n):
    if j < 0 or j > n - 1:
        return -(10**9)
    elif i == m - 1:
        return matrix[i][j]
    else:
        p1 = matrix[i][j] + path(matrix, i + 1, j - 1, m, n)
        p2 = matrix[i][j] + path(matrix, i + 1, j, m, n)
        p3 = matrix[i][j] + path(matrix, i + 1, j + 1, m, n)

        return max(p1, p2, p3)


def getMaxPathSum(matrix):
    maxi = -(10**9)
    m = len(matrix)
    n = len(matrix[0])

    for j in range(n):
        maxi = max(maxi, path(matrix, 0, j, m, n))

    return maxi
