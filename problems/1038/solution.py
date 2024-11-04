# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cum_sum = 0

    def cumSum(self, root):
        if root is None:
            return None
        else:
            self.cumSum(root.right)
            self.cum_sum += root.val
            root.val = self.cum_sum
            self.cumSum(root.left)
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.cumSum(root)

        return root
