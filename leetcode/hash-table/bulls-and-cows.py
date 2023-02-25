# https://leetcode.com/problems/bulls-and-cows/

from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0

        counter = Counter(secret)
        for char in guess:
            if char in counter:
                b += 1
                counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]

        for c1, c2 in zip(secret, guess):
            if c1 == c2:
                a += 1
                b -= 1

        return "%dA%dB" % (a, b)
