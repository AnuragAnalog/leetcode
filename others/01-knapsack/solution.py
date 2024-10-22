from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.

def knapsack01(ind, weights, values, W):
    if W == 0:
        return 0

    if ind == 0:
        if weights[ind] <= W:
            return values[ind]
        else:
            return 0
    
    p1 = 0
    if weights[ind] <= W:
        p1 = values[ind] + knapsack01(ind - 1, weights, values, W - weights[ind])
    p2 = knapsack01(ind - 1, weights, values, W)

    return max(p1, p2)
    
t = int(input())

for _ in range(t):
    n = int(input())
    wi = list(map(int, input().split()))
    vi = list(map(int, input().split()))
    W = int(input())

    res = knapsack01(n-1, wi, vi, W)
    print(res)
