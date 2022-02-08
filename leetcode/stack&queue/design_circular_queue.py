# https://leetcode.com/problems/design-circular-queue/submissions/
# k칸의 환형 큐를 구현하기 위하여 k+1개의 공간을 사용하는 방식으로 구현함
# 정확히 k칸의 공간만 사용하여 구현하는 방법도 있음


class MyCircularQueue:
    def __init__(self, k: int):
        self._front = 0
        self._rear = 0
        self._size = k + 1
        self.queue = [-1] * (k + 1)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self._rear] = value
        self._rear = (self._rear + 1) % self._size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        item = self.queue[self._front]
        self.queue[self._front] = -1
        self._front = (self._front + 1) % self._size
        return True

    def Front(self) -> int:
        return self.queue[self._front]

    def Rear(self) -> int:
        return self.queue[(self._rear - 1) % self._size]

    def isEmpty(self) -> bool:
        return self._front == self._rear

    def isFull(self) -> bool:
        return (self._rear + 1) % self._size == self._front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
