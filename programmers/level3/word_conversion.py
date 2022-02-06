# https://programmers.co.kr/learn/courses/30/lessons/43163
# 코딩테스트 고득점 Kit : dfs/bfs

from collections import deque


def one_change_check(word1, word2):
    cnt = 0
    for a, b in zip(word1, word2):
        if a == b:
            continue
        cnt += 1
    return cnt == 1


def bfs(begin, target, words):
    q = deque([(begin, 0)])
    visited = set()
    visited.add(begin)
    while q:
        now, t = q.popleft()
        if now == target:
            return t

        for word in words:
            if word in visited:
                continue
            if not one_change_check(now, word):
                continue
            q.append((word, t + 1))
            visited.add(word)

    return 0


def solution(begin, target, words):
    return bfs(begin, target, words)
