# https://leetcode.com/problems/add-two-numbers-ii/

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
        stack1 = []
        stack2 = []
        queue = deque()
        p, q = l1, l2
        while p:
            stack1.append(p.val)
            p = p.next
        while q:
            stack2.append(q.val)
            q = q.next

        carry = 0
        while stack1 and stack2:
            one = stack1.pop()
            two = stack2.pop()
            adder = one + two + carry
            queue.append(adder % 10)
            carry = adder // 10

        while stack1:
            adder = stack1.pop() + carry
            queue.append(adder % 10)
            carry = adder // 10

        while stack2:
            adder = stack2.pop() + carry
            queue.append(adder % 10)
            carry = adder // 10

        while carry:
            queue.append(carry % 10)
            carry //= 10

        ans = None
        while queue:
            ans = ListNode(queue.popleft(), ans)

        return ans
