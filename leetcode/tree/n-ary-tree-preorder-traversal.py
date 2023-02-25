# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        def traversal(x):
            if not x:
                return
            result.append(x.val)
            for y in x.children:
                traversal(y)

        result = []
        traversal(root)
        return result
