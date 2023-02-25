# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Runtime: 42 ms, faster than 99.61% of Python3 online submissions for Average of Levels in Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        vals = defaultdict(list)
        q = deque([(0, root)])
        while q:
            lv, node = q.popleft()

            vals[lv].append(node.val)

            if node.left:
                q.append((lv + 1, node.left))
            if node.right:
                q.append((lv + 1, node.right))

        answer = [0] * len(vals)
        for lv in vals:
            answer[lv] = sum(vals[lv]) / len(vals[lv])

        return answer
