# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:
    def __init__(self):
        self.enstack = []
        self.destack = []

    def push(self, x: int) -> None:
        self.enstack.append(x)

    def pop(self) -> int:
        if self.destack:
            return self.destack.pop()

        while self.enstack:
            item = self.enstack.pop()
            self.destack.append(item)

        if not self.destack:
            raise Exception("underflow")
        return self.destack.pop()

    def peek(self) -> int:
        if self.destack:
            return self.destack[-1]

        while self.enstack:
            item = self.enstack.pop()
            self.destack.append(item)

        if not self.destack:
            raise Exception("underflow")
        return self.destack[-1]

    def empty(self) -> bool:
        if self.destack:
            return False
        if self.enstack:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
