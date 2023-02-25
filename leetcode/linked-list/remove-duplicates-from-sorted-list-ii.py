# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import defaultdict


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = defaultdict(int)
        p = head

        while p:
            counter[p.val] += 1
            p = p.next

        elem = [e for e, v in counter.items() if v == 1]

        q = None
        while elem:
            q = ListNode(elem.pop(), q)

        return q
