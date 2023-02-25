# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []

        def inorder(x):
            if x.left:
                inorder(x.left)
            nums.append(x.val)
            if x.right:
                inorder(x.right)

        inorder(root)
        return nums[k - 1]


# https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/2449130/Python-97-faster-solution-inorder-traversal
class Solution:
    answer = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def k_small(node, k, idx):
            if self.answer != None:
                return self.answer
            if not node:
                return idx

            idx = k_small(node.left, k, idx) + 1
            if self.answer != None:
                return self.answer

            if idx == k:
                self.answer = node.val
                return self.answer

            return k_small(node.right, k, idx)

        return k_small(root, k, 0)
