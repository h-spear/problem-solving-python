# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(x, is_left):
            if not x:
                return 0
            if not x.left and not x.right and is_left == True:
                return x.val

            return helper(x.left, True) + helper(x.right, False)

        return helper(root, False)
