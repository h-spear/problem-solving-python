# https://www.acmicpc.net/problem/5446

import sys
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = False
        self.mark = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        self.word = True

    def marking(self, word):
        node = self.root
        for char in word:
            node.mark = 1
            node = node.children[char]
        node.mark = 1
        self.word = True

    def remove(self, word):
        node = self.root
        cnt = 0
        for char in word:
            if node.children[char].mark == 1:
                node = node.children[char]
            elif node.children[char].mark == -1:
                return cnt
            else:
                cnt += 1
                node.children[char].mark = -1
                return cnt

        return cnt + 1


input = lambda: sys.stdin.readline().rstrip()

for tc in range(int(input())):
    trie = Trie()
    delete = [input() for _ in range(int(input()))]
    for word in delete:
        trie.insert(word)

    n = int(input())
    for _ in range(n):
        trie.marking(input())

    answer = 0
    for word in delete:
        answer += trie.remove(word)
    print(answer if n != 0 else 1)
