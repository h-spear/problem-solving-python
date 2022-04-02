# https://www.acmicpc.net/problem/1091

n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
want = [0, 1, 2] * (n // 3)
visited = set()
answer = 0
while 1:
    if want == p:
        print(answer)
        break

    temp = [0] * n
    for i in range(n):
        temp[s[i]] = p[i]

    if tuple(temp) in visited:
        print(-1)
        break

    p = temp
    visited.add(tuple(p))
    answer += 1
