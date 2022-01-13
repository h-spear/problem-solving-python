# Singly Linked List


class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            self.head = Node(item, self.head)
        self.size += 1

    # p가 가리키는 노드 뒤에 삽입
    def insert_after(self, item, p):
        p.next = Node(item, p.next)
        self.size += 1

    def insert_back(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            p = self.head
            while p.next != None:
                p = p.next
            self.insert_after(item, p)
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            raise EmptyError("underflow")
        self.head = self.head.next
        self.size -= 1

    # p가 가리키는 노드 다음 노드를 삭제
    def delete_after(self, p):
        if self.is_empty():
            raise EmptyError("underflow")

        t = p.next
        p.next = t.next
        self.size -= 1

    def delete_back(self):
        if self.is_empty():
            raise EmptyError("underflow")
        p = self.head
        before = None
        while p.next != None:
            before = p
            p = p.next

        if not before:
            self.head = None
            return

        self.delete_after(before)

    def show(self):
        p = self.head
        while p != None:
            print(p.elem, end=" -> ")
            p = p.next
        print("None")

    def search(self, target):
        p = self.head
        cnt = 0
        while p != None:
            if p.elem == target:
                cnt += 1
            p = p.next

        if cnt:
            print("found!", cnt)
        else:
            print("not found")


class EmptyError(Exception):
    pass


List = LinkedList()
List.insert_front(1)
List.insert_front(2)
List.insert_front(3)
List.show()

List.insert_after(5, List.head)
List.show()

List.insert_back(7)
List.insert_back(8)
List.show()

List.search(7)

List.delete_back()
List.delete_back()
List.show()

List.search(7)

List.delete_after(List.head)
List.show()

List.delete_front()
List.delete_front()
List.show()

List.delete_front()
List.show()
