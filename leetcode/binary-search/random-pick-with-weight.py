# https://leetcode.com/problems/random-pick-with-weight/

import random
from bisect import bisect_left


class Solution:
    def __init__(self, w: List[int]):
        psum = [w[0]]
        for i in range(1, len(w)):
            psum.append(psum[-1] + w[i])
        self.w = w
        self.psum = psum

    def pickIndex(self) -> int:
        randint = random.randrange(1, self.psum[-1] + 1)
        idx = bisect_left(self.psum, randint)
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
