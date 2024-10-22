# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.values = list()

    def inOrder(self, root):
        if root is None:
            return None
        else:
            self.inOrder(root.left)
            self.values.append(root.val)
            self.inOrder(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inOrder(root)

        return self.values[k - 1]
