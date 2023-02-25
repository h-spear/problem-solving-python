# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# https://www.youtube.com/watch?v=18ncLrRKGiM

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    indexer = {}

    def construct(self, inorder, preorder, i_start, p_start, size):
        if size <= 0:
            return None

        root_v = preorder[p_start]
        left_size = self.indexer[root_v] - i_start
        right_size = size - left_size - 1
        left = self.construct(inorder, preorder, i_start, p_start + 1, left_size)
        right = self.construct(
            inorder,
            preorder,
            i_start + left_size + 1,
            p_start + left_size + 1,
            right_size,
        )
        return TreeNode(root_v, left, right)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i, v in enumerate(inorder):
            self.indexer[v] = i

        return self.construct(inorder, preorder, 0, 0, len(inorder))
