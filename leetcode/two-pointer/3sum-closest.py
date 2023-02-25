# https://leetcode.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        opt_sum = float("inf")
        answer = 0

        for i in range(n - 2):
            find = target - nums[i]
            left = i + 1
            right = n - 1
            opt = float("inf")
            cl, cr = 0, 0
            while left < right:
                calc = abs(find - nums[left] - nums[right])
                if calc < opt:
                    opt = calc
                    cl, cr = left, right

                if nums[left] + nums[right] < find:
                    left += 1
                else:
                    right -= 1

            summ = nums[i] + nums[cl] + nums[cr]
            calc = abs(target - summ)
            if opt_sum > calc:
                opt_sum = calc
                answer = summ

        return answer
