# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from collections import defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        word_length = len(words[0])
        word_hash = defaultdict(int)
        check_length = word_length * len(words)
        checker = None
        ls = len(s)

        for word in words:
            word_hash[word] += 1

        if ls < check_length:
            return result

        def hash_check():
            for k in word_hash:
                if k not in checker:
                    return False
                if checker[k] != word_hash[k]:
                    return False
            return True

        for i in range(ls - check_length + 1):
            flag = True
            checker = defaultdict(int)
            j = i
            while j < i + check_length:
                word = s[j : j + word_length]
                if word not in word_hash:
                    flag = False
                    break
                checker[word] += 1
                j += word_length

            if not flag:
                continue

            if hash_check():
                result.append(i)

        return result
