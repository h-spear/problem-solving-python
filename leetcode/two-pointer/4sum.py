# https://leetcode.com/problems/4sum/


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        output = []

        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l = j + 1
                r = length - 1
                tgt = target - nums[i] - nums[j]

                while l < r:
                    cal = nums[l] + nums[r]
                    if cal == tgt:
                        output.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                    elif cal < tgt:
                        l += 1
                    else:
                        r -= 1

        return output
