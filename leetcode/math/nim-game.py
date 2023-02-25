# https://leetcode.com/problems/nim-game/


class Solution:
    def canWinNim(self, n: int) -> bool:
        res = [False, True, True, True]
        return res[n % 4]
