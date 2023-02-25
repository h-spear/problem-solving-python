# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/


class Solution:
    def minimumSum(self, num: int) -> int:
        li = list(str(num))
        li.sort()
        new1 = int(li[0] + li[2])
        new2 = int(li[1] + li[3])
        return new1 + new2
