# https://leetcode.com/problems/rotate-list/
# Runtime: 33 ms, faster than 98.50% of Python3 online submissions for Rotate List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        q = deque()
        p = head

        while p:
            q.append(p)
            p = p.next

        k %= len(q)
        if len(q) == 1:
            return head

        for _ in range(k):
            last = q.pop()
            q[-1].next = last.next
            last.next = q[0]
            q.appendleft(last)

        return q.popleft()
