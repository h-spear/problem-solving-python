# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        visited = set()
        while 1:
            temp = 0
            for char in s:
                temp += int(char) ** 2

            if temp in visited:
                return False
            if temp == 1:
                return True

            visited.add(temp)
            s = str(temp)
        return False
