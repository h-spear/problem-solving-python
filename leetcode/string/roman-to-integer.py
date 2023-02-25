# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        _hash = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        n = len(s)
        num = 0

        i = 0
        while i < n:
            if i + 1 < n:
                r = s[i : i + 2]
                if r in _hash:
                    num += _hash[r]
                    i += 2
                    continue

            r = s[i]
            if r in _hash:
                num += _hash[r]
            i += 1

        return num
