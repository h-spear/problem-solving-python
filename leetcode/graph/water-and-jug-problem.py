# https://leetcode.com/problems/water-and-jug-problem/

from collections import deque


class Solution:
    def canMeasureWater(
        self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int
    ) -> bool:
        q = deque([(0, 0)])
        visited = set([(0, 0)])

        while q:
            a, b = q.popleft()
            if a + b == targetCapacity:
                return True

            candidates = []

            # Fill any of the jugs with water.
            candidates.append((jug1Capacity, b))
            candidates.append((a, jug2Capacity))

            # Empty any of the jugs.
            candidates.append((0, b))
            candidates.append((a, 0))

            # 1 -> 2
            if a + b <= jug2Capacity:
                candidates.append((0, a + b))
            else:
                candidates.append((a - (jug2Capacity - b), jug2Capacity))

            # 2 -> 1
            if a + b <= jug1Capacity:
                candidates.append((a + b, 0))
            else:
                candidates.append((jug1Capacity, b - (jug1Capacity - a)))

            for candidate in candidates:
                if candidate in visited:
                    continue
                q.append(candidate)
                visited.add(candidate)

        return False
