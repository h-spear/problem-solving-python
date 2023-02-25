# https://leetcode.com/problems/repeated-dna-sequences/


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        checker = set()
        answer = set()
        for i in range(n - 9):
            save = s[i : i + 10]
            if save in checker:
                answer.add(save)
            else:
                checker.add(save)

        answer = list(answer)
        for x in answer:
            x = list(x)

        return answer
