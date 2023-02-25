# https://leetcode.com/problems/min-stack/


class MinStack:
    INF = float("inf")

    def __init__(self):
        self.stack = []
        self.minima = self.INF

    def push(self, val: int) -> None:
        self.stack.append((val, self.minima))
        self.minima = min(self.minima, val)

    def pop(self) -> None:
        _, minima = self.stack.pop()
        self.minima = minima

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minima


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
