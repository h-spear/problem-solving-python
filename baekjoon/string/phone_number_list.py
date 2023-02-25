# https://www.acmicpc.net/problem/5052

import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()


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

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            if node.word == True:
                return False
            node = node.children[char]
        return node.word


for tc in range(int(input())):
    n = int(input())
    trie = Trie()
    words = []
    for _ in range(n):
        word = input()
        trie.insert(word)
        words.append(word)

    consistency = True
    for word in words:
        if trie.search(word) == False:
            consistency = False
            break

    if consistency:
        print("YES")
    else:
        print("NO")
