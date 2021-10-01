# https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left = []
        right = []
        num = 1
        left.append(num)
        for i in range(len(nums) - 1):
            num *= nums[i]
            left.append(num)
        num = 1
        right.append(num)
        for i in range(len(nums) - 1, 0, -1):
            num *= nums[i]
            right.append(num)
        right.reverse()

        for i in range(len(nums)):
            nums[i] = left[i] * right[i]
        return nums

    # O(n^2) : time limit exceeded
    def productExceptSelf_error(self, nums: list[int]) -> list[int]:
        answer = []
        for i in range(len(nums)):
            num = 1
            for j in range(len(nums)):
                if j != i:
                    num *= nums[j]
            answer.append(num)
        return answer


answer = Solution()
print(answer.productExceptSelf([1, 2, 3, 4]))
