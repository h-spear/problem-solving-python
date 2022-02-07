# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        p, q, r = list1, list2, None
        li = []
        while p and q:
            if p.val <= q.val:
                li.append(p.val)
                p = p.next
            else:
                li.append(q.val)
                q = q.next
        while p:
            li.append(p.val)
            p = p.next
        while q:
            li.append(q.val)
            q = q.next

        while li:
            r = ListNode(li.pop(), r)

        return r
