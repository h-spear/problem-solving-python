# https://leetcode.com/problems/check-if-it-is-a-straight-line/


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates.pop()
        x2, y2 = coordinates.pop()

        # x축 평행
        if x2 == x1:
            while coordinates:
                x, y = coordinates.pop()

                if x != x1:
                    return False

            return True
        else:
            inc = (y2 - y1) / (x2 - x1)

            while coordinates:
                x, y = coordinates.pop()
                if x == x1:
                    return False

                _inc = (y - y1) / (x - x1)

                if inc != _inc:
                    return False

            return True
