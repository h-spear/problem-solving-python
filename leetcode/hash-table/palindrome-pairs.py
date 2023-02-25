# https://leetcode.com/problems/palindrome-pairs/
# https://leetcode.com/problems/palindrome-pairs/discuss/2586194/Python-Hashmap-Solution-oror-85-faster-runtime-oror-67-faster-memory-usage


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        answer = []
        hashmap = {}
        n = len(words)

        for i, word in enumerate(words):
            hashmap[word] = i

        for i in range(n):
            word = words[i]

            # case1
            if word[::-1] in hashmap:
                indice = hashmap[word[::-1]]
                if i != indice:
                    answer.append([i, indice])

            # case2
            if word != "" and "" in hashmap and word == word[::-1]:
                indice = hashmap[""]

                answer.append([i, indice])
                answer.append([indice, i])

            # case3
            for j in range(1, len(word)):
                if word[j:][::-1] in hashmap and word[:j] == word[:j][::-1]:
                    indice = hashmap[word[j:][::-1]]
                    if i != indice:
                        answer.append([indice, i])

                if word[:j][::-1] in hashmap and word[j:] == word[j:][::-1]:
                    indice = hashmap[word[:j][::-1]]
                    if i != indice:
                        answer.append([i, indice])

        return answer


# TLE
# https://leetcode.com/problems/palindrome-pairs/discuss/1987826/Python-Trie-solution-explained

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False
        self.idx = -1
        self.palindrome_idxs = []


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def is_palindrome(self, s):
        return s == s[::-1]

    def search(self, word, idx, res):
        p = self.root
        for i in range(len(word)):
            if p.end and self.is_palindrome(word[i:]):
                res.append([idx, p.idx])

            if word[i] not in p.children:
                return
            p = p.children[word[i]]

        if p.end and p.idx != idx:
            res.append([p.idx, idx])

        for pidx in p.palindrome_idxs:
            res.append([idx, pidx])

        return

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        output = []

        for i in range(n):
            p = self.root
            r_word = words[i][::-1]

            for j in range(len(r_word)):
                if self.is_palindrome(r_word[j:]):
                    p.palindrome_idxs.append(i)

                p = p.children[r_word[j]]

            p.end = True
            p.idx = i

        for i in range(n):
            self.search(words[i], i, output)

        return output


# TLE
# https://www.youtube.com/watch?v=SSq0xH51pZQ
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word, left, right):
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True

        n = len(words)
        answer = []
        _hash = {w: i for i, w in enumerate(words)}
        for i in range(n):
            word = words[i]
            # 1
            if word == "":
                for j in range(n):
                    if i != j and is_palindrome(words[j], 0, len(words[j]) - 1):
                        answer.append([i, j])
                        answer.append([j, i])
                continue

            # 2
            r_word = word[::-1]
            if r_word in _hash and _hash[r_word] != i:
                answer.append([i, _hash[r_word]])

            # 3
            for k in range(1, len(word)):
                if is_palindrome(word, 0, k - 1) and word[k:][::-1] in _hash:
                    answer.append([_hash[word[k:][::-1]], i])
                if is_palindrome(word, k, len(word) - 1) and word[:k][::-1] in _hash:
                    answer.append([i, _hash[word[:k][::-1]]])

        return answer
