# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even_head = head.next
        even = even_head
        while even.next and even.next.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        if even.next:
            odd.next = even.next
            odd = odd.next
        even.next = None

        odd.next = even_head
        return head
