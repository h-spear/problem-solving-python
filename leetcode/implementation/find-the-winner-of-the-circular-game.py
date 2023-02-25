# https://leetcode.com/problems/find-the-winner-of-the-circular-game/
# queue

from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque([i for i in range(1, n + 1)])
        while len(q) > 1:
            for _ in range(k - 1):
                q.append(q.popleft())

            q.popleft()

        return q[0]


# recursive
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return 1 if n == 1 else (self.findTheWinner(n - 1, k) + k - 1) % n + 1
