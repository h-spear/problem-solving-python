# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traversal(node):
            if low <= node.val <= high:
                self.answer += node.val

            if node.left:
                traversal(node.left)
            if node.right:
                traversal(node.right)

        self.answer = 0
        traversal(root)
        return self.answer
