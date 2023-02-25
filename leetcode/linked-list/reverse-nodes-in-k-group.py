# https://leetcode.com/problems/reverse-nodes-in-k-group/
# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/2513416/Python-easy-to-read-and-understand-or-recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def f(self, head, k):
        node, count = head, k
        while node and count:
            node = node.next
            count -= 1
        
        if count:
            return head
        
        prev = None
        temp = head
        for i in range(k):
            _next = head.next
            head.next = prev
            prev = head
            head = _next
        temp.next = self.f(head, k)
        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.f(head, k)