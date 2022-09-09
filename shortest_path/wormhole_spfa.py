from collections import defaultdict, deque

for tc in range(int(input())):
    n, m, w = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))

    INF = 9876543210
    for start in range(1, n + 1):
        distance = [INF] * (n + 1)
        distance[start] = 0
        q = deque()
        q.append(start)
        update = [0] * (n + 1)
        on = [0] * (n + 1)
        on[start] = 1
        cycle = False
        while q:
            x = q.popleft()
            on[x] = 0

            for y, cost in graph[x]:

                if distance[y] > distance[x] + cost:
                    distance[y] = distance[x] + cost
                    if not on[y]:
                        q.append(y)
                        update[y] += 1
                        on[y] = 1
                        if update[y] == n:
                            cycle = True
                            q.clear()
                            break
        if cycle:
            break

    if cycle:
        print("YES")
    else:
        print("NO")
