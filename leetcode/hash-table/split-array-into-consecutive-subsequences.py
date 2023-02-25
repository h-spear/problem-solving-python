# https://leetcode.com/problems/split-array-into-consecutive-subsequences/
# https://intrepidgeeks.com/tutorial/split-array-to-consistent-sequence-split-array-is-a-continuous-subsequence

from collections import Counter, defaultdict


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        _hash = defaultdict(int)

        for num in nums:
            if counter[num] == 0:
                continue
            elif _hash[num] > 0:
                _hash[num] -= 1
                _hash[num + 1] += 1
            elif counter[num + 1] > 0 and counter[num + 2] > 0:
                counter[num + 1] -= 1
                counter[num + 2] -= 1
                _hash[num + 3] += 1
            else:
                return False
            counter[num] -= 1

        return True
