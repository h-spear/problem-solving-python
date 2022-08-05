# https://school.programmers.co.kr/learn/courses/30/lessons/60060
# Trie

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.cnt = 0
        self.is_word = False
        self.children = defaultdict(TrieNode)
        self.word_length = defaultdict(int)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        lw = len(word)
        node = self.root
        node.cnt += 1
        node.word_length[lw] += 1
        for char in word:
            node = node.children[char]
            node.cnt += 1
            node.word_length[lw] += 1
        node.is_word = True

    def search(self, word):
        lw = len(word)
        node = self.root
        for char in word:
            if char == "?":
                return node.word_length[lw]
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.word_length[lw]


def solution(words, queries):
    answer = []
    trie = Trie()
    trie_rev = Trie()
    prefix_query = []
    suffix_query = []
    result = [0] * len(queries)

    for idx, query in enumerate(queries):
        if query[0] == "?":
            prefix_query.append((idx, query[::-1]))
        else:
            suffix_query.append((idx, query))

    for word in words:
        trie.insert(word)
        trie_rev.insert(word[::-1])

    for idx, query in prefix_query:
        result[idx] += trie_rev.search(query)

    for idx, query in suffix_query:
        result[idx] += trie.search(query)

    return result
