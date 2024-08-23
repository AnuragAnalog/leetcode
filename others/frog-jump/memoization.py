from os import *
from sys import *
from collections import *
from math import *

from typing import *

def energyGain(ind, heights, energy, n):
    if ind == n - 1:
        return energy
    elif ind == n - 2:
        return energy + abs(heights[n-2] - heights[n-1])
    else:
        e1 = energyGain(ind+1, heights, abs(heights[ind] - heights[ind+1]), n)
        e2 = energyGain(ind+2, heights, abs(heights[ind] - heights[ind+2]), n)

    return energy + min(e1, e2)

def frogJump(n: int, heights: List[int]) -> int:
    energy = 0

    return energyGain(0, heights, energy, n)
