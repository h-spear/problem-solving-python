# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(0, root)])
        nodes = defaultdict(list)
        while q:
            lv, x = q.popleft()
            nodes[lv].append(x.val)

            if x.left:
                q.append((lv + 1, x.left))
            if x.right:
                q.append((lv + 1, x.right))

        n = len(nodes)
        output = [[] for _ in range(n)]
        for lv in range(n):
            output[lv] = nodes[n - lv - 1]

        return output
