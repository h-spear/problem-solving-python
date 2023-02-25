# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binstr_to_int(s: str) -> int:
            n = len(s)
            num = 0
            for i in range(n):
                if s[n - i - 1] == "1":
                    num += 1 << i
            return num

        def int_to_binstr(num: int) -> str:
            binstr = ""

            while num:
                if num & 1:
                    binstr += "1"
                else:
                    binstr += "0"
                num >>= 1
            if binstr == "":
                return "0"
            return binstr[::-1]

        num = binstr_to_int(a) + binstr_to_int(b)
        return int_to_binstr(num)
