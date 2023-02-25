# https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        depth_x = -1
        depth_y = -1
        parent_x = -1
        parent_y = -1

        q = deque([(0, root)])
        while q:
            lv, node = q.popleft()

            for nnode in [node.left, node.right]:
                if nnode:
                    q.append((lv + 1, nnode))
                    if nnode.val == x:
                        depth_x = lv + 1
                        parent_x = node.val
                    elif nnode.val == y:
                        depth_y = lv + 1
                        parent_y = node.val

        return parent_x != parent_y and depth_x == depth_y
