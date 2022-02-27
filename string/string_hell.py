# https://www.acmicpc.net/problem/20166

import sys
from collections import defaultdict


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
            node = node.children[char]
        return node.word


def dfs(i, j, string):
    string += graph[i][j]
    if len(string) > 5:
        return

    if trie.search(string):
        hash[string] += 1

    for k in range(8):
        nx = (i + dx[k]) % n
        ny = (j + dy[k]) % m
        dfs(nx, ny, string)


input = lambda: sys.stdin.readline().rstrip()
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]
n, m, k = map(int, input().split())
trie = Trie()
graph = []
for _ in range(n):
    graph.append(input())

wanted = []
for _ in range(k):
    word = input()
    wanted.append(word)
    trie.insert(word)

hash = defaultdict(int)
for i in range(n):
    for j in range(m):
        dfs(i, j, "")

for word in wanted:
    print(hash[word])
