from os import *
from sys import *
from collections import *
from math import *


def include(arr, ind, n, k, curr_sum):
    if ind < 0:
        return False
    elif curr_sum + arr[ind] == k:
        return True
    else:
        not_take = include(arr, ind - 1, n, k, curr_sum)
        take = include(arr, ind - 1, n, k, curr_sum + arr[ind])

    return not_take or take


def subsetSumToK(n, k, arr):
    curr_sum = 0
    n = len(arr)
    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    return include(arr, n - 1, n, k, curr_sum)
