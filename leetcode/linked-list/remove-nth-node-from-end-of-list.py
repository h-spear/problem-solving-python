# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        walker = head
        runner = head

        while n and runner.next:
            runner = runner.next
            n -= 1

        if n:
            return head.next

        while walker.next and runner.next:
            walker = walker.next
            runner = runner.next

        walker.next = walker.next.next

        return head
