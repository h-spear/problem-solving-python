# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import defaultdict, deque


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []

        nodes_by_level = defaultdict(list)
        q = deque([(0, root)])
        max_level = 0
        while q:
            lv, node = q.popleft()
            max_level = max(max_level, lv)

            nodes_by_level[lv].append(node.val)

            for child in node.children:
                q.append((lv + 1, child))

        output = [[] for _ in range(max_level + 1)]

        for lv in nodes_by_level:
            output[lv] = nodes_by_level[lv]

        return output
