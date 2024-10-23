# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return list()

        q = list()
        level_order = list()
        q.append(root)

        while q:
            curr_level = list()
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                curr_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_order.append(curr_level)

        return level_order
