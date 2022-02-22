# https://www.acmicpc.net/problem/5670

import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()


class TrieNode:
    def __init__(self):
        self.push = 0
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

    def update_push_count(self, root, i=1):
        root.push = i
        if len(root.children) > 1 or root.word == True:
            if root != self.root:
                i += 1
        for x in root.children:
            self.update_push_count(root.children[x], i)

    def get_push_count(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        return node.push


while 1:
    try:
        trie = Trie()
        n = int(input())
        words = []
        for _ in range(n):
            word = input()
            trie.insert(word)
            words.append(word)

        answer = 0
        trie.update_push_count(trie.root)
        for word in words:
            answer += trie.get_push_count(word)

        print("{:.2f}".format(answer / n))
    except:
        break
