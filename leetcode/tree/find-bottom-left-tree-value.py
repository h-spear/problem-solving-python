# https://leetcode.com/problems/find-bottom-left-tree-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        nodes = defaultdict(list)
        q = deque([(0, root)])
        max_lv = 0
        while q:
            lv, node = q.popleft()
            nodes[lv].append(node.val)
            max_lv = max(max_lv, lv)

            if node.left:
                q.append((lv + 1, node.left))
            if node.right:
                q.append((lv + 1, node.right))

        return nodes[max_lv][0]
