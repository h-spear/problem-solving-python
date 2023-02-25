# https://leetcode.com/problems/path-sum-ii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = None
    path = None
    targetSum = 0

    def helper(self, node, curr):
        curr += node.val
        if not node.left and not node.right and curr == self.targetSum:
            self.answer.append(self.path.copy())
            return

        if node.left:
            self.path.append(node.left.val)
            self.helper(node.left, curr)
            self.path.pop()
        if node.right:
            self.path.append(node.right.val)
            self.helper(node.right, curr)
            self.path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return root

        self.targetSum = targetSum
        self.answer = []
        self.path = []
        self.path.append(root.val)
        self.helper(root, 0)
        return self.answer
