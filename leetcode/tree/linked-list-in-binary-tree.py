# https://leetcode.com/problems/linked-list-in-binary-tree/
# https://leetcode.com/problems/linked-list-in-binary-tree/discuss/2022374/Easy-python-solution-with-recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, head, root):
        if not head:
            return True

        left_check = False
        if root.left and head.val == root.left.val:
            left_check = self.helper(head.next, root.left)

        right_check = False
        if root.right and head.val == root.right.val:
            right_check = self.helper(head.next, root.right)

        return left_check or right_check

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        if not root:
            return False

        if root.val == head.val:
            if self.helper(head.next, root):
                return True

        left_check = self.isSubPath(head, root.left)
        right_check = self.isSubPath(head, root.right)
        return left_check or right_check
