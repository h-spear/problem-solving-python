# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        p = head
        while p:
            q.append(p)
            p = p.next

        p = q.popleft()
        flag = 1
        while q:
            if flag:
                p.next = q.pop()
                flag = 0
            else:
                p.next = q.popleft()
                flag = 1
            p = p.next

        p.next = None

        return head
