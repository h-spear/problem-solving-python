# https://www.acmicpc.net/problem/13505
# 2진수를 10진수로 변환 : int('binary number(String)', 2)

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.data = None
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, bin):
        node = self.root
        for char in bin:
            node = node.children[char]
        node.data = bin

    def search(self, bin):
        node = self.root

        for char in bin:
            next = "1" if char == "0" else "0"
            if next in node.children:
                node = node.children[next]
            else:
                node = node.children[char]

        a = int(bin, 2)
        b = int(node.data, 2)
        return a ^ b


trie = Trie()
n = int(input())
nums = list(map(int, input().split()))
mst = len(format(max(nums), "b"))
bins = []
for num in nums:
    b = format(num, "b")
    b = (mst - len(b)) * "0" + b
    bins.append(b)
    trie.insert(b)

answer = -1
for bin in bins:
    answer = max(answer, trie.search(bin))
print(answer)
