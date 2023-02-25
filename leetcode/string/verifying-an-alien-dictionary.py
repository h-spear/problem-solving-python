# https://leetcode.com/problems/verifying-an-alien-dictionary/

from functools import cmp_to_key


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_hash = {}
        for i, o in enumerate(order):
            order_hash[o] = i

        def compare(a, b):
            la = len(a)
            lb = len(b)
            for i in range(min(la, lb)):
                if order_hash[a[i]] < order_hash[b[i]]:
                    return -1
                elif order_hash[a[i]] > order_hash[b[i]]:
                    return 1

            if la < lb:
                return -1
            else:
                return 1

        sorted_words = sorted(words, key=cmp_to_key(compare))

        for a, b in zip(words, sorted_words):
            if a != b:
                return False
        return True
