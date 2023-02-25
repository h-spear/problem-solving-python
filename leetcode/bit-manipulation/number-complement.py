# https://leetcode.com/problems/number-complement/


class Solution:
    def findComplement(self, num: int) -> int:
        complement = ""
        for x in bin(num)[2:]:
            if x == "1":
                complement += "0"
            else:
                complement += "1"

        return int(complement, 2)
