from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.

def knapsack01(ind, weights, values, W, dp):
    if ind == 0:
        if weights[0] <= W:
            return values[0]
        return 0

    if dp[ind][W] != -1:
        return dp[ind][W]
    
    p1 = 0
    if weights[ind] <= W:
        p1 = values[ind] + knapsack01(ind - 1, weights, values, W - weights[ind], dp)
    p2 = knapsack01(ind - 1, weights, values, W, dp)

    dp[ind][W] = max(p1, p2)

    return dp[ind][W]
    
t = int(input())

for _ in range(t):
    n = int(input())
    wi = list(map(int, input().split()))
    vi = list(map(int, input().split()))
    W = int(input())

    dp = [[-1] * (W+1) for _ in range(n)]

    res = knapsack01(n-1, wi, vi, W, dp)
    print(res)
