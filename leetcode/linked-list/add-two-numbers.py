# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        p, q, r = l1, l2, None
        a, b, c = "", "", None
        while p:
            a += str(p.val)
            p = p.next
        while q:
            b += str(q.val)
            q = q.next

        c = deque(str(int("".join(reversed(a))) + int("".join(reversed(b)))))

        while c:
            r = ListNode(c.popleft(), r)

        return r
