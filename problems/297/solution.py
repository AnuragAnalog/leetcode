# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.h = 0

    def get_height(self, root, level):
        if root is None:
            return None
        
        self.h = max(self.h, level + 1)
        self.get_height(root.left, level + 1)
        self.get_height(root.right, level + 1)

    def serial(self, root, idx):
        self.list_repr[idx] = root.val
        if root.left is not None:
            self.serial(root.left, 2*idx + 1)
        if root.right is not None:
            self.serial(root.right, 2*idx + 2)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        self.get_height(root, 0)
        self.list_repr = {-1: self.h}
        self.serial(root, 0)

        return str(list(self.list_repr.items()))

    def deserial(self, data, idx):
        if idx not in data:
            return None
        root = TreeNode(data[idx])
        if self.max_nodes - 1 >= 2*idx + 1: 
            root.left = self.deserial(data, 2*idx + 1)
        if self.max_nodes - 1 >= 2*idx + 2:
            root.right = self.deserial(data, 2*idx + 2)

        return root
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        list_repr = dict()
        for k, v in list(eval(data)):
            list_repr[k] = v
        self.max_nodes = (2**list_repr[-1])-1
        print(self.max_nodes)
        root = self.deserial(list_repr, 0)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
