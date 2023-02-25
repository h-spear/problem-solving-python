# https://leetcode.com/problems/check-if-n-and-its-double-exist/


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set(arr)
        if 0 in s:
            if arr.count(0) >= 2:
                return True

        for num in arr:
            if num == 0:
                continue
            if num * 2 in s:
                return True
        return False
