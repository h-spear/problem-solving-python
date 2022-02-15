# https://leetcode.com/problems/invert_binary_tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 재귀
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(
                root.left
            )
            return root
        return None


# BFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = collections.deque([root])
        while q:
            node = q.popleft()

            if node:
                node.left, node.right = node.right, node.left

                q.append(node.left)
                q.append(node.right)

        return root
