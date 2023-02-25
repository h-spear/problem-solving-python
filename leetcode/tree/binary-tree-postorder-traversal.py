# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        def postorderHelper(x):

            if x.left:
                postorderHelper(x.left)
            if x.right:
                postorderHelper(x.right)
            result.append(x.val)

        postorderHelper(root)
        return result
