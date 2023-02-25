# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from bisect import bisect_left


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for idx, number in enumerate(numbers):
            find = target - number

            f_idx = bisect_left(numbers[idx + 1 :], find)

            if f_idx + idx + 1 >= n:
                continue
            if numbers[f_idx + idx + 1] == find:
                return [idx + 1, f_idx + idx + 2]

        return []
