# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def helper(x):
            if x.val > val:
                if not x.left:
                    x.left = TreeNode(val)
                else:
                    helper(x.left)
            else:
                if not x.right:
                    x.right = TreeNode(val)
                else:
                    helper(x.right)

        helper(root)
        return root
