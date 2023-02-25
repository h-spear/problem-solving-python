# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxx):
            if node.val >= maxx:
                self.count += 1

            if node.left:
                dfs(node.left, max(maxx, node.val))
            if node.right:
                dfs(node.right, max(maxx, node.val))

        dfs(root, -10000000)
        return self.count
