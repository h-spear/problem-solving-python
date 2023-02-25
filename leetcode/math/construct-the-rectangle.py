# https://leetcode.com/problems/construct-the-rectangle/


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        middle = int(area ** 0.5)
        for l in range(middle, area + 1):
            w = area // l
            if l < w:
                continue

            if l * w == area:
                return [l, w]

        return None
