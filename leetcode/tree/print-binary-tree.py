# https://leetcode.com/problems/print-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def get_height(self, root):
        q = deque([(0, root)])
        max_lv = 0
        while q:
            lv, node = q.popleft()
            max_lv = max(max_lv, lv)

            if node.left:
                q.append((lv + 1, node.left))
            if node.right:
                q.append((lv + 1, node.right))
        return max_lv

    def dfs(self, node, height, r, c, res):
        res[r][c] = str(node.val)

        d = height - r - 1
        if node.left:
            self.dfs(node.left, height, r + 1, c - 2 ** d, res)
        if node.right:
            self.dfs(node.right, height, r + 1, c + 2 ** d, res)

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.get_height(root)
        m = height + 1
        n = 2 ** m - 1
        res = [[""] * n for _ in range(m)]
        self.dfs(root, height, 0, (n - 1) // 2, res)
        return res
