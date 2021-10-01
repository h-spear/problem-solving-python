# https://www.acmicpc.net/problem/1182

n, s = map(int, input().split())
li = list(map(int, input().split()))

answer = 0
for i in range(n):
    now = li[i]
    for j in range(i + 1, n):
        if now == s:
            answer += 1

        now += li[j]

print(answer)
