# https://leetcode.com/problems/subtree-of-another-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    answer = False

    def compare(self, a, b):
        q = deque()
        q.append((a, b))
        while q:
            a, b = q.popleft()

            if not a and not b:
                continue
            elif not a or not b:
                return False
            elif a.val != b.val:
                return False

            q.append((a.left, b.left))
            q.append((a.right, b.right))

        return True

    def helper(self, root, subRoot):
        if not root:
            return
        if self.compare(root, subRoot):
            self.answer = True
            return
        if self.answer:
            return

        self.helper(root.left, subRoot)
        self.helper(root.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.helper(root, subRoot)
        return self.answer
