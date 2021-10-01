# https://leetcode.com/problems/3sum/
# two pointer (O(n^2))
# 같은 원소를 생략함으로써 시간을 많이 단축할 수 있었더
# 8321ms -> 1번 단축 -> 4865ms -> 2번단축 -> 1197ms


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = []
        print(nums)
        for i in range(len(nums)):
            # 시간 단축 1 : 같은 원소인 경우 아래 과정 생략
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            now = nums[i]
            target = -now

            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    answer.append([now, nums[left], nums[right]])

                    # 시간 단축 2 : 같은 원소인 경우 while문 생략
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
        return answer


answer = Solution()
print(answer.threeSum([-1, 0, 1, 2, -1, -4]))


# 통과 못한 버전
# brute force 시간초과로 통과 불가(O(n^3))
#
# from itertools import combinations
#
#
# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         answer = []
#         for numbers in combinations(nums, 3):
#             if sum(numbers) == 0 and list(numbers) not in answer:
#                 answer.append(list(numbers))
#
#         return answer
#
