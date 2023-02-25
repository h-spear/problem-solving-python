# https://leetcode.com/problems/design-linked-list/


class ListNode:
    def __init__(self, val=0, prev=None, _next=None):
        self.prev = prev
        self.next = _next
        self.val = val


class MyLinkedList:
    def __init__(self):
        head = ListNode()
        tail = ListNode()
        head.next, head.prev = tail, tail
        tail.next, tail.prev = head, head

        self.head = head
        self.tail = tail
        self.count = 0

    def get(self, index: int) -> int:
        if index >= self.count:
            return -1

        p = self.head.next

        while index:
            p = p.next
            index -= 1

        return p.val

    def addAtHead(self, val: int) -> None:
        head = self.head

        newnode = ListNode(val)
        head.next.prev = newnode
        newnode.next = head.next
        newnode.prev = head
        head.next = newnode
        self.count += 1

    def addAtTail(self, val: int) -> None:
        tail = self.tail

        newnode = ListNode(val)
        tail.prev.next = newnode
        newnode.prev = tail.prev
        newnode.next = tail
        tail.prev = newnode
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return

        p = self.head.next

        while index:
            p = p.next
            index -= 1

        newnode = ListNode(val)
        newnode.prev = p.prev
        newnode.next = p
        p.prev.next = newnode
        p.prev = newnode
        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.count:
            return

        removed = self.head.next

        while index and removed != self.tail:
            removed = removed.next
            index -= 1

        if removed == self.tail:
            return

        removed.prev.next = removed.next
        removed.next.prev = removed.prev
        self.count -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
