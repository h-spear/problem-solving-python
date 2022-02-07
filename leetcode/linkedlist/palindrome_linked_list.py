# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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


# 1. list 순회
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


# 2. 덱
# 양방향 모두 O(1)
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


# 3. Runner
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
