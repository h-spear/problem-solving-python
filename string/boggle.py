# https://www.acmicpc.net/problem/9202

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

    def start_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def dfs(i, j, word, visited):
    global found, longest, score
    if visited[i][j]:
        return
    if len(word) > 8:
        return
    if trie.start_with(word) == False:
        return

    word += graph[i][j]
    if trie.search(word):
        found.add(word)
        if len(longest) < len(word):
            longest = word
        elif len(longest) == len(word):
            longest = sorted([longest, word])[0]

    for k in range(8):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            continue
        visited[i][j] = 1
        dfs(nx, ny, word, visited)
        visited[i][j] = 0


input = lambda: sys.stdin.readline().rstrip()
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
score_hash = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11}
w = int(input())
trie = Trie()

for _ in range(w):
    word = input()
    trie.insert(word)
_ = input()

b = int(input())
for cnt in range(b):
    found = set()
    score = 0
    graph = []
    longest = ""
    for _ in range(4):
        graph.append(input())

    for i in range(4):
        for j in range(4):
            visited = [[0] * 4 for _ in range(4)]
            dfs(i, j, "", visited)

    for word in found:
        score += score_hash[len(word)]
    print(score, longest, len(found))

    if cnt == b - 1:
        break
    _ = input()
