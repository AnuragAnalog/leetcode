# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.level_nodes = dict()

    def levelOrder(self, root, level):
        if root is None:
            return None
        else:
            if level not in self.level_nodes:
                self.level_nodes[level] = 0
            self.level_nodes[level] += root.val
            self.levelOrder(root.left, level + 1)
            self.levelOrder(root.right, level + 1)

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        self.levelOrder(root, 0)
        try:
            return sorted(self.level_nodes.values(), reverse=True)[k-1]
        except:
            return -1
