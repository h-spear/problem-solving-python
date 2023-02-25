# https://leetcode.com/problems/letter-case-permutation/


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        n = len(s)

        def back_tracking(i, string):
            if i == n:
                answer.append(string)
                return

            if s[i].isdigit():
                back_tracking(i + 1, string + s[i])
            else:
                back_tracking(i + 1, string + s[i].lower())
                back_tracking(i + 1, string + s[i].upper())

        back_tracking(0, "")
        return answer
