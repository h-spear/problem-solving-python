# https://www.acmicpc.net/problem/13424

for tc in range(int(input())):
    n, m = map(int, input().split())
    INF = float("inf")
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    min_dist = INF
    answer = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        distance[a][b] = c
        distance[b][a] = c

    k = int(input())
    cur = list(map(int, input().split()))

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    distance[i][j] = 0
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    # 방 k에서 만날 경우
    for r in range(1, n + 1):
        dist = 0
        for i in cur:
            dist += distance[r][i]
        if min_dist > dist:
            min_dist = dist
            answer = r

    print(answer)
