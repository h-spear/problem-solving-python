# https://www.acmicpc.net/problem/14725

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, info):
        node = self.root
        for word in info:
            node = node.children[word]
        node.is_end = True

    def iterator(self, root, i=0):
        for word in sorted(root.children.keys()):
            print("--" * i, word, sep="")
            self.iterator(root.children[word], i + 1)


n = int(input())
trie = Trie()
for _ in range(n):
    _, *info = input().split()
    trie.insert(info)
trie.iterator(trie.root)
