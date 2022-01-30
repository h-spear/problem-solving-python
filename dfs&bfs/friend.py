# https://www.acmicpc.net/problem/1058

n = int(input())
graph = [list(input()) for _ in range(n)]

answer = 0


def is_two_friend(a, b):
    for i, x in enumerate(graph[a]):
        if x == "Y":
            if graph[i][b] == "Y":
                return 1
    return 0


for i in range(n):
    friends = 0
    for _i, x in enumerate(graph[i]):
        if i == _i:
            continue
        if x == "Y":
            friends += 1
            continue
        friends += is_two_friend(i, _i)
    answer = max(answer, friends)

print(answer)
