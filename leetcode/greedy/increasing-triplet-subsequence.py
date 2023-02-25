# https://leetcode.com/problems/increasing-triplet-subsequence/


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        INF = float("inf")
        one, two, three = INF, INF, INF

        for num in nums:
            one = min(one, num)

            if num > one:
                two = min(two, num)

            if num > two:
                three = min(three, num)

        return three != INF
