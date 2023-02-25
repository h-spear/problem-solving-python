# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

from collections import deque


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        q = deque(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        answer = []
        while q:
            x = q.popleft()
            num = int(x[-1])
            if len(x) == n:
                answer.append(x)
                continue

            if num + k <= 9:
                q.append(x + str(num + k))
            if k == 0:
                continue
            if num - k >= 0:
                q.append(x + str(num - k))

        return answer
