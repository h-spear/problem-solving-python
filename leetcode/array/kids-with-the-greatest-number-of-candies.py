# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        maxx = max(candies)
        for candy in candies:
            if candy + extraCandies >= maxx:
                output.append(True)
            else:
                output.append(False)
        return output
