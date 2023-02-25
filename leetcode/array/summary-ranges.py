# https://leetcode.com/problems/summary-ranges/


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        i = 0
        n = len(nums)
        while i < n:
            start = i
            j = i
            while j < n - 1 and nums[j] + 1 == nums[j + 1]:
                j += 1
            end = j

            ss = str(nums[start])
            if start != end:
                ss += "->" + str(nums[end])
            answer.append(ss)
            i = j + 1

        return answer
