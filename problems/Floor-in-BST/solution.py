from os import *
from sys import *
from collections import *
from math import *

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#     Following is the TreeNode class structure

#     class TreeNode:

#         def __init__ (self, data):

#             self.data = data
#             self.left = None
#             self.right = None
            
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def search(root, X, mini):
    if root is None:
        return mini
    else:
        mini.append(root.data)
        mini = search(root.right, X, mini)
        mini = search(root.left, X, mini)

        return mini

def floorInBST(root, X):
    mini = list()
    mini = search(root, X, mini)
    final_mini = 0

    for m in sorted(mini):
        if m <= X:
            final_mini = m

    return final_mini
