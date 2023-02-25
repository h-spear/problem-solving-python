# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        arr = []
        p = head
        while p:
            arr.append(p.val)
            p = p.next

        n = len(arr)
        answer = 0
        for i in range(n):
            if arr[i]:
                answer += 2 ** (n - i - 1)

        return answer
