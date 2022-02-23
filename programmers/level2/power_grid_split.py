# https://programmers.co.kr/learn/courses/30/lessons/86971

from collections import defaultdict, deque


def solution(n, wires):
    answer = 10000
    graph = defaultdict(list)
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start, b):
        q = deque([start])
        visited = [0] * (n + 1)
        visited[start] = 1
        cnt = 1
        while q:
            x = q.popleft()

            for next in graph[x]:
                if x == start and next == b:
                    continue
                if visited[next]:
                    continue
                q.append(next)
                visited[next] = 1
                cnt += 1
        return cnt

    for a, b in wires:
        result = abs(bfs(a, b) - bfs(b, a))
        answer = min(answer, result)

    return answer
