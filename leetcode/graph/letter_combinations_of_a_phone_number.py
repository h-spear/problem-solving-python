# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(s="", i=0):
            if i == len(digits):
                if s:
                    answer.append(s)
                return
            now = digits[i]
            for char in chars[now]:
                dfs(s + char, i + 1)

        dfs()
        return answer
