# https://leetcode.com/problems/word-ladder/

import heapq
from collections import defaultdict, deque

# bfs : 통과
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        word_length = len(wordList[0])

        if endWord not in word_set:
            return 0

        q = deque([beginWord])
        answer = 0
        while q:
            answer += 1
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return answer

                for i in range(word_length):
                    pre = word[:i]
                    old = word[i]
                    suf = word[i + 1 :]
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        if char == old:
                            continue
                        new_word = pre + char + suf
                        if new_word in word_set:
                            word_set.remove(new_word)
                            q.append(new_word)

        return 0


# dijkstra : 시간초과
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def is_edge(word1, word2):
            count = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    count += 1
                if count > 1:
                    return False

            return count == 1

        graph = defaultdict(set)
        word_count = len(wordList)
        for i in range(word_count):
            word1 = wordList[i]

            if is_edge(word1, beginWord):
                graph[beginWord].add(word1)

            for j in range(i + 1, word_count):
                word2 = wordList[j]
                if is_edge(word1, word2):
                    graph[word1].add(word2)
                    graph[word2].add(word1)

        # dijkstra
        INF = float("inf")
        distance = defaultdict(lambda: INF)
        distance[beginWord] = 1
        heap = [(0, beginWord)]
        while heap:
            dist, word = heapq.heappop(heap)

            if dist > distance[word]:
                continue

            for next_word in graph[word]:
                cost = dist + 1
                if distance[next_word] > cost:
                    distance[next_word] = cost
                    heapq.heappush(heap, (cost, next_word))

        # impossible
        if distance[endWord] == INF:
            return 0
        return distance[endWord] + 1
