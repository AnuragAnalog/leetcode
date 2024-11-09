# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, root, curr_sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            if curr_sum == root.val:
                return True
        
        return self.search(root.left, curr_sum - root.val) or self.search(root.right, curr_sum - root.val)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.search(root, targetSum)
