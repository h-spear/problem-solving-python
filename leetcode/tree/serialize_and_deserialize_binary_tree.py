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
        q = deque([root])
        result = ["null"]
        while q:
            node = q.popleft()

            if node:
                q.append(node.left)
                q.append(node.right)
                result.append(str(node.val))
            else:
                result.append("null")
        return " ".join(result)

    def deserialize(self, data):
        if data == "null null":
            return None

        nodes = data.split()
        root = TreeNode(int(nodes[1]))
        q = deque([root])
        i = 2
        while q:
            node = q.popleft()

            if nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1

            if nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
