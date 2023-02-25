# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque, defaultdict


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        nodes_by_level = defaultdict(list)
        q = deque()
        q.append((0, root))
        while q:
            lv, node = q.popleft()
            nodes_by_level[lv].append(node)

            if node.left:
                q.append((lv + 1, node.left))
            if node.right:
                q.append((lv + 1, node.right))

        for lv in nodes_by_level:
            length = len(nodes_by_level[lv])
            for i in range(length - 1):
                nodes_by_level[lv][i].next = nodes_by_level[lv][i + 1]

        return root
