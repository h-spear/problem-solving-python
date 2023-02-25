# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        p = head
        while p and p.val == val:
            p = p.next

        head = p
        if not head:
            return head

        prev = p
        p = p.next
        while p:
            if p.val == val:
                prev.next = p.next
                p = p.next
            else:
                prev = prev.next
                p = p.next

        return head
