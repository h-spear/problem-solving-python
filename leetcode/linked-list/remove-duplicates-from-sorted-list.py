# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import defaultdict


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        walker = head
        runner = head
        counter = defaultdict(int)

        while runner:
            v = runner.val
            counter[v] += 1
            runner = runner.next

        while walker:
            v = walker.val
            for i in range(counter[v] - 1):
                walker.next = walker.next.next
            walker = walker.next

        return head
