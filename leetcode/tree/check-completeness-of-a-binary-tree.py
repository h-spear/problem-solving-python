# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([(0, root)])
        nodes = []
        nodes.append(root.val)
        while q:
            lv, node = q.popleft()
            if node.left:
                q.append((lv + 1, node.left))
                nodes.append(node.left.val)
            else:
                nodes.append(-1)
            if node.right:
                q.append((lv + 1, node.right))
                nodes.append(node.right.val)
            else:
                nodes.append(-1)

        for i in range(len(nodes) - 1):
            if nodes[i] == -1 and nodes[i + 1] != -1:
                return False

        return True
