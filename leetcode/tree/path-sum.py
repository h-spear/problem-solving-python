# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return 0

        flag = [False]

        def helper(x, summ):
            if not x.left and not x.right and summ == targetSum:
                flag[0] = True
                return

            if flag[0]:
                return

            if x.left:
                helper(x.left, summ + x.left.val)

            if x.right:
                helper(x.right, summ + x.right.val)

        helper(root, root.val)
        return flag[0]
