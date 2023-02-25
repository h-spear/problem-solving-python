# https://leetcode.com/problems/sum-of-square-numbers/

# left, right 1씩 감소
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5)
        while left <= right:
            summ = left ** 2 + right ** 2
            if summ == c:
                return True
            elif summ > c:
                right -= 1
            else:
                left += 1
        return False


# slow
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True

        def find_b(a, c):
            target = c - a ** 2
            left = 0
            right = c
            while left <= right:
                mid = (left + right) // 2
                temp = mid ** 2
                if temp == target:
                    return True
                elif temp > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        for a in range(0, int(c ** 0.5) + 1):
            if find_b(a, c):
                return True
        return False
