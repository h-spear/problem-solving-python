# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nums.append(node.val)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

        nums = []
        helper(root)
        nums.sort()
        answer = 1234567
        for i in range(len(nums) - 1):
            answer = min(answer, nums[i + 1] - nums[i])

        return answer
