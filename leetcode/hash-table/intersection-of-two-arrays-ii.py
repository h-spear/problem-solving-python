# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = defaultdict(int)
        answer = []
        for num in nums1:
            counter[num] += 1

        for num in nums2:
            if num in counter:
                answer.append(num)
                counter[num] -= 1
                if counter[num] == 0:
                    del counter[num]

        return answer
