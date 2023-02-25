# https://leetcode.com/problems/koko-eating-bananas/


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(k):
            t = 0
            for pile in piles:
                t += int(math.ceil(pile / k))
            return t

        left = 1
        right = int(1e9)
        answer = 0
        while left <= right:
            mid = (left + right) // 2

            if eat(mid) <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
