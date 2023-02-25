# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None

        while node:
            _next, node.next = node.next, prev
            prev, node = node, _next
        return prev


class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        forward = head
        rev = None
        while forward:
            rev, rev.next, forward = forward, rev, forward.next
        return rev
