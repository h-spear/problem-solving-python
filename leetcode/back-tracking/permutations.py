# https://leetcode.com/problems/permutations/


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(element, i):
            if i == len(nums):
                answer.append(element)
                return

            for num in nums:
                if num in element:
                    continue
                _element = element.copy()
                _element.append(num)
                dfs(_element, i + 1)

        dfs([], 0)
        return answer


# library
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums, len(nums)))
