# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 123456

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def helper(node, height):
            if not node.left and not node.right:
                self.answer = min(self.answer, height)
                return

            if node.left:
                helper(node.left, height + 1)

            if node.right:
                helper(node.right, height + 1)

        helper(root, 1)
        return self.answer
