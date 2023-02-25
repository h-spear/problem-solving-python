# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import bisect_left


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def helper(x):
            arr.append(x.val)

            if x.left:
                helper(x.left)
            if x.right:
                helper(x.right)

        arr = []
        helper(root)
        arr.sort()
        n = len(arr)

        for i in range(n):
            num = arr[i]
            find = k - arr[i]
            idx = bisect_left(arr[i + 1 :], find)
            if i + idx + 1 >= n:
                continue
            if arr[i + idx + 1] == find:
                return True

        return False
