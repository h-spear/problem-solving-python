# https://leetcode.com/problems/word-ladder-ii/
# hard *****

import heapq
from collections import defaultdict, deque


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        def get_diff_count(word1, word2):
            count = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    count += 1
            return count

        # generate graph
        # 왜 두 개씩? -> set
        graph = defaultdict(set)
        word_count = len(wordList)
        for i in range(word_count):
            for j in range(i + 1, word_count):
                word1 = wordList[i]
                word2 = wordList[j]
                if get_diff_count(word1, word2) == 1:
                    graph[word1].add(word2)
                    graph[word2].add(word1)

        for word in wordList:
            if get_diff_count(beginWord, word) == 1:
                graph[beginWord].add(word)
                graph[word].add(beginWord)

        # min distance
        INF = float("inf")
        distance = defaultdict(lambda: INF)

        # endWord부터 계산
        distance[endWord] = 0
        heap = []
        heapq.heappush(heap, (0, endWord))
        while heap:
            dist, word = heapq.heappop(heap)
            for next_word in graph[word]:
                if distance[word] + 1 < distance[next_word]:
                    distance[next_word] = distance[word] + 1
                    heapq.heappush(heap, (distance[next_word], next_word))

        # endWord -> beginWord 도달할 수 없으면 [] return.
        if distance[beginWord] == INF:
            return []

        # bfs
        q = deque()
        q.append((beginWord, distance[beginWord], [beginWord]))
        answer = []
        while q:
            word, dist, path = q.popleft()

            if word == endWord:
                answer.append(path.copy())
                continue

            for next_word in graph[word]:
                # 최단거리로 도착하지 않으면 건너뜀
                if distance[next_word] != dist - 1:
                    continue
                q.append((next_word, dist - 1, path + [next_word]))

        return answer
