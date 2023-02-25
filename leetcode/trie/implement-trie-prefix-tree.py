# https://leetcode.com/problems/implement-trie-prefix-tree/

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        p = self.root
        for char in word:
            p = p.children[char]
        p.is_word = True

    def search(self, word: str) -> bool:
        p = self.root
        for char in word:
            if char not in p.children:
                return False
            p = p.children[char]
        return p.is_word

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for char in prefix:
            if char not in p.children:
                return False
            p = p.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
