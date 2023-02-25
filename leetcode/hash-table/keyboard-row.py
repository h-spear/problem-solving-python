# https://leetcode.com/problems/keyboard-row/


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        hashmap = {}
        for char in "qwertyuiopQWERTYUIOP":
            hashmap[char] = 1
        for char in "asdfghjklASDFGHJKL":
            hashmap[char] = 2
        for char in "zxcvbnmZXCVBNM":
            hashmap[char] = 3

        answer = []
        for word in words:
            s = set()
            for char in word:
                s.add(hashmap[char])
                if len(s) == 2:
                    break
            else:
                answer.append(word)

        return answer
