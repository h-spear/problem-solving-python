# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0

        answer = 0
        q = deque([(0, root)])
        while q:
            answer += 1
            for _ in range(len(q)):
                lv, node = q.popleft()

                for child in node.children:
                    q.append((lv + 1, child))

        return answer
