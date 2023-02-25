# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

# O(n)
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)

        for i, c in enumerate(chalk):
            k -= c
            if k < 0:
                return i
        return -1


# O(nlogn)
# binary search + prefix sum
from itertools import accumulate
from bisect import bisect_right


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        psum = list(accumulate(chalk))
        return bisect_right(psum, k % sum(chalk))
