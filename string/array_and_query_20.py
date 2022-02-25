# https://www.acmicpc.net/problem/16903
# zfill로 이진수 앞 자리를 쉽게 맞춰줄 수 있음
# format(number, "b").zfill(30)

import sys
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.data = None
        self.count = 0
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, bin):
        node = self.root
        node.count += 1
        for char in bin:
            node = node.children[char]
            node.count += 1
        node.data = bin

    def remove(self, bin):
        node = self.root
        node.count -= 1
        for char in bin:
            node = node.children[char]
            node.count -= 1

    def XOR(self, bin):
        node = self.root
        for char in bin:
            next = "1" if char == "0" else "0"
            if next in node.children and node.children[next].count >= 1:
                node = node.children[next]
            else:
                node = node.children[char]

        print(int("0b" + bin, 2) ^ int("0b" + node.data, 2))


input = lambda: sys.stdin.readline().rstrip()
trie = Trie()
trie.insert("0" * 30)
m = int(input())
for _ in range(m):
    cmd, x = map(int, input().split())
    x = format(x, "b").zfill(30)
    if cmd == 1:
        trie.insert(x)
    elif cmd == 2:
        trie.remove(x)
    elif cmd == 3:
        trie.XOR(x)
