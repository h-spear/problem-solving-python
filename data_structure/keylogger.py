# https://www.acmicpc.net/problem/5397


class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.cursur = self.head

    def insert(self, val):
        p = self.cursur
        newnode = Node(val)
        newnode.prev = p
        newnode.next = p.next
        if p.next:
            p.next.prev = newnode
        p.next = newnode
        self.cursur = newnode

    def delete(self):
        removed = self.cursur
        if removed == self.head:
            return

        if removed.prev:
            removed.prev.next = removed.next

        if removed.next:
            removed.next.prev = removed.prev

        self.cursur = removed.prev

    def cursur_shift_left(self):
        if self.cursur.prev:
            self.cursur = self.cursur.prev

    def cursur_shift_right(self):
        if self.cursur.next:
            self.cursur = self.cursur.next

    def show(self):
        if not self.head.next:
            return

        p = self.head.next
        while p:
            print(p.val, end="")
            p = p.next
        print()


for tc in range(int(input())):
    li = LinkedList()
    s = input()
    for char in s:
        if char == "<":
            li.cursur_shift_left()
        elif char == ">":
            li.cursur_shift_right()
        elif char == "-":
            li.delete()
        else:
            li.insert(char)
    li.show()
