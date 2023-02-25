# https://leetcode.com/problems/reduce-array-size-to-the-half/

from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total_cnt = len(arr)
        counter = Counter(arr)
        bound = total_cnt // 2

        li = [v for v in counter.values()]
        li.sort(reverse=True)
        remove_cnt = 0
        for i in range(len(counter)):
            remove_cnt += li[i]

            if total_cnt - remove_cnt <= bound:
                return i + 1

        return -1
