# https://www.acmicpc.net/problem/7432

import sys
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path):
        node = self.root
        for dir in path:
            node = node.children[dir]
        node.is_end = True

    def iterator(self, root, depth=0):
        for node in sorted(root.children.keys()):
            print(" " * depth, node, sep="")
            self.iterator(root.children[node], depth + 1)


input = lambda: sys.stdin.readline().rstrip()
n = int(input())
trie = Trie()
for _ in range(n):
    path = input().split("\\")
    trie.insert(path)

trie.iterator(trie.root)
