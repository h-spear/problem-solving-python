# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = defaultdict(int)
        q = deque([(1, root)])
        while q:
            depth, node = q.popleft()
            sums[depth] += node.val

            if node.left:
                q.append((depth + 1, node.left))
            if node.right:
                q.append((depth + 1, node.right))

        return sorted(sums.items(), key=lambda x: (-x[1], x[0]))[0][0]
