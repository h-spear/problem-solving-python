# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    lv_p = 0
    lv_q = 0

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def find(lv, node):
            if self.lv_p and self.lv_q:
                return
            if node == p:
                self.lv_p = lv
            if node == q:
                self.lv_q = lv

            if node.left:
                find(lv + 1, node.left)
                parent[node.left] = node
            if node.right:
                find(lv + 1, node.right)
                parent[node.right] = node

        parent = defaultdict(TreeNode)
        find(1, root)

        if self.lv_p > self.lv_q:
            p, q = q, p
            self.lv_p, self.lv_q = self.lv_q, self.lv_p

        while self.lv_p != self.lv_q:
            self.lv_q -= 1
            q = parent[q]

        while p != q:
            p = parent[p]
            q = parent[q]

        return p
