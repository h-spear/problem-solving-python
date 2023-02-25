# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def is_pseudo_palindromic():
            odd = 0
            for cnt in counter.values():
                if cnt & 1:
                    odd += 1
                    if odd >= 2:
                        return False
            return True

        def helper(node):
            counter[node.val] += 1

            if not node.left and not node.right:
                answer[0] += is_pseudo_palindromic()
                counter[node.val] -= 1
                return

            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

            counter[node.val] -= 1

        counter = defaultdict(int)
        answer = [0]
        helper(root)
        return answer[0]
