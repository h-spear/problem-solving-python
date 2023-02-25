# https://leetcode.com/problems/reordered-power-of-2/

from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        counter = Counter(str(n))

        for i in range(30):
            power = str(1 << i)
            if counter == Counter(power):
                return True
        return False
