from os import *
from sys import *
from collections import *
from math import *

from typing import *


def energyGain(ind, heights):
    if ind == 0:
        return 0
    elif ind == 1:
        return abs(heights[0] - heights[1])
    else:
        er = energyGain(ind - 1, heights) + abs(heights[ind] - heights[ind - 1])
        el = energyGain(ind - 2, heights) + abs(heights[ind] - heights[ind - 2])

    return min(er, el)


def frogJump(n: int, heights: List[int]) -> int:
    dp = [0] * n

    dp[0] = 0
    dp[1] = abs(heights[0] - heights[1])

    for i in range(2, n):
        er = dp[i - 1] + abs(heights[i] - heights[i - 1])
        el = dp[i - 2] + abs(heights[i] - heights[i - 2])

        dp[i] = min(el, er)

    return dp[n - 1]
