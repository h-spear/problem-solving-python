# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        id = 0
        for head in lists:
            p = head
            while p:
                heapq.heappush(heap, (p.val, id, p))
                p = p.next
                id += 1

        head = heap[0][2] if heap else None
        while heap:
            _, _, p = heapq.heappop(heap)
            if not heap:
                p.next = None
                break
            p.next = heap[0][2]

        return head
