# https://leetcode.com/problems/sort-list/
# merge sort

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def merge_sort(self, list1, list2):
        head = ListNode()
        p = head
        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next

        while list1:
            p.next = list1
            list1 = list1.next
            p = p.next

        while list2:
            p.next = list2
            list2 = list2.next
            p = p.next

        return head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        walker = head
        runner = head.next
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next

        mid = walker
        list1 = head
        list2 = mid.next
        mid.next = None

        sorted1 = self.sortList(list1)
        sorted2 = self.sortList(list2)
        return self.merge_sort(sorted1, sorted2)
