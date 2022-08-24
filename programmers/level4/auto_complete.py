# https://school.programmers.co.kr/learn/courses/30/lessons/17685

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        node.count += 1
        for char in word:
            node = node.children[char]
            node.count += 1
        node.is_word = True

    def autocomplete(self, word):
        node = self.root
        length = 0
        for char in word:
            if char not in node.children:
                return -1
            if node.count == 1:
                return length
            else:
                length += 1
            node = node.children[char]
        return length


def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)

    for word in words:
        answer += trie.autocomplete(word)

    return answer
