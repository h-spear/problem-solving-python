# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        def preorderHelper(x):
            result.append(x.val)

            if x.left:
                preorderHelper(x.left)
            if x.right:
                preorderHelper(x.right)

        preorderHelper(root)
        return result
