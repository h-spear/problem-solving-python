# https://leetcode.com/problems/longest-palindromic-substring/

# 99.03%
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(left, right):
            while left >= 0 and right < n:
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1

            return s[left + 1 : right]

        if n <= 1 or s == s[::-1]:
            return s

        max_len = 0
        answer = ""
        for i in range(0, n):
            cand1 = expand(i, i + 1)
            cand2 = expand(i, i + 2)
            if max_len < len(cand1):
                max_len = len(cand1)
                answer = cand1
            if max_len < len(cand2):
                max_len = len(cand2)
                answer = cand2
            # oneline
            # answer = max(answer, expand(i, i + 1), expand(i, i + 2), key=len)

        return answer


# bruteforce: 시간초과
class Solution:
    def longestPalindrome(self, s: str) -> str:
        checker = dict()
        n = len(s)

        def is_palindrome(string):
            if string in checker:
                return checker[string]

            ls = len(string)
            for i in range(ls // 2):
                if string[i] != string[ls - 1 - i]:
                    checker[string] = False
                    break
            else:
                checker[string] = True

            return checker[string]

        max_len = 0
        answer = ""
        for i in range(n):
            for j in range(i + 1):
                string = s[i - j : i + 1]
                if is_palindrome(string):
                    if max_len < j + 1:
                        max_len = j + 1
                        answer = string

        return answer
