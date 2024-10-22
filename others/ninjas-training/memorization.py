from typing import *


def f(ind, points, sel_index):
    if ind == 0:
        maxi = 0
        for i in range(3):
            if i != sel_index:
                maxi = max(maxi, points[ind][i])

        return maxi

    maxi = 0
    for i in range(3):
        if i != sel_index:
            maxi = max(maxi, points[ind][i] + f(ind - 1, points, i))

    return maxi


def ninjaTraining(n: int, points: List[List[int]]) -> int:
    # ll = list()
    # Write your code here.
    # for i in range(3):
    # ll.append(f(n - 1, points, i))
    # return max(ll)
    return f(n - 1, points, 3)
