# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        answer = 0
        for x in words:
            if x not in counter:
                continue

            rev_x = x[::-1]
            if rev_x == x:
                continue

            if rev_x in counter:
                counter[x] -= 1
                if counter[x] == 0:
                    del counter[x]

                counter[rev_x] -= 1
                if counter[rev_x] == 0:
                    del counter[rev_x]

                answer += 4

        for x in counter:
            if x == x[::-1] and counter[x] >= 2:
                answer += (counter[x] // 2) * 4
                counter[x] %= 2

        for x in counter:
            if counter[x] == 0:
                continue
            if x == x[::-1]:
                answer += 2
                break

        return answer
