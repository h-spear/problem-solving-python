# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

from functools import cmp_to_key


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def compare(a, b):
            orga = a
            orgb = b
            cnta = 0
            cntb = 0

            while a:
                if a & 1:
                    cnta += 1

                a >>= 1

            while b:
                if b & 1:
                    cntb += 1

                b >>= 1

            if cnta < cntb:
                return -1
            elif cnta > cntb:
                return 1

            if orga < orgb:
                return -1
            else:
                return 1

        arr.sort(key=cmp_to_key(compare))

        return arr
