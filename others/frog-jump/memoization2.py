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
    return energyGain(n - 1 , heights)
