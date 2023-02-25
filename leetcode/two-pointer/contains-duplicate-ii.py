# https://leetcode.com/problems/contains-duplicate-ii/


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        counter = set()
        for i in range(min(k + 1, n)):
            if nums[i] in counter:
                return True
            counter.add(nums[i])

        i = 0
        j = min(k + 1, n)
        while j < n:
            counter.remove(nums[i])
            i += 1
            if nums[j] in counter:
                return True
            counter.add(nums[j])
            j += 1

        return False
