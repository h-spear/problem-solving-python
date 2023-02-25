# https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if 0 in nums:
            idx = nums.index(0)
            others = 1
            for i in range(n):
                if i == idx:
                    continue
                others *= nums[i]

            for i in range(n):
                if i == idx:
                    nums[i] = others
                else:
                    nums[i] = 0
        else:
            all_product = 1
            for num in nums:
                all_product *= num
            for i in range(n):
                nums[i] = all_product // nums[i]

        return nums
