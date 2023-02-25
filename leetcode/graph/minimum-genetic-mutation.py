# https://leetcode.com/problems/minimum-genetic-mutation/

from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        choice = "ACGT"
        bank = set(bank)

        def bfs(start):
            visited = set()
            q = deque([start])
            visited.add(start)
            count = -1
            while q:
                count += 1
                for _ in range(len(q)):
                    gene = q.popleft()

                    if gene == end:
                        return count

                    for i in range(8):
                        for new in choice:
                            if new == gene[i]:
                                continue

                            new_gene = gene[:i] + new + gene[i + 1 :]

                            if new_gene not in bank:
                                continue
                            if new_gene in visited:
                                continue

                            q.append(new_gene)
                            visited.add(new_gene)
            return -1

        return bfs(start)
