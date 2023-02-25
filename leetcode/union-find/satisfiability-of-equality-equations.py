# https://leetcode.com/problems/satisfiability-of-equality-equations/


class Solution:
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, a, b):
        a = self.find(parent, a)
        b = self.find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    def equationsPossible(self, equations: List[str]) -> bool:
        hashmap = {}
        parent = [i for i in range(555)]
        ne = []
        for equation in equations:
            a, b = equation[0], equation[3]
            if a not in hashmap:
                hashmap[a] = len(hashmap) + 1
            if b not in hashmap:
                hashmap[b] = len(hashmap) + 1

            a = hashmap[a]
            b = hashmap[b]

            if "==" in equation:
                self.union(parent, a, b)
            else:
                ne.append((a, b))

        for a, b in ne:
            if self.find(parent, a) == self.find(parent, b):
                return False
        return True
