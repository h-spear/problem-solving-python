# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        answer = []
        _hash = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        n = len(digits)

        def dfs(i, curr):
            if i == n:
                answer.append(curr)
                return

            for alpha in _hash[digits[i]]:
                dfs(i + 1, curr + alpha)

        dfs(0, "")
        return answer
