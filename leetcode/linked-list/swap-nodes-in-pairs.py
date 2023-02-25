# https://leetcode.com/problems/swap-nodes-in-pairs/
# value만 swap

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p and p.next:
            p.val, p.next.val = p.next.val, p.val
            p = p.next.next

        return head
