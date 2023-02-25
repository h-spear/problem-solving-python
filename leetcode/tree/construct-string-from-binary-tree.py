# https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = ""

    def tree2str(self, root: Optional[TreeNode]) -> str:

        self.answer = ""

        def helper(node):
            self.answer += str(node.val)

            if node.left and not node.right:
                self.answer += "("
                helper(node.left)
                self.answer += ")"
                return

            if not node.left and node.right:
                self.answer += "()("
                helper(node.right)
                self.answer += ")"
                return

            if node.left and node.right:
                self.answer += "("
                helper(node.left)
                self.answer += ")"
                self.answer += "("
                helper(node.right)
                self.answer += ")"
                return

        helper(root)
        return self.answer
