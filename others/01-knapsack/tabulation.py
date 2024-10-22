from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
    
t = int(input())

for _ in range(t):
    n = int(input())
    wi = list(map(int, input().split()))
    vi = list(map(int, input().split()))
    max_weight = int(input())

    dp = [[0] * (max_weight+1) for _ in range(n)]

    for W in range(wi[0], max_weight+1):
        dp[0][W] = vi[0]

    for ind in range(1, n):
        for W in range(max_weight+1):
            p1 = 0
            if wi[ind] <= W:
                p1 = vi[ind] + dp[ind - 1][W - wi[ind]]
            p2 = dp[ind - 1][W]

            dp[ind][W] = max(p1, p2)

    print(dp[n-1][max_weight])
