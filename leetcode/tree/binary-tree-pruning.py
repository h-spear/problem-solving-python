# https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return False
            left = helper(node.left)
            right = helper(node.right)

            if not left:
                node.left = None
            if not right:
                node.right = None
            return left or right or node.val == 1

        if helper(root):
            return root
        else:
            return None
