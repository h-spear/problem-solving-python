# https://leetcode.com/problems/shuffle-an-array/

import random


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.size = len(nums)

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        checker = set()
        nums = self.nums
        rand_indices = []
        rand_array = []
        for _ in range(self.size):
            indice = random.randint(0, self.size - 1)
            while indice in checker:
                indice = random.randint(0, self.size - 1)
            rand_indices.append(indice)
            checker.add(indice)

        for indice in rand_indices:
            rand_array.append(nums[indice])

        return rand_array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
