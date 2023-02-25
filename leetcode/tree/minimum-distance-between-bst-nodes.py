# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []
        q = deque([root])
        while q:
            node = q.popleft()
            values.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        values.sort()
        answer = float("inf")
        for i in range(len(values) - 1):
            answer = min(answer, values[i + 1] - values[i])

        return answer
