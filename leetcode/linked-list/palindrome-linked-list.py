# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 98.51%
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        walker = head
        runner = head
        rev = None
        while runner and runner.next:
            runner = runner.next.next
            rev, rev.next, walker = walker, rev, walker.next

        if runner:
            walker = walker.next

        while rev and rev.val == walker.val:
            walker = walker.next
            rev = rev.next

        return not rev


# 2
from collections import deque


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = deque()
        p = head
        while p != None:
            q.append(p.val)
            p = p.next

        while len(q) >= 2:
            if q.pop() != q.popleft():
                return False
        return True


# 3
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = []
        p = head
        while p != None:
            tmp.append(p.val)
            p = p.next

        for i in range(len(tmp) // 2):
            if tmp[i] != tmp[len(tmp) - i - 1]:
                return False
        return True
