# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        s = set()
        q = deque([root])
        while q:
            node = q.popleft()
            s.add(node.val)

            if len(s) >= 2:
                return False

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return True
