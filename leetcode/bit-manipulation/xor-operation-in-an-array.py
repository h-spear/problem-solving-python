# https://leetcode.com/problems/xor-operation-in-an-array/


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        answer = 0
        i = 0
        while i < n:
            num = start + 2 * i
            answer ^= num
            i += 1

        return answer
