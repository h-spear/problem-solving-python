# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import defaultdict


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root

        def dfs(x, depth):
            _hash[depth].append(x)

            if x.left:
                dfs(x.left, depth + 1)
            if x.right:
                dfs(x.right, depth + 1)

        _hash = defaultdict(list)
        dfs(root, 0)

        for level in _hash:
            nodes = _hash[level]
            length = len(nodes)
            for i in range(length - 1):
                nodes[i].next = nodes[i + 1]

        return root
