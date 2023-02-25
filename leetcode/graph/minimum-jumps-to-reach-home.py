# https://leetcode.com/problems/minimum-jumps-to-reach-home/submissions/
# https://leetcode.com/problems/minimum-jumps-to-reach-home/discuss/2376123/Python-3-BFS
# backward 먼저 queue에 넣어도 동작함. why?

from collections import deque


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        n = max([x] + forbidden) + a + b + 1

        visited = set()
        for f in forbidden:
            visited.add(f)

        q = deque([(0, True)])
        visited.add(0)
        count = -1

        while q:
            count += 1
            for _ in range(len(q)):
                now, back = q.popleft()

                if now == x:
                    return count

                _next = now - b
                if _next > 0 and back and _next not in visited:
                    visited.add(_next)
                    q.append((_next, False))

                _next = now + a
                if _next < n and _next not in visited:
                    visited.add(_next)
                    q.append((_next, True))

        return -1
