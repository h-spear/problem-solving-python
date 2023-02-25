# https://leetcode.com/problems/even-odd-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
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

        for lv in range(max_lv + 1):
            if lv & 1 == 0:
                if nodes[lv][0] & 1 == 0:
                    return False
                for i in range(1, len(nodes[lv])):
                    if nodes[lv][i] & 1 == 0:
                        return False
                    if nodes[lv][i - 1] >= nodes[lv][i]:
                        return False
            else:
                if nodes[lv][0] & 1:
                    return False
                for i in range(1, len(nodes[lv])):
                    if nodes[lv][i] & 1:
                        return False
                    if nodes[lv][i - 1] <= nodes[lv][i]:
                        return False

        return True
