# https://leetcode.com/problems/hamming-distance/


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        answer = 0
        for a, b in zip(bin(x)[2:].zfill(32), bin(y)[2:].zfill(32)):
            if a != b:
                answer += 1
        return answer
