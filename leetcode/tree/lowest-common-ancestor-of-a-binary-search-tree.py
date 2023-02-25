# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        parent = defaultdict(int)
        depth_hash = defaultdict(int)

        def dfs(x, depth):
            depth_hash[x] = depth

            if x.left:
                parent[x.left] = x
                dfs(x.left, depth + 1)

            if x.right:
                parent[x.right] = x
                dfs(x.right, depth + 1)

        dfs(root, 0)

        # lca
        if depth_hash[p] > depth_hash[q]:
            p, q = q, p

        while depth_hash[p] != depth_hash[q]:
            q = parent[q]

        while p != q:
            p = parent[p]
            q = parent[q]

        return p
