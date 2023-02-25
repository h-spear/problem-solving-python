# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict


class Solution:
    answer = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = defaultdict(int)
        counter[0] = 1

        def dfs(node, summ):
            if not node:
                return

            summ += node.val
            self.answer += counter[summ - targetSum]

            counter[summ] += 1
            dfs(node.left, summ)
            dfs(node.right, summ)
            counter[summ] -= 1

        dfs(root, 0)
        return self.answer
