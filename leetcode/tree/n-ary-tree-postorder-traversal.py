# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        if not root:
            return []

        def traversal(node):
            for child in node.children:
                traversal(child)
            answer.append(node.val)

        answer = []
        traversal(root)
        return answer
