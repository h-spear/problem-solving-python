# https://leetcode.com/problems/array-partition-i/


class Solution:
    # 465ms, 나의 풀이
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        print(nums)
        answer = 0
        while len(nums) >= 2:
            nums.pop()
            answer += nums풀이op()
        return answer

    # 611ms
    def arrayPairSum2(self, nums: list[int]) -> int:
        answer = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                answer += min(pair)
                pair = []
        return answer

    # 296ms
    def arrayPairSum3(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])


answer = Solution()
print(answer.arrayPairSum([1, 4, 3, 2]))
print(answer.arrayPairSum2([1, 4, 3, 2]))
print(answer.arrayPairSum3([1, 4, 3, 2]))
