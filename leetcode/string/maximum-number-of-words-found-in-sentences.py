# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer = 0
        for sentence in sentences:
            l = len(sentence.split())
            answer = max(l, answer)

        return answer
