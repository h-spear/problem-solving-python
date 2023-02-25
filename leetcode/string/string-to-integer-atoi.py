# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, s: str) -> int:
        i = ""
        negative = False
        int_max = 2 ** 31 - 1
        int_min = -(2 ** 31)

        # 1
        for idx, char in enumerate(s):
            if char == " ":
                pass
            else:
                i = s[idx:]
                break

        # 2
        if i and i[0] == "-":
            negative = True
            i = i[1:]
        elif i and i[0] == "+":
            i = i[1:]

        # 3
        for idx, char in enumerate(i):
            if char.isdigit():
                pass
            else:
                i = i[:idx]
                break

        if not i:
            return 0

        i = int(i)
        if negative:
            i *= -1

        if i < int_min:
            return int_min
        if i > int_max:
            return int_max
        return i
