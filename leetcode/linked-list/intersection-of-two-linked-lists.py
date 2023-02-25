# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        la = 0
        lb = 0

        p = headA
        q = headB
        long = None
        short = None

        while p:
            la += 1
            p = p.next

        while q:
            lb += 1
            q = q.next

        if la > lb:
            long = headA
            short = headB
        else:
            long = headB
            short = headA

        diff = abs(la - lb)
        while diff:
            long = long.next
            diff -= 1

        while long is not short:
            long = long.next
            short = short.next

        return long
