# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        q = deque([root])
        while q:
            x = q.popleft()

            if x:
                q.append(x.left)
                q.append(x.right)
                result.append(str(x.val))
            else:
                result.append("null")

        return " ".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "null":
            return None

        nodes = data.split()
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q:
            x = q.popleft()

            if nodes[i] != "null":
                x.left = TreeNode(int(nodes[i]))
                q.append(x.left)
            i += 1

            if nodes[i] != "null":
                x.right = TreeNode(int(nodes[i]))
                q.append(x.right)
            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
