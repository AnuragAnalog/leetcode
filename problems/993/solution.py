# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, parent, root, level):
        if root is None:
            return

        self.inOrder(root, root.left, level + 1)
        self.node_info[root.val] = [level, parent]
        self.inOrder(root, root.right, level + 1)

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.node_info = {
            x: [None, -1],
            y: [None, -1]
        }

        self.inOrder(root, root.left, 1)
        self.inOrder(root, root.right, 1)

        if (self.node_info[x][0] == self.node_info[y][0]) and (self.node_info[x][1] != self.node_info[y][1]):
            return True
        return False
