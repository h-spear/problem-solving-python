# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(list)
        q = deque([(0, 0, root)])
        while q:
            col, lv, node = q.popleft()
            nodes[col].append((lv, node.val))

            if node.left:
                q.append((col - 1, lv + 1, node.left))
            if node.right:
                q.append((col + 1, lv + 1, node.right))

        output = []
        keys = sorted(nodes.keys())
        for key in keys:
            nodes[key].sort()
            temp = []
            for lv, val in nodes[key]:
                temp.append(val)
            output.append(temp)

        return output
