# https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def helper(node):
            self.answer += 1

            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

        helper(root)
        return self.answer
