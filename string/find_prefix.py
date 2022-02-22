# https://www.acmicpc.net/problem/14426
# 이분 탐색도 가능

from collections import defaultdict
import sys


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def find_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return 1


input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
trie = Trie()
for _ in range(n):
    trie.insert(input())

print(sum([trie.find_prefix(input()) for _ in range(m)]))
