# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = defaultdict(list)
        vals = defaultdict(list)
        q = deque([(0, root)])
        max_lv = 0
        while q:
            lv, node = q.popleft()
            max_lv = max(max_lv, lv)

            if lv & 1:
                nodes[lv].append(node)
                vals[lv].append(node.val)

            if node.left:
                q.append((lv + 1, node.left))
            if node.right:
                q.append((lv + 1, node.right))

        for lv in range(1, max_lv + 1, 2):
            length = len(nodes[lv])
            for i in range(length):
                nodes[lv][i].val = vals[lv][length - i - 1]

        return root
