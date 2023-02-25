# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(pnode, qnode):
            if not self.answer:
                return

            if not pnode and not qnode:
                return
            elif not pnode or not qnode:
                self.answer = False
                return

            if pnode.val != qnode.val:
                self.answer = False
                return

            dfs(pnode.left, qnode.left)
            dfs(pnode.right, qnode.right)

        dfs(p, q)
        return self.answer
