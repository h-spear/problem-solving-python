# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        manhatan = 123456789
        idx = -1

        for i, (_x, _y) in enumerate(points):
            if x != _x and y != _y:
                continue

            distance = abs(x - _x) + abs(y - _y)
            if distance < manhatan:
                manhatan = distance
                idx = i

        return idx
